#!/usr/bin/env python
# flake8: noqa

import argparse
import sys

try:
    from speed_sleuth.browser.chromium import ChromiumBrower
    from speed_sleuth.provider.speedofme import *  # to import object into the global table.
    from speed_sleuth.provider.speedtest import *  # to import object into the global table.
except Exception as e:
    print("Fail to load provider: ", e)
    sys.exit(1)

providers = ["speedtest", "speedofme"]

parser = argparse.ArgumentParser()
parser.add_argument("-c", "--count", type=int, default=1)
parser.add_argument(
    "-p", "--providers", choices=providers, default=providers, nargs="+"
)
args = parser.parse_args()

for provider in args.providers:
    class_name = provider.capitalize()
    ProviderClass = globals().get(class_name)
    if ProviderClass:
        instance = ProviderClass(ChromiumBrower())
        for i in range(args.count):
            instance.run(f"{provider}-{i}.png")
    else:
        print(f"No class found for provider {provider}")
