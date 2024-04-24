# coding: utf-8
# Disable broad-except for now, will refine later.
# pylint: disable=broad-except
"""Generic Provider class which provides an abstraction for the different
drivers we would like to use."""

import abc


class Provider(metaclass=abc.ABCMeta):
    """Each driver will be derive from this Abstract provider class.

    This class also contains generic methods which needs to be
    implemented in the concrete provider classes.

    """

    @classmethod
    def __subclasshook__(cls, subclass):
        return (
            hasattr(subclass, "run")
            and callable(subclass.run)
            and hasattr(subclass, "parse_results")
            and callable(subclass.parse_results)
            or NotImplemented
        )

    @classmethod
    @abc.abstractmethod
    def run(cls, filename):
        """Actual method that would trigger the test for the given provider."""

    @classmethod
    @abc.abstractmethod
    def parse_results(cls):
        """Method that would gather results from the speedtest for the given
        provider."""
