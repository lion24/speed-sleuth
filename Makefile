PLATFORM := linux64
VERSION=$(shell curl https://googlechromelabs.github.io/chrome-for-testing/LATEST_RELEASE_STABLE)
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
	curl -o /tmp/driver.zip https://storage.googleapis.com/chrome-for-testing-public/$(VERSION)/$(PLATFORM)/chromedriver-$(PLATFORM).zip \
  		&& unzip -oj /tmp/driver.zip -d env/bin && rm -rf /tmp/driver.zip

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
	find . -name '.pytest_cache' -exec rm -fr {} +

run: clean
	python main.py

test: clean
	pytest -q tests

.PHONY: env clean lint
