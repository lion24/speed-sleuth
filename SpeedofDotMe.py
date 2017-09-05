#coding: utf-8
import time
from SpeedtestProvider import SpeedtestProvider

class SpeedofDotMe(SpeedtestProvider):
    def __init__(self):
        super().__init__("http://speedof.me")

    def run(self):
       startbtn = self.driver.find_element_by_css_selector('button#btnStart')
       startbtn.click()
       print("[+] running speedof.me, please wait")
       time.sleep(70)
       print("[+] done, taking snapshot of the website results")
       self.driver.get_screenshot_as_file('speedofme-results.png') 
        
    def parseResults(self):
        pass
