# coding: utf-8
"""
speedtest.net provider
"""
# Disable broad-except for now, will refine later.
# pylint: disable=broad-except

from selenium.common.exceptions import NoSuchElementException
from provider import Provider


class Speedtest(Provider):
    """
    This provider is used to perform test against speedtest.net
    """
    def __init__(self):
        super().__init__("https://www.speedtest.net/")

    def accept_eula(self):
        """
        Speedtest will ask you to accept license agreement before launching the test
        This function will click on the "I consent" button to allow test to proceed.
        """
        try:
            if self.driver.find_element_by_css_selector("#_evidon-banner-acceptbutton"):
                self.driver.execute_script(
                    "document.querySelector(\"#_evidon-banner-acceptbutton\").click();")
        except NoSuchElementException:
            pass #Silently ignore this exception which can occured.

    def run(self, filename='speedtest-result.png'):
        try:
            self.accept_eula()
            self.wait_for_clickable('a.js-start-test')
            self.driver.find_element_by_css_selector('a.js-start-test').click()
            print("[+] running speedtest.net, please wait")
            # Block until Go btn is available again
            self.wait_for_clickable('a.js-start-test')
            print("[+] done, taking snapshot of the website results")
            self.driver.get_screenshot_as_file(filename)
            # Dismiss speedtest modal.
            self.driver.find_element_by_css_selector("a.notification-dismiss").click()
        except Exception as exp:
            self.cleanup(-1, exp)

    def parse_results(self):
        pass
