PLATFORM := linux64
VERSION=$(shell curl http://chromedriver.storage.googleapis.com/LATEST_RELEASE)
PROJECT_NAME := "automated-speedtest"
BOLD := \033[1m
RESET := \033[0m

export PYTHONPATH := $(PWD):$(PATH)
export PATH := env/bin:$(PATH)

all: env webdriver
	@echo "done, you can now do: source env/bin/activate"

env: requirements.txt
	$(RM) -rf $@
	virtualenv -p python3 $@ \
	&& . ./$@/bin/activate \
	&& pip install -Ur $<

webdriver:
ifeq (, $(shell which bsdtar))
	$(error "bsdtar is not install, consider doing apt-get install bsdtar")
endif
	curl http://chromedriver.storage.googleapis.com/$(VERSION)/chromedriver_$(PLATFORM).zip \
  	| bsdtar -xvf - -C env/bin/ 
	@chmod a+x env/bin/chromedriver

check: 
	@flake8

lint:
	@echo -e "$(BOLD)analyzing code for $(PROJECT_NAME)$(RESET)"
	-@pylint lib/**/*.py \
		--output-format text --reports no --output-format=colorized

clean:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

run: clean
	python3 speedtest.py

.PHONY: env clean lint
