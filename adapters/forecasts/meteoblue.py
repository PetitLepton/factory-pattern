# Standard Library
from typing import List, Optional

# Application
from use_case.forecasts.interface import WeatherProvider, WeatherProviderBuilder


class Meteoblue(WeatherProvider):
    def get_models(self) -> List[str]:
        return ["BASIC_MLM", "GEM15"]


class MeteoblueBuilder(WeatherProviderBuilder):
    def __init__(self) -> None:
        self._instance: Optional[WeatherProvider] = None

    def __call__(self) -> WeatherProvider:
        if self._instance is None:
            self._instance = Meteoblue()
        return self._instance
