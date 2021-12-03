def read_input(filename):
    with open(filename) as f:
        content = f.readlines()
    return [x.strip("\n") for x in content]


def solve_part_one(binary_numbers):
    gamma = ""
    epsilon = ""
    for i in range(len(binary_numbers[0])):
        num_zeroes = 0
        num_ones = 0
        for binary_num in binary_numbers:
            if binary_num[i] == '1':
                num_ones += 1
            else:
                num_zeroes += 1

        if num_ones > num_zeroes:
            gamma += '1'
            epsilon += '0'
        else:
            gamma += '0'
            epsilon += '1'
    
    return int(gamma, 2) * int(epsilon, 2)


def solve_part_two(binary_numbers):
    o2_nums = binary_numbers
    co2_nums = binary_numbers

    for i in range(len(binary_numbers[0])):
        o2_one_counts = 0
        for num in o2_nums:
            o2_one_counts += (1 if num[i] == '1' else 0)

        co2_one_counts = 0
        for num in co2_nums:
            co2_one_counts += (1 if num[i] == '1' else 0)
        
        if len(o2_nums) > 1:
            o2_size = len(o2_nums)
            o2_nums = [num for num in o2_nums if num[i] == ('1' if o2_one_counts >= o2_size / 2.0 else '0')]

        if len(co2_nums) > 1:
            co2_size = len(co2_nums) 
            co2_nums = [num for num in co2_nums if num[i] == ('0' if co2_one_counts >= co2_size / 2.0 else '1')]
    
    o2 = int(o2_nums[0], 2)
    co2 = int(co2_nums[0], 2)
    return o2 * co2


if __name__ == "__main__":
    input_data = read_input("input.txt")

    print(solve_part_one(input_data))
    print(solve_part_two(input_data))
