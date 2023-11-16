# standard library
from pkgutil import get_data


# dependencies
from deshima_rawdata import cli


# constants
DATA_LIST = get_data("deshima_rawdata", "data.csv")


def test_download() -> None:
    pass


def test_cli_list() -> None:
    assert cli.list("csv") == DATA_LIST.decode()
