'''
Given an array of integers, find the first missing positive integer in linear time and constant space. In other
words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and
negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.
'''


def missing_pos_int(input_list: list) -> int:
    lower_bound = -1
    upper_bound = -1
    num_loop_passes =0
    lowest_num_seen = 'a'
    # print(f"start list = {input_list}")
    for num in input_list:
        num_loop_passes += 1

        if num <= 0:
            continue

        elif num > lower_bound and num > upper_bound:
            old_upper_bound = upper_bound
            upper_bound = num
            if lower_bound == -1:
                lower_bound = num
            elif upper_bound - old_upper_bound > 0:
                lower_bound = old_upper_bound
        elif num < lower_bound and num < upper_bound:
            old_lower_bound = lower_bound
            lower_bound = num
            if upper_bound == -1:
                upper_bound = num
            elif old_lower_bound - lower_bound > 1:
                upper_bound = old_lower_bound
        elif num > lower_bound and num < upper_bound:
            lower_bound = num
        if lowest_num_seen == 'a' or lowest_num_seen >= num:
            lowest_num_seen = num
        # print(f"loop bounds: {lower_bound}, {upper_bound}")


    bounds_diff = upper_bound - lower_bound
    # print(f"lower bound = {lower_bound} , upper bound = {upper_bound} and lowest num seen = {lowest_num_seen}")
    if bounds_diff > 1:
        return lower_bound + 1
    elif lowest_num_seen > 1:
        ret_val = lowest_num_seen - 1
        return ret_val
    else:
        ret_val = upper_bound + 1
        return ret_val


    return 0


def main():

    input_list = [3, 4, -1, 1]  #2
    print("the lowest positive missing int from {} is {}".format(input_list, str(missing_pos_int(input_list))))

    input_list = [1, 2, 0] #3
    print("the lowest positive missing int from {} is {}".format(input_list, str(missing_pos_int(input_list))))

    input_list = [1,2,3] #4
    print("the lowest positive missing int from {} is {}".format(input_list, str(missing_pos_int(input_list))))

    input_list = [4,5,6,7,10] #1
    print("the lowest positive missing int from {} is {}".format(input_list, str(missing_pos_int(input_list))))

    input_list = [-1,-12,1,4] #3
    print("the lowest positive missing int from {} is {}".format(input_list, str(missing_pos_int(input_list))))

if __name__ == "__main__":
    main()