'''
Given an array of integers, return a new array such that each element at index i of the new array is the product
of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [
3, 2, 1], the expected output would be [2, 3, 6].

*****Follow-up: what if you can't use division
'''


def product_a_list(num_list: list) -> int:
    ans_int = 1
    for item in num_list:
        ans_int *= item
    return ans_int


# function to do this WITHOUT division
def ret_list_of_surrounding_product(num_list: list) -> list:
    ans_list = []
    for index in range(len(num_list)):
        ans_list.append(product_a_list(num_list[:index]) * product_a_list(num_list[index+1:]))

    return ans_list

def main():

    num_list = [1, 2, 3, 4, 5]
    print(str(ret_list_of_surrounding_product(num_list)))

    num_list = [3, 2, 1]
    print(str(ret_list_of_surrounding_product(num_list)))


if __name__ == "__main__":
    main()