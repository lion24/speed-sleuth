import sys, os

sys.path.insert(0, os.path.abspath('lib'))

from speedtestprovider.speedtest import Speedtest


speedtest = Speedtest()
speedtest.run()
