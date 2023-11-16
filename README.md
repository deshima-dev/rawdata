# rawdata

[![Release](https://img.shields.io/pypi/v/deshima-rawdata?label=Release&color=cornflowerblue&style=flat-square)](https://pypi.org/project/deshima-rawdata/)
[![Python](https://img.shields.io/pypi/pyversions/deshima-rawdata?label=Python&color=cornflowerblue&style=flat-square)](https://pypi.org/project/deshima-rawdata/)
[![Downloads](https://img.shields.io/pypi/dm/deshima-rawdata?label=Downloads&color=cornflowerblue&style=flat-square)](https://pepy.tech/project/deshima-rawdata)
[![Tests](https://img.shields.io/github/actions/workflow/status/deshima-dev/rawdata/tests.yaml?label=Tests&style=flat-square)](https://github.com/deshima-dev/rawdata/actions)

DESHIMA raw data and downloader package

## Use of the data

Please contact [@astropenguin](https://github.com/astropenguin) before using the data.

## Download the data

```shell
$ pip install deshima-rawdata
$ deshima-rawdata download <observation ID>
```

See the command help for more information.

```shell
$ deshima-rawdata download --help
```

## List of the data

```shell
$ deshima-rawdata list
```

|   Observation ID | File name                    | Source name   | Observation type   |
|-----------------:|:-----------------------------|:--------------|:-------------------|
|   20231108052231 | cosmos_20231108052231.tar.gz | Jupiter       | raster             |
|   20231109015146 | cosmos_20231109015146.tar.gz | Jupiter       | zscan              |
|   20231109060113 | cosmos_20231109060113.tar.gz | Blank sky     | skydip             |
