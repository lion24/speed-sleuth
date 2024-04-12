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

## Testing

I started to write a bunch of unit tests because running the full test suite
using a real browser doing a real test is quite long and painful.
The goal is the achieve the best coverage using unit tests.

If for any reason, one of the provider decide to change the design or the css
class to activate the test, we are fucked.

That's why this is still important to run the integration tests against the real
providers on a regular basis. For now this is not the case. The plan is to have
a test that will be activate each night with a cron that will run the full integration
test suite.

### Some examples

Launch unit tests:
```sh
hatch run test:run -- -k unit
```

Launch the integration tests:
```sh
hatch run test:run -- -k integration
```

If you want to run the full test suite:
```sh
hatch run test:run
```
> Note: be aware that running the full test suite requires a supported browser installed
on your machine.

## TODO

 - Add support for multiple browsers (firefox, opera, safari?).
 - Instead of taking pictures of the results, parse the DOM to retrieve results.
 - ~Add continuous integration support (travis)~ done, write unit tests and extend coverage.

## Contribution

I would be honored to receive some PR and I will attach a high attention on reviewing them. You're welcome! :-)
