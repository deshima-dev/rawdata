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


def download(
    obsid: str,
    /,
    *,
    dir: Path = Path(),
    progress: bool = True,
) -> Path:
    """Download DESHIMA raw data for given observation ID.

    Args:
        obsid: Observation ID (YYYYmmddHHMMSS).
        dir: Directory where the raw data is saved.
        progress: Whether to show a progress bar.

    Returns:
        Path of the downloaded raw data.

    """
    url = f"{GITHUB_URL}/v{__version__}/data/{obsid}.tar.gz"

    if not (response := get(url, stream=True)).ok:
        response.raise_for_status()

    bar_options = {
        "disable": not progress,
        "total": int(response.headers.get("content-length", 0)),
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
