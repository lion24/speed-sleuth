#coding: utf-8

from abc import ABC, abstractmethod
from selenium import webdriver

class SpeedtestProvider(ABC):
    def __init__(self, target):
        self.target = target
        options = webdriver.ChromeOptions()
        options.binary_location = '/usr/bin/chromium-browser'
        options.add_argument('headless')
        options.add_argument('window-size=1200x800')
        options.add_argument('lang=en_US')
        self.driver = webdriver.Chrome(chrome_options=options)
        self.driver.get(target)
    
    @abstractmethod
    def run(self):
        raise "Should be implemented in daughter class"

    @abstractmethod
    def parseResults(self):
        raise "Should be implemented in daughter class"

