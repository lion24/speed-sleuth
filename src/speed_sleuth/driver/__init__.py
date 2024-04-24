import abc
from typing import Any


class DriverInterface(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (
            hasattr(subclass, "find_element")
            and callable(subclass.find_element)
            and hasattr(subclass, "wait_to_be_visible")
            and callable(subclass.wait_to_be_visible)
            and hasattr(subclass, "wait_for_element")
            and callable(subclass.wait_for_element)
            and hasattr(subclass, "wait_for_button_clickable")
            and callable(subclass.wait_for_button_clickable)
            and hasattr(subclass, "get")
            and callable(subclass.get)
            and hasattr(subclass, "cleanup")
            and callable(subclass.cleanup)
            or NotImplemented
        )

    @classmethod
    @abc.abstractmethod
    def find_element(cls, by="id", value: str | None = None) -> Any:
        pass

    @classmethod
    @abc.abstractmethod
    def wait_to_be_visible(cls, element: Any, timeout: int = 90) -> bool:
        pass

    @classmethod
    @abc.abstractmethod
    def wait_for_element(
        cls, locator: tuple[str, str], timeout: int = 120
    ) -> Any:
        """Should return an instance to the element pointed by the locator.
        For example in selenium it would be a WebElement instance
        """
        pass

    @classmethod
    @abc.abstractmethod
    def wait_for_button_clickable(
        cls, locator: tuple[str, str], timeout: int = 120
    ) -> Any:
        """Should return a pointer to a button element once this one is
        considered clickable

        Raises:
            NoSuchElementException: raised when no element was found under the
                specified locator.
        """
        pass

    @classmethod
    @abc.abstractmethod
    def get(cls, url: str):
        pass

    @classmethod
    @abc.abstractmethod
    def cleanup(cls, errno=0):
        pass
