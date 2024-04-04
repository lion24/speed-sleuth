#!/usr/bin/env python

import argparse
import sys


sys.path += ["lib"]


try:
    from provider.speedtest import Speedtest
    from provider.speedofme import Speedofme
    from browser.chromium import ChromiumBrower
except Exception as e:
    print("Fail to load provider: ", e)
    sys.exit(1)

providers = ["speedtest", "speedofme"]

parser = argparse.ArgumentParser()
parser.add_argument("-c", "--count", type=int, default=1)
parser.add_argument("-p", "--providers", choices=providers, default=providers, nargs="+")
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
