__all__ = ["download", "list"]


# standard library
import tarfile
from pathlib import Path


# dependencies
import pandas as pd
from fire import Fire
from requests import get
from tqdm import tqdm
from . import __version__


# constants
CHUNK_SIZE = 1024
DATA_LIST = pd.read_csv(
    Path(__file__).with_name("data.csv"),
    index_col=0,
    dtype={0: str},
)
DATA_REPO_URL = "https://github.com/deshima-dev/rawdata"
DEFAULT_DATA_TAG = f"v{__version__}"
DEFAULT_LIST_FORMAT = "markdown"


def download(
    obsid: str,
    /,
    *,
    dir: Path = Path(),
    extract: bool = False,
    progress: bool = False,
    tag: str = DEFAULT_DATA_TAG,
) -> Path:
    """Download DESHIMA raw data for given observation ID.

    Args:
        obsid: Observation ID (YYYYmmddHHMMSS).
        dir: Directory where the raw data is saved.
        extract: Whether to extract the raw data.
        progress: Whether to show a progress bar.
        tag: Git tag (or branch) of the raw data.
            Note this is for development use only.

    Returns:
        Path of the downloaded raw data.

    """
    file_name = Path(DATA_LIST["File name"][str(obsid)])
    url = f"{DATA_REPO_URL}/raw/{tag}/data/{file_name}"

    if not (response := get(url, stream=True)).ok:
        response.raise_for_status()

    bar_options = {
        "disable": not progress,
        "total": int(response.headers["content-length"]),
        "unit": "B",
        "unit_scale": True,
    }
    data_path = Path(dir) / file_name

    with tqdm(**bar_options) as bar, open(data_path, "wb") as f:
        for data in response.iter_content(CHUNK_SIZE):
            bar.update(len(data))
            f.write(data)

    if not extract:
        return data_path

    with tarfile.open(data_path, "r:gz") as tar:
        tar.extractall(data_path.parent)
        dir_name = tar.getnames()[0]

    data_path.unlink(True)
    return data_path.with_name(dir_name)


def list(format: str = DEFAULT_LIST_FORMAT) -> str:
    """List DESHIMA raw datasets available in the package.

    Args:
        format: Format of the list that can be output by pandas.

    Returns:
        String of the list with given format.

    """
    return getattr(DATA_LIST, f"to_{format}")()


def main() -> None:
    """Entry point of the deshima-rawdata command."""
    Fire({"download": download, "list": list})
