# Local
from .factory import WeatherProvidersFactory
from .meteoblue import MeteoblueBuilder


weather_providers_factory = WeatherProvidersFactory()
weather_providers_factory.register_builder(name="meteoblue", builder=MeteoblueBuilder())