from tools.concrete import calculate_concrete
from tools.brick import estimate_bricks
from tools.weather import get_weather

TOOLS = {
    "concrete_calculator": calculate_concrete,
    "brick_estimator": estimate_bricks,
    "weather": get_weather,
}
