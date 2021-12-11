def read_input(filename):
    with open(filename) as f:
        content = f.readlines()
    lines = [x.strip("\n") for x in content]
    data = []
    for line in lines:
        left, right = line.split(" | ")
        data.append((left.split(), right.split()))
    return data


def solve_part_one(displays):
    res = 0
    unique_segments_length = (2, 4, 3, 7)
    for display in displays:
        res += sum([1 for x in display[1] if len(x) in unique_segments_length])
    return res


def solve_part_two(displays):
    total_sum = 0
    unique_segments_length = (2, 4, 3, 7)

    for display in displays:
        curr_sum = "" 

        unique_segments = {l: set(segment) for segment in display[0] 
            if (l := len(segment)) in unique_segments_length}

        for segment in display[1]:
            # trivial cases since they are unique
            if len(segment) == 2:
                curr_sum += "1"
            elif len(segment) == 4:
                curr_sum += "4"
            elif len(segment) == 3:
                curr_sum += "7"
            elif len(segment) == 7:
                curr_sum += "8"
            
            # Non-trivial cases with multiple possibilities
            seg_set = set(segment)
            num_overlaps = lambda x: len(seg_set.intersection(x))

            # len(segment) == 5 are the numbers 2, 3, and 5
            if len(segment) == 5:
                # If the curr segment has two intersections with the 1,
                # it needs to be the 3
                if num_overlaps(unique_segments[2]) == 2:
                    curr_sum += "3"
                # the 2 has two intersections with the 4
                elif num_overlaps(unique_segments[4]) == 2:
                    curr_sum += "2"
                else:
                    curr_sum += "5"
            
            # len(segment) == 6 are the numbers 0, 6, 9
            elif len(segment) == 6:
                # 6 is the only number with only one intersection with the 1
                if num_overlaps(unique_segments[2]) == 1:
                    curr_sum += "6"
                # 9 has four intersections with the 4
                elif num_overlaps(unique_segments[4]) == 4:
                    curr_sum += "9"
                else:
                    curr_sum += "0"
        
        total_sum += int(curr_sum)

    return total_sum


if __name__ == "__main__":
    input_data = read_input("input.txt")

    print(solve_part_one(input_data))
    print(solve_part_two(input_data))
