def to_meters(feet):
    meters = feet * 0.3048
    return round(meters, 2)

def to_feet(meters):
    feet = meters / 0.3048
    return round(feet, 2)
