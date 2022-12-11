from abc import ABC, abstractmethod
from typing import Any, Callable, Dict, List, Optional
import logging

logger = logging.getLogger(name=__name__)


class WeatherProvider(ABC):
    @abstractmethod
    def get_models(self) -> List[str]:
        pass


class WeatherProviderBuilder(ABC):
    def __init__(self) -> None:
        self._instance: Optional[WeatherProvider] = None

    @abstractmethod
    def __call__(self, **kwargs: Any) -> WeatherProvider:
        pass
