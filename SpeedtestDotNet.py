#coding: utf-8
import time
from SpeedtestProvider import SpeedtestProvider


class SpeedtestDotNet(SpeedtestProvider):
    def __init__(self):
        super().__init__("http://beta.speedtest.net")

    def run(self):
       gobtn = self.driver.find_element_by_css_selector('a.js-start-test') 
       gobtn.click()
       print("[+] running speedtest.net, please wait")
       time.sleep(60)
       print("[+] done, taking snapshot of the website results")
       self.driver.get_screenshot_as_file('speedtest-progress.png')
       self.driver.close()

    def parseResults(self):
        pass

