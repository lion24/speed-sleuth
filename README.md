# Speed Sleuth 🕵️ [![Tests](https://github.com/lion24/speed-sleuth/actions/workflows/test.yml/badge.svg?branch=main)](https://github.com/lion24/speed-sleuth) [![codecov](https://codecov.io/gh/lion24/speed-sleuth/graph/badge.svg?token=A4VHEY9KTT)](https://codecov.io/gh/lion24/speed-sleuth) ![GH Page deploy](https://github.com/lion24/speed-sleuth/actions/workflows/docs.yml/badge.svg)

Automated speedtest analyser using selenium and a compatible browser.

## Compatibility matrix

| Operating System | ![Chrome](https://raw.githubusercontent.com/alrra/browser-logos/master/src/chrome/chrome_48x48.png) | ![Firefox](https://raw.githubusercontent.com/alrra/browser-logos/master/src/firefox/firefox_48x48.png) | ![IE](https://raw.githubusercontent.com/alrra/browser-logos/master/src/edge/edge_48x48.png) | ![Safari](https://raw.githubusercontent.com/alrra/browser-logos/master/src/safari/safari_48x48.png) | ![Opera](https://raw.githubusercontent.com/alrra/browser-logos/master/src/opera/opera_48x48.png) |
| ---------------- | --------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------ |
| Windows          | :interrobang:                                                                                       | :grey_question:                                                                                        | :white_check_mark:                                                                          | N/A                                                                                                 | :grey_question:                                                                                  |
| macOS            | :white_check_mark:                                                                                  | :grey_question:                                                                                        | :x:                                                                                         | :grey_question:                                                                                     | :grey_question:                                                                                  |
| Linux            | :white_check_mark:                                                                                  | :grey_question:                                                                                        | :x:                                                                                         | N/A                                                                                                 | :grey_question:                                                                                  |

- :white_check_mark: - tested, works fine
- :warning: - not for production use
- :grey_question: - will work in the future (help out if you can)
- :interrobang: - maybe works, not tested
- :x: no support planned

## Supported provider

| Provider                                                       | Supported ?        |
| -------------------------------------------------------------- | ------------------ |
| [Speedtest.net](https://speedtest.net)                         | :white_check_mark: |
| [Speedof.me](https://speedof.me/)                              | :white_check_mark: |
| [fast.com](https://fast.com/)                                  | :grey_question:    |
| [Google Fiber Speed Test](https://fiber.google.com/speedtest/) | :grey_question:    |
| [TestMy.net](https://testmy.net/)                              | :grey_question:    |

- :white_check_mark: - tested, works fine
- :grey_question: - will work in the future (help out if you can)

Focusing here on the top 5 most used providers. But other might be integrated.
Feel free to add new ones.

## Requirements

- Python3 and `hatch` https://hatch.pypa.io/latest/
- A browser supported by the selenium framework (currently only Chromium and Edge implemented)

## How to run

You can test against different providers:

```sh
hatch env run speed-sleuth -- <providers ...>
```

To test against speedtest.net:

```sh
hatch env run speed-sleuth -- speedtest
```

To test against multiple providers, for example speedtest.net and speedof.me (one test at a time)

```sh
hatch env run speed-sleuth -- speedtest speedofme
```

If running with hatch it's better to escape hatch arguments from the program arguments using `--`.

You can get help using:

```sh
hatch env run speed-sleuth -- --help
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
> on your machine.

## TODO

- Add support for multiple browsers (see compatibility matrix)
- Instead of taking pictures of the results, parse the DOM to retrieve results.

## Contribution

I would be honored to receive some PR and I will attach a high attention on reviewing them. You're welcome! :-)
