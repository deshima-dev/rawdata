__all__ = ["download"]


# standard library
from pathlib import Path


# dependencies
from fire import Fire
from requests import get
from tqdm import tqdm
from . import __version__


# constants
CHUNK_SIZE = 1024
GITHUB_URL = "https://raw.githubusercontent.com/deshima-dev/rawdata"
DEFAULT_TAG = f"v{__version__}"


def download(
    obsid: str,
    /,
    *,
    dir: Path = Path(),
    progress: bool = True,
    tag: str = DEFAULT_TAG,
) -> Path:
    """Download DESHIMA raw data for given observation ID.

    Args:
        obsid: Observation ID (YYYYmmddHHMMSS).
        dir: Directory where the raw data is saved.
        progress: Whether to show a progress bar.
        tag: Git tag (or branch) of the raw data.

    Returns:
        Path of the downloaded raw data.

    """
    url = f"{GITHUB_URL}/{tag}/data/{obsid}.tar.gz"

    if not (response := get(url, stream=True)).ok:
        response.raise_for_status()

    bar_options = {
        "disable": not progress,
        "total": int(response.headers["content-length"]),
        "unit": "B",
        "unit_scale": True,
    }
    data_path = Path(dir) / response.url.split("/")[-1]

    with tqdm(**bar_options) as bar, open(data_path, "wb") as f:
        for data in response.iter_content(CHUNK_SIZE):
            bar.update(len(data))
            f.write(data)

    return data_path


def main() -> None:
    """Entry point of the deshima-rawdata command."""
    Fire({"download": download})
