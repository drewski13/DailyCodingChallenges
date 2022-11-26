'''
This problem was asked by Google.

An XOR linked list is a more memory efficient doubly linked list. Instead of each node holding next and prev fields,
it holds a field named both, which is an XOR of the next node and the previous node. Implement an XOR linked list; it
has an add(element) which adds the element to the end, and a get(index) which returns the node at index.

If using a language that has no pointers (such as Python), you can assume you have access to get_pointer and
dereference_pointer functions that converts between nodes and memory addresses.
'''
import ctypes
import sys

# helper functions for Python for pretend pointers
mem_dict = {}


def get_pointer(an_object):
    for mem_address, dict_object in mem_dict.items():
        if dict_object == an_object:
            return mem_address


def dereference_pointer(mem_address):
    return mem_dict[mem_address]


# CLASSES
class XorLinkedList:
    def __init__(self):
        self.start_node = None

    def add(self, data: str):
        # special case for the very first element being added
        if self.start_node is None:
            new_node = XorNode(data)
            # add to mem_dict for its fake pointer
            mem_dict[id(new_node)] = new_node
            print(mem_dict)
            # initializes to None because there is no other nodes yet!
            new_node.both = None
            mem = id(new_node)
            print(f"added a start node with no issues, data for it is '{new_node}' and its mem address is {mem}")
            self.start_node = new_node
            return

        # special case for only the 2nd element being add, gets much harder after that
        if self.start_node.both is None:
            new_node = XorNode(data)
            # add to mem_dict for its fake pointer
            mem_dict[id(new_node)] = new_node
            print(mem_dict)
            self.start_node.both = get_pointer(new_node)
            new_node.both = get_pointer(self.start_node)
            mem = id(new_node)
            print(f"added a second node with no issues, data for it is '{new_node}' and its mem address is {mem}")
            return

        # end of XOR doubly linked list is when the .both for a node is equal to the previous Node's address
        start_node_address = get_pointer(self.start_node)

        # n starts as the 2nd node in the list and will update each loop pass after XORing the .both
        # if .both == mem address of start_node then you know there is only 2 nodes and you can add next_node and return
        n = dereference_pointer(self.start_node.both)
        n_last = get_pointer(self.start_node)
        # ITERATE until the .both value is equal to the previous node's address
        while True:

            # special case for adding just the 3rd node
            if get_pointer(self.start_node) == n.both:
                new_node = XorNode(data)
                # add to mem_dict for its fake pointer
                mem_dict[id(new_node)] = new_node
                print(mem_dict)
                n.both = get_pointer(self.start_node) ^ id(new_node)
                new_node.both = get_pointer(n)
                mem = id(new_node)
                print(f"added a third node with no issues, data for it is '{new_node}' and its mem address is {mem}")
                print(f"[+] Node 1 has a .both == {n.both}")
                break
            else:
                # this would mean we found the last item in the list
                if n.both == n_last:
                    new_node = XorNode(data)
                    mem = id(new_node)
                    print(
                        f"added another node with no issues, data for it is '{new_node}' and its mem address is {mem}")
                    # add to mem_dict for its fake pointer
                    mem_dict[id(new_node)] = new_node
                    print(f"new dict for pointers = {mem_dict}")
                    # the last item's both value has to be updated to reflect prev and next XOR'd
                    n.both = n_last ^ id(new_node)
                    # add .both value to new_node which is just the address to the previous element
                    new_node.both = id(n)
                    break
                else:
                    # otherwise move to the next item in the list by XORing .both value with n_last address
                    # NOTE: this is the crux of a XOR doubly linked list. XORing two values allows you to get at both
                    # values by XORing the resultant value with either of the original values! (which is why XORing
                    # should not be used alone for cryptography)
                    temp_n_last = get_pointer(n)
                    n = dereference_pointer(n.both ^ n_last)
                    n_last = temp_n_last

    def get(self, index: int):
        print(f"------------doing a get for item with index {index}------------")
        print(mem_dict)
        for k, v in mem_dict.items():
            print(f"{v}(mem: {k}, .both: {v.both})")
        if index == 0:
            start_node_add = get_pointer(self.start_node)
            return dereference_pointer(start_node_add)
        elif index == 1:
            node_one_mem = self.start_node.both
            print(f"about to dereference the node 1 address of {node_one_mem}")
            return dereference_pointer(self.start_node.both)
        else:
            start_node_address = get_pointer(self.start_node)
            # looping with each pass getting the next node by xoring the current node's .both value with the previous
            # nodes address
            for x in range(index - 1):
                if x == 0:
                    current_node_address = self.start_node.both
                    curr_object = dereference_pointer(current_node_address)
                    curr_both = curr_object.both
                    next_node_address = curr_both ^ start_node_address
                    n_last_address = curr_both ^ next_node_address
                    next_node = dereference_pointer(next_node_address)
                    curr_both = next_node.both
                    # update last address to the address of the curr node, then the current node becomes the next node
                    n_last_address = get_pointer(curr_object)
                    curr_object = next_node
                else:
                    next_node_address = curr_both ^ n_last_address
                    next_node = dereference_pointer(next_node_address)
                    curr_both = next_node.both
                    # update last address to the address of the curr node, then the current node becomes the next node
                    n_last_address = get_pointer(curr_object)
                    curr_object = next_node
            wanted_node = dereference_pointer(next_node_address)
            # current_node_address = current_node.both ^ n_last_address
            return wanted_node  # dereference_pointer(current_node_address)


class XorNode:
    # NOTE: both here is an XOR'd value of prev and next nodes
    def __init__(self, data: str):
        self.both = None
        self.item = data

    def __repr__(self):
        return self.item


# MAIN
def main():
    new_xor_linked_list = XorLinkedList()
    new_xor_linked_list.add("Hello, World! from Start Node 1")
    # new_xor_linked_list.display_start()
    print(new_xor_linked_list.get(0))
    print("----------------------------------------")
    new_xor_linked_list.add("Node 2")
    print(new_xor_linked_list.get(1))
    new_xor_linked_list.add("Node 3")
    print(new_xor_linked_list.get(2))
    new_xor_linked_list.add("Node 4")
    print(new_xor_linked_list.get(3))
    new_xor_linked_list.add("Node 5")
    print(new_xor_linked_list.get(4))
    new_xor_linked_list.add("Node 6")
    print(new_xor_linked_list.get(5))
    new_xor_linked_list.add("Node 7")
    print(f"you wanted: {new_xor_linked_list.get(6)}")
    new_xor_linked_list.add("Node 8")
    print(f"you wanted: {new_xor_linked_list.get(7)}")


'''
    new_xor_linked_list.add("Node 2")
    n2 = new_xor_linked_list.get(2)
    try:
        print("the address of node 2 is: {}".format(id(n2)))
        # print("the size of node 1 is: {}".format(sys.getsizeof(n1)))
    except Exception as e:
        print(e)
    #print(new_xor_linked_list.get(2))
'''

if __name__ == "__main__":
    main()
