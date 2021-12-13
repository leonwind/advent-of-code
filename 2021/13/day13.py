def read_input(filename):
    with open(filename) as f:
        content = f.readlines()
    rows = [x.strip("\n") for x in content]
    points = set()
    folds = []
    for row in rows:
        if not row:
            continue
        
        if row.startswith("fold along"):
            entry = row[len("fold along "):]
            axis, size = entry.split("=")
            folds.append((axis, int(size)))
        else:
            x, y = row.split(",")
            points.add((int(x), int(y)))
    
    return points, folds


def _fold_paper(points, fold):
    new_points = set()

    if fold[0] == 'y':
        for point in points:
            if point[1] < fold[1]:
                new_points.add(point)
            else:
                new_y = fold[1] - (point[1] - fold[1])
                new_points.add((point[0], new_y))
    
    elif fold[0] == 'x':
        for point in points:
            if point[0] < fold[1]:
                new_points.add(point)
            else:
                new_x = fold[1] - (point[0] - fold[1])
                new_points.add((new_x, point[1]))
    
    return new_points 


def solve_part_one(points, fold):
    points = _fold_paper(points, fold)
    return len(points)


def solve_part_two(points, folds):
    for fold in folds:
        points = _fold_paper(points, fold)
    
    num_cols = max([point[0] for point in points]) + 1
    num_rows = max([point[1] for point in points]) + 1
    matrix = [[" " for _ in range(num_cols)] for _ in range(num_rows)]

    for x, y in points:
        matrix[y][x] = '#'

    return matrix    


if __name__ == "__main__":
    points, folds = read_input("input.txt")

    print(solve_part_one(points, folds[0]))
    
    matrix = solve_part_two(points, folds)
    for row in matrix:
        print(row)