def calculate_concrete(length: float, width: float, depth: float):
    volume = length * width * depth

    return {
        "volume_m3": round(volume,2)
    }

