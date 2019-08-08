# coding: utf-8
"""
Generic Provider class which provides an abstraction for the different drivers
we would like to use.
"""

import time
import sys
import traceback
from abc import ABC, abstractmethod
from selenium import webdriver
from selenium.common.exceptions import (
    StaleElementReferenceException,
    TimeoutException
)
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Provider(ABC):
    """
    Each driver will be derive from this Abstract provider class.
    This class also contains generic methods which needs to be implemented
    in the concrete provider classes.
    """
    def __init__(self, target):
        self.target = target
        self.driver = self.driver_init()
        self.driver.get(target)

    @staticmethod
    def driver_init():
        """
        Init a driver. Right now, only chrome is support, plan is to add support for
        more drivers.
        """
        options = webdriver.ChromeOptions()
        options.binary_location = '/usr/bin/google-chrome'
        options.add_argument('--headless')
        options.add_argument('--window-size=1400x900')
        options.add_argument('--disable-gpu')
        options.add_argument('--lang=en_US')
        return webdriver.Chrome(chrome_options=options)
        # As using selenium api > 2.x, this call should block until
        # readyState is hit.

    def wait_for_clickable(self, element, timeout=90):
        """
        Method that wait until an element is present and clickable in the DOM.
        """
        time.sleep(2)  # Hack, when element is clicked, it remains active for a
        # small period on the DOM before beeing staled.
        try:
            WebDriverWait(self.driver,
                          timeout,
                          poll_frequency=2,
                          ignored_exceptions=(StaleElementReferenceException)
                          ).until(
                              EC.element_to_be_clickable(
                                  (By.CSS_SELECTOR, element)))
        except TimeoutException as ex:
            print("Timeout in finding element {} from DOM, reason: {}"
                  .format(element, str(ex))
                  )
            raise
        except Exception:
            print("Unexpected error occured:", sys.exc_info()[0])
            raise

    def cleanup(self, errno=0, exp=None):
        """
        If any error occured, we will cleanup reserved resources.
        """
        if exp:
            print("An error occured: " + exp)
            traceback.print_exc()
        self.driver.close()
        self.driver.quit()
        self.driver = None
        if errno:
            sys.exit(errno)

    @abstractmethod
    def run(self):
        """
        Actual method that would trigger the test for the given provider.
        """
        raise "Should be implemented in daughter class"

    @abstractmethod
    def parse_results(self):
        """
        Method that would gather results from the speedtest for the given provider
        """
        raise "Should be implemented in daughter class"
