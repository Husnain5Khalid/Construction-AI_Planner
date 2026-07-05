def estimate_bricks(length: float, height: float):
    wall_area = length * height
    bricks = wall_area * 60

    return{
        "wall_area": round(wall_area, 2),
        "estimated_bricks": int(bricks)
    }

'''
The Problem We're Solving

Suppose the user asks:

Estimate bricks for an 8 m × 3 m wall.

The AI needs to answer:

Wall Area = 24 m²

Estimated Bricks = 1440

Where Does 60 Come From?
bricks = wall_area * 60

is using a simplified assumption:

1 square meter of wall
≈ 60 standard bricks
'''