'''
The question we'll work through is the following: return a new sorted merged list from K sorted lists,
each with size N. Before we move on any further, you should take some time to think about the solution!

First, go through an example. This buys time, makes sure you understand the problem, and lets you gain some intuition
for the problem. For example, if we had [[10, 15, 30], [12, 15, 20], [17, 20, 32]], the result should be [10, 12, 15,
15, 17, 20, 20, 30, 32].

Next, give any solution you can think of (even if it's brute force). It seems obvious that if we just flattened the
lists and sorted it, we would get the answer we want. The time complexity for that would be O(KN log KN),
since we have K * N total elements.

The third step is to think of pseudocode—a high-level solution for the problem. This is where we explore different
solutions. The things we are looking for are better space/time complexities but also the difficulty of the
implementation. You should be able to finish the solution in 30 minutes. Here, we can see that we only need to look
at K elements in each of the lists to find the smallest element initially. Heaps are great for finding the smallest
element. Let's say the smallest element is E. Once we get E, we know we're interested in only the next element of the
list that held E. Then we'd extract out the second smallest element and etc. The time complexity for this would be O(
KN log K), since we remove and append to the heap K * N times.

NOTE: this solution was written before their ANSWER in an email i read from them. Perhaps its not as 'efficient'
    [*] ill put their solution in a comment at the bottom of this script for FULL DISCLOSURE
'''

# important note for me at least is that we know the inner list sizes are all UNIFORM (= N)
def ret_complete_sorted_list(a_list_of_lists: list) -> list:
    if len(a_list_of_lists) == 1:
        ans_list = a_list_of_lists[0]
        return ans_list
    else:
        ans_list = a_list_of_lists[0].copy()
        ans_copy = ans_list.copy()
        print(f"initial answer list = {ans_list}")
        loop_var = 0
        for item in ans_copy:
            loop_var +=1
            for a_list in a_list_of_lists[1:]:
                curr_num = item
                for a_item in a_list.copy():
                    print(f"if {a_item} <= {curr_num}")
                    if a_item <= curr_num:
                        ans_list.insert(ans_list.index(curr_num), a_item)
                        a_list.remove(a_item)
                        print(f"inserted item in IF statement, now a_list = {a_list}")
                    elif len(a_list_of_lists[0]) == loop_var and len(a_list) > 0:
                        inserted_item = False
                        print(f"a_item = {a_item}, whats left = {a_list_of_lists[1:]}, ans_list = {ans_list}, a_list = {a_list}")
                        for item in ans_list:
                            if item > a_item:
                                ans_list.insert(ans_list.index(item), a_item)
                                a_list.remove(a_item)
                                print(f"inserted item {a_item} in ELIF statment, now a_list = {a_list}")
                                inserted_item = True
                                break
                        if not inserted_item:
                            ans_list.append(a_item)
                            print(f"last chance append now ans_list = {ans_list}")
                            a_list.remove(a_item)

                    else:
                        break
                    #elif type(a_item) == int and a_item > curr_num:
                    #    ans_list.append(a_item)
                    #    a_list[a_list.index(a_item)] = "x"
                print(f"new list = {a_list_of_lists}, {ans_list}")

        print(f"whats left = {a_list_of_lists[1:]}")

        #logic for anythng that is left
        #for

        return ans_list


def main():

    list_of_sorted_lists = [[12, 15, 20], [17, 20, 32], [10, 18, 30]]
    print("FINAL ANSWER: " + str(ret_complete_sorted_list(list_of_sorted_lists)))

    #list_of_sorted_lists = [[12, 15, 20], [10, 18, 30]], [17, 20, 32]
    # print("FINAL ANSWER: " + str(ret_complete_sorted_list(list_of_sorted_lists)))

    list_of_sorted_lists = [[17, 20, 32], [12, 15, 20], [10, 18, 30]]
    print("FINAL ANSWER: " + str(ret_complete_sorted_list(list_of_sorted_lists)))


if __name__ == "__main__":
    main()