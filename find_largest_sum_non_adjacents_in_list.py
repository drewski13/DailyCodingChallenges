'''
This problem was asked by Airbnb.

Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or
negative.

For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10,
since we pick 5 and 5.

Follow-up: Can you do this in O(N) time and constant space?
'''


def find_largest_non_adjacent_sum(a_list: list) -> str:
    list_of_lists_to_sum = []
    dict_of_largest_non_adjacent_nums_seen = {}
    curr_largest_num = -1
    for i, val in enumerate(a_list):
        if i == 0:
            list_of_lists_to_sum.append([val])
            dict_of_largest_non_adjacent_nums_seen[i] = [val]
            curr_largest_num = val
        elif i == 1:
            list_of_lists_to_sum.append([val])
            dict_of_largest_non_adjacent_nums_seen[i] = [val]
            if val > curr_largest_num:
                curr_largest_num = val
        else:
            if val >= curr_largest_num:
                curr_largest_num = val
                for k, v in dict_of_largest_non_adjacent_nums_seen.items():
                    if i - k > 1:
                        dict_of_largest_non_adjacent_nums_seen[k].append(val)
                dict_of_largest_non_adjacent_nums_seen[i] = [val]

            if i % 2 == 0:
                list_of_lists_to_sum[0].append(val)
            else:
                list_of_lists_to_sum[1].append(val)
    curr_largest = []
    for k, v in dict_of_largest_non_adjacent_nums_seen.items():
        if len(curr_largest) == 0:
            curr_largest = v
        else:
            if sum(v) > sum(curr_largest):
                curr_largest = v

    for inner_list in list_of_lists_to_sum:
        if sum(inner_list) > sum(curr_largest):
            curr_largest = inner_list

    largest_sum = sum(curr_largest)
    return f"the largest sum was {largest_sum}, from picking {curr_largest}"


def main():
    input_list = [2, 4, 6, 2, 5]  # should return 13, since we pick 2, 6, and 5
    print(find_largest_non_adjacent_sum(input_list))
    input_list = [5, 1, 1, 5]  # should return 10, since we pick 5 and 5
    print(find_largest_non_adjacent_sum(input_list))
    input_list = [1, 10, 1, 1, 10, 1]  # should return 20, since we pick 10 and 10
    print(find_largest_non_adjacent_sum(input_list))


if __name__ == "__main__":
    main()
