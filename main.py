# Application
from adapters.forecasts import weather_providers_factory


meteoblue = weather_providers_factory.create("meteoblue")

print(meteoblue.get_models())