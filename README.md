Automated-Speedtest [![Build Status](https://travis-ci.org/lion24/automated-speedtest.svg?branch=master)](https://travis-ci.org/lion24/automated-speedtest) [![Coverage Status](https://coveralls.io/repos/github/lion24/automated-speedtest/badge.svg?branch=master)](https://coveralls.io/github/lion24/automated-speedtest?branch=master)
====
Automated speedtest analyser using chrome headless feature

## Requirements

 - Python3 and virtualenv (python3-virtualenv)
 - A google chrome that support headless mode. The latest version supports by default this mode (https://www.google.com/chrome)
 - You should also have `bsdtar` installed to unpack the webdriver correctly.

## How to run

just type:
```
make
```
to bootstrap the virtualenv and install all the necessary python dependencies.

Then, once dependencies have been fetched, you can do:
```
make run
```
to run the tool and start testing your connection against multiple providers.
For the moment, it's only support speedtest.net and speedof.me. Plan is to add some more.

## TODO

 - Add support for multiple browsers (firefox, opera, safari?).
 - Instead of taking pictures of the results, parse the DOM to retrieve results.
 - ~Add continuous integration support (travis)~ done, write unit tests and extend coverage.

## Contribution

I would be honored to receive some PR and I will attach a high attention on reviewing them. You're welcome! :-)
