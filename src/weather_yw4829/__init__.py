# read version from installed package
from importlib.metadata import version
__version__ = version("weather_yw4829")

from .weather_yw4829 import (
    celsius_to_fahrenheit,
    summarize_temperatures,
    clean_readings,
)
