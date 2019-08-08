# coding: utf-8
# Disable broad-except for now, will refine later.
# pylint: disable=broad-except
"""
speedof.me provider
"""

from provider import Provider


class SpeedofMe(Provider):
    """
    This provider is a representation of speedof.me
    It is used to perform tests against speedof.me
    """
    def __init__(self):
        super().__init__("http://speedof.me")

    def run(self, filename='speedofme-results.png'):
        try:
            startbtn = self.driver.find_element_by_css_selector(
                'button#btnStart')
            startbtn.click()
            print("[+] running speedof.me, please wait")
            self.wait_for_clickable('button#btnStart')
            print("[+] done, taking snapshot of the website results")
            self.driver.get_screenshot_as_file(filename)
        except Exception as exp:
            self.cleanup(-1, exp)

        self.cleanup()

    def parse_results(self):
        pass
