'''
This problem was asked by Jane Street.

cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair. For
example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.

Given this implementation of cons:

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair
Implement car and cdr.
'''


#FUNCs
def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair


# NOTE: __closure__ magic function in Python. A closure is a function object that remembers values in enclosing scopes
# even if they are not present in memory. The __closure__ attribute of a closure function returns a tuple of cell
# objects.

# NOTE: “Cell” objects are used to implement variables referenced by multiple scopes. For each such variable,
# a cell object is created to store the value; the local variables of each stack frame that references the value
# contains a reference to the cells from outer scopes which also use that variable.

# because there are two variables in the scopes, i have access to 2 cell values via __closure__ attribute on the
# function object returned by pair(), and to access the cell values you use .cell_contents!
def car(pair):
    return pair.__closure__[0].cell_contents


def cdr(pair):
    return pair.__closure__[1].cell_contents


#main
def main():
    print(car(cons(3, 4)))
    print(cdr(cons(3, 4)) )


if __name__ == "__main__":
    main()