from math import pi, sin, cos


def pt_on_cir(nums: int, radius: int, center: tuple[int]) -> list[tuple[int]]:
    """
    return the coordinate of points on the circle, points are evenly distributed.

    Parameters:
        - nums - nums of points is on the circle
        - radius - radius on the circle
        - center - center of the circle e.g. (x, y)

    Returns:
        - a list of all pt's coord in the format of (x, y)
    """
    section = pi * 2 / nums

    coords = []
    for i in range(nums):
        y = sin(section * i) * radius
        x = cos(section * i) * radius
        coords.append((center[0] + x, center[1] - y))

    return coords
