# flake8: noqa
import click

from speed_sleuth.browser import BrowserFactory
from speed_sleuth.driver.selenium import SeleniumDriver
from speed_sleuth.provider.speedofme import *  # to import object into the global table.
from speed_sleuth.provider.speedtest import *  # to import object into the global table.

providers = ["speedtest", "speedofme"]


@click.command(help="speed_sleuth is a tool to conduct automated speedtest")
@click.option(
    "-c",
    "--count",
    type=click.INT,
    default=1,
    help="the provider to test against",
)
@click.argument("providers", nargs=-1, type=click.Choice(providers))
def main(count, providers):
    if not providers:
        raise click.UsageError("You must specify at least one provider.")

    browser = BrowserFactory.get_browser()

    driver = SeleniumDriver(browser)

    for provider in providers:
        class_name = provider.capitalize()
        ProviderClass = globals().get(class_name)
        if ProviderClass:
            instance = ProviderClass(driver)
            for i in range(count):
                instance.run(f"{provider}-{i}.png")
        else:
            print(f"No class found for provider {provider}")


if __name__ == "__main__":
    main()
