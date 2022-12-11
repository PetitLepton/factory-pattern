# Standard Library
from typing import Any, Dict

# Application
from use_case.forecasts.interface import WeatherProvider, WeatherProviderBuilder


class WeatherProvidersFactory:
    def __init__(self):
        self._builders: Dict[str, WeatherProviderBuilder] = {}

    def register_builder(self, name: str, builder: WeatherProviderBuilder) -> None:
        self._builders[name] = builder

    def create(self, name: str, **kwargs: Any) -> WeatherProvider:
        builder = self._builders.get(name)
        if not builder:
            raise ValueError(name)
        return builder(**kwargs)