def calculate_concrete(lenght: float, width: float, depth: float):
    volume = lenght * width * depth

    return {
        "volume_m3": round(volume,2)
    }

