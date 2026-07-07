from tools.concrete import calculate_concrete
from tools.brick import estimate_bricks
from tools.weather import get_weather

TOOL_REGISTRY = {
    "concrete_calculator": calculate_concrete,
    "brick_estimator": estimate_bricks,
    "weather": get_weather,
}