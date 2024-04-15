# coding: utf-8
# Disable broad-except for now, will refine later.
# pylint: disable=broad-except
"""Generic Provider class which provides an abstraction for the different
drivers we would like to use."""

from abc import ABC, abstractmethod

from speed_sleuth.driver import DriverInterface


class Provider(ABC):
    """Each driver will be derive from this Abstract provider class.

    This class also contains generic methods which needs to be
    implemented in the concrete provider classes.

    """

    def __init__(self, driver: DriverInterface):
        self.driver = driver

    @abstractmethod
    def run(self, filename):
        """Actual method that would trigger the test for the given provider."""
        raise NotImplementedError("Should be implemented in daughter class")

    @abstractmethod
    def parse_results(self):
        """Method that would gather results from the speedtest for the given
        provider."""
        raise NotImplementedError("Should be implemented in daughter class")
