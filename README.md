# automated-speedtest
Automated speedtest analyser using chrome headless feature

## Requirements

 - Python3 and virtualenv (python3-virtualenv)
 - A google chrome that support headless mode. The latest versions supports by default this mode (https://www.google.com/chrome)
 - You also should have `bsdtar` installed in order for make recipe to unpack the webdriver correctly.
 
## How to run

just type: 
```
make
```
to boostrap the virtualenv and install all the necessary python dependencies.

Then, once dependencies has been fecthed, you can do: 
```
make run
```
to run the tool and start testing your connection against multiple providers. 
For the moment, it's only support speedtest.net and speedof.me. Plan is to add some more. 

## TODO

 - Add support for multiple browsers (firefox, opera, safari?).
 - Instead of taking pictures of the results, parse the DOM, retrieve results and print it.
 - Add continuous integration support, write unit tests (travis).

## Contribution

I would be honored to received some PR and I will attached a high attention on reviewing them. You're welcome! :-)