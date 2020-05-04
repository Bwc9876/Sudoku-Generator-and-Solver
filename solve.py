

def solve(tiles, screen):
    for x in tiles:
        if x.number == 0:
            for y in range(1, 10):
                x.number = y
                if not Check(x, tiles):
                    x.number = y
                    if not CheckGrid(tiles):
                        print('Done')
                        return tiles
                    else:
                        if solve(tiles, screen):
                            return tiles
            break
    x.number = 0


def CheckGrid(tiles):
    results = []
    nums = []
    for i in tiles:
        results += [Check(i, tiles)]
        nums += [i.number]
    if 0 in nums:
        return True
    return True in results


def Check(tile, tiles):
    for s in tiles:
        if not s == tile:
            if not s.number == 0:
                if tile.row == s.row and tile.number == s.number:
                    return True
                if tile.col == s.col and tile.number == s.number:
                    return True
                if tile.net == s.net and tile.number == s.number:
                    return True
    return False
