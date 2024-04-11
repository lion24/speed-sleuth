Speed Sleuth 🕵️ [![Tests](https://github.com/lion24/speed-sleuth/actions/workflows/test.yml/badge.svg?branch=main)](https://github.com/lion24/speed-sleuth) [![codecov](https://codecov.io/gh/lion24/speed-sleuth/graph/badge.svg?token=A4VHEY9KTT)](https://codecov.io/gh/lion24/speed-sleuth)
![GH Page deploy](https://github.com/lion24/speed-sleuth/actions/workflows/docs.yml/badge.svg)
====
Automated speedtest analyser using chrome headless feature

## Requirements

 - Python3 and `hatch` https://hatch.pypa.io/latest/
 - A browser supported by the selenium framework (currently only Chromium and Edge implemented)

## How to run

just type:

```sh
hatch run main
```

to run the tool and start testing your connection against multiple providers.
For the moment, it's only support speedtest.net and speedof.me. Plan is to add some more.

You can only test against a single provider, for example speedtest:

```sh
hatch run main -p speedtest
```

## Some notes

Install editable dependencies: https://setuptools.pypa.io/en/latest/userguide/development_mode.html

```sh
hatch -e default shell
python -m pip install --editable .
```

## TODO

 - Add support for multiple browsers (firefox, opera, safari?).
 - Instead of taking pictures of the results, parse the DOM to retrieve results.
 - ~Add continuous integration support (travis)~ done, write unit tests and extend coverage.

## Contribution

I would be honored to receive some PR and I will attach a high attention on reviewing them. You're welcome! :-)
