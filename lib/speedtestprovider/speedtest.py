# coding: utf-8
from speedtestprovider import SpeedtestProvider


class Speedtest(SpeedtestProvider):
    def __init__(self):
        super().__init__("http://beta.speedtest.net")

    def run(self):
        try:
            gobtn = self.driver.find_element_by_css_selector('a.js-start-test')
            gobtn.click()
            print("[+] running speedtest.net, please wait")
            # Block until Go btn is available again
            self.wait_for_clickable('a.js-start-test')
            print("[+] done, taking snapshot of the website results")
            self.driver.get_screenshot_as_file('speedtest-results.png')
        except:
            print("An error occured, cleaning up...")
            self.cleanup(-1)

        self.cleanup()

    def parseResults(self):
        pass
