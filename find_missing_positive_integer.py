'''
Given an array of integers, find the first missing positive integer in linear time and constant space. In other
words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and
negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.
'''


def missing_pos_int(input_list: list) -> int:
    highest = 0
    lowest = input_list[0]
    poss_gap = 0
    prev_num = input_list[0]
    for i in input_list:

        # curr low checked against absolute value of list item so negative numbers do not affect it.
        if i < 0:
            continue
        if i == poss_gap:
            poss_gap = 0
        if i - prev_num > 1 or prev_num - i > 1 and i > 0:
            poss_gap = min(i, prev_num) + 1
        lowest = min(abs(lowest), abs(i))
        highest = max(i, highest)
        prev_num = i
    if poss_gap > 0:
        return poss_gap
    if lowest <= 0 and highest == 0:
        return 1
    if lowest > 1:
        return lowest - 1
    else:
        return highest +1


def main():
    input_list = [-120, 100, 0, 101, 102, 103]  # 1
    print("the lowest positive missing int from {} is {}".format(input_list, str(missing_pos_int(input_list))))

    input_list = [3, 4, -1, 1]
    print("the lowest positive missing int from {} is {}".format(input_list, str(missing_pos_int(input_list))))

    input_list = [1, 2, 0]  # 3
    print("the lowest positive missing int from {} is {}".format(input_list, str(missing_pos_int(input_list))))

    input_list = [1, 2, 3]  # 4
    print("the lowest positive missing int from {} is {}".format(input_list, str(missing_pos_int(input_list))))

    input_list = [4,5,6,7,10] #1
    print("the lowest positive missing int from {} is {}".format(input_list, str(missing_pos_int(input_list))))

    input_list = [-1,-12,1,4] #3
    print("the lowest positive missing int from {} is {}".format(input_list, str(missing_pos_int(input_list))))


if __name__ == "__main__":
    main()
