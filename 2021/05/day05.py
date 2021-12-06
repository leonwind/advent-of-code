def read_input(filename):
    with open(filename) as f:
        content = f.readlines()
    return [x.strip("\n") for x in content]


def parse_input(input_data):
    lines = []
    for row in input_data:
        start, end = row.split("->")
        start = tuple(int(x) for x in start.split(','))
        end = tuple(int(x) for x in end.split(','))
        lines.append((start, end))
    return lines 


def _build_fields(lines, part_two=False):
    points = {}

    for line in lines:
        x1, y1 = line[0]
        x2, y2 = line[1]

        if x1 != x2 and y1 != y2:
            if not part_two or abs(x2 - x1) != abs(y2 - y1):
                # Ignore diagonal points for part 1 or if the angle is not 45 degrees
                continue

            x_step = 1 if x2 > x1 else -1
            y_step = 1 if y2 > y1 else -1
            tmp_x, tmp_y = x1, y1

            for _ in range(abs(x2 - x1) + 1):
                if (tmp_x, tmp_y) in points:
                    points[(tmp_x, tmp_y)] += 1
                else:
                    points[(tmp_x, tmp_y)] = 1

                tmp_x += x_step
                tmp_y += y_step

        else:
            x1, x2 = sorted([x1, x2])
            y1, y2 = sorted([y1, y2])

            if x1 == x2:
                for y in range(y1, y2 + 1):
                    if (x1, y) in points:
                        points[(x1, y)] += 1
                    else:
                        points[(x1, y)] = 1 

            else:
                for x in range(x1, x2 + 1):
                    if (x, y1) in points:
                        points[(x, y1)] += 1
                    else:
                        points[(x, y1)] = 1 
                
    return len([k for k, v in points.items() if v >= 2]) 


def solve_part_one(lines):
    return _build_fields(lines) 


def solve_part_two(lines):
    return _build_fields(lines, part_two=True) 


if __name__ == "__main__":
    input_data = read_input("input.txt")
    lines = parse_input(input_data)
    #print(lines)

    print(solve_part_one(lines))
    print(solve_part_two(lines))
