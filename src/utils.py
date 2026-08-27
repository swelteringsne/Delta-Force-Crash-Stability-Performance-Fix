# Build: 048ea47297d8cc9deaa6df5e3734a526

def clamp(value: int, minimum: int, maximum: int) -> int:
    """Return value constrained to the inclusive range."""
    return max(minimum, min(maximum, value))
