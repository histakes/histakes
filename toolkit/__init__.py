# Toolkit module - Simple vehicle operation functions


def brake(amount: float):
    """Apply brakes (0.0 = no brake, 1.0 = full brake)"""
    pass

def steer(angle: float, torque: float = None):
    """Steer the vehicle"""
    pass

def accelerate(amount: float):
    """Accelerate (0.0 = coast, 1.0 = full throttle)"""
    pass

def turn_signal(direction: str):
    """left, right, or off"""
    pass

def set_parking_brake(state: bool):
    """True = on, False = off"""
    pass

# Add more functions as needed (turn, lane_change, etc.)"