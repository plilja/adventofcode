def ulam_spiral_corners():
    corners_at_level = (1, 1, 1, 1)
    level = 1
    while True:
        yield corners_at_level
        (tr, tl, bl, br) = corners_at_level
        corners_at_level = (br + level + 1, br + 2 * (level + 1), br + 3 * (level + 1), br + 4 * (level + 1))
        level += 2


def step1(d):
    if d == 1:
        return 0
    u = ulam_spiral_corners()
    next(u) # Skip center
    layers = 1
    prev = 2
    for tr, tl, bl, br in u:
        stop = False
        if d <= tr:
            corner1 = prev
            corner2 = tr
            stop = True
        elif d <= tl:
            corner1 = tr
            corner2 = tl
            stop = True
        elif d <= bl:
            corner1 = tl
            corner2 = bl
            stop = True
        elif d <= br:
            corner1 = bl
            corner2 = br
            stop = True

        if stop:
            center = corner1 + (corner2 - corner1) // 2
            dist_to_center = abs(d - center)
            return layers + dist_to_center
        layers += 1
        prev = br + 1

d = int(input())
print(step1(d))
