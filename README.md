# dso-mgr

[![Tests][badge-tests]][tests]
[![Documentation][badge-docs]][documentation]

[badge-tests]: https://img.shields.io/github/actions/workflow/status/Boehringer-Ingelheim/dso-mgr/test.yaml?branch=main
[badge-docs]: https://img.shields.io/readthedocs/dso-mgr

Automatically run the correct version of dso through uv

## Getting started

Please refer to the [documentation][],
in particular, the [API documentation][].

## Installation

You need to have Python 3.10 or newer installed on your system.
If you don't have Python installed, we recommend installing [Mambaforge][].

There are several alternative options to install dso-mgr:

<!--
1) Install the latest release of `dso-mgr` from [PyPI][]:

```bash
pip install dso-mgr
```
-->

1. Install the latest development version:

```bash
pip install git+https://github.com/Boehringer-Ingelheim/dso-mgr.git@main
```

## Release notes

See the [changelog][].

## Contact

For questions and help requests, you can reach out in the [scverse discourse][].
If you found a bug, please use the [issue tracker][].

## Citation

> t.b.a

[mambaforge]: https://github.com/conda-forge/miniforge#mambaforge
[scverse discourse]: https://discourse.scverse.org/
[issue tracker]: https://github.com/Boehringer-Ingelheim/dso-mgr/issues
[tests]: https://github.com/Boehringer-Ingelheim/dso-mgr/actions/workflows/test.yml
[documentation]: https://dso-mgr.readthedocs.io
[changelog]: https://dso-mgr.readthedocs.io/en/latest/changelog.html
[api documentation]: https://dso-mgr.readthedocs.io/en/latest/api.html
[pypi]: https://pypi.org/project/dso-mgr
