'''
This problem was recently asked by Google.

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
'''


def sum_two_nums_from_list_to_k(a_list, k):
    print("Given a list of numbers and a number k, return whether any two numbers from the list add up to k.")
    print(f"the list = {str(a_list)}, and k = {k}")
    list_of_nums_seen = []
    ret_list_of_answers = []
    for new_num in a_list:
        for old_num in list_of_nums_seen:
            sum_of_nums = new_num + old_num
            if sum_of_nums == k:
                # print(f"{new_num} + {old_num} = {k}")
                ret_list_of_answers.append((new_num, old_num))
        list_of_nums_seen.append(new_num)
    print(str(ret_list_of_answers))
    return ret_list_of_answers


def main():
    the_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, -1, 18]
    k = 13
    # the_list = [10, 15, 3, 7]
    sum_two_nums_from_list_to_k(the_list, k)


if __name__ == "__main__":
    main()