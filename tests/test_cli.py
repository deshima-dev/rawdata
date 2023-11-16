# standard library
from os import environ as env


# dependencies
from deshima_rawdata import cli


def test_cli_download() -> None:
    for obsid in cli.DATA_LIST.index:
        cli.download(obsid, tag=env["GITHUB_SHA"])


def test_cli_list() -> None:
    assert cli.list("csv") == cli.DATA_LIST.to_csv()
