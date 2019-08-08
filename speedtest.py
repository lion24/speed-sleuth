import argparse
from provider.speedtest import Speedtest

parser = argparse.ArgumentParser()
parser.add_argument("-c", "--count", type=int, default=1)
args = parser.parse_args()

speedtest = Speedtest()
for i in range(args.count):
    speedtest.run("speedtest-{}.png".format(i))
