# Author: Bishal Sarang

# Import Visualiser class from module visualiser
from visualiser.visualiser import Visualiser as vs

# Add decorator
# Decorator accepts optional arguments: ignore_args , show_argument_name, show_return_value and node_properties_kwargs
@vs(node_properties_kwargs={"shape":"record", "color":"#f57542", "style":"filled", "fillcolor":"grey"})
def fibvis2(n):
    if n < 2:
        return n
    return fibvis2(n - 1) + fibvis2(n - 2)


def main():
    # Call function
    print(fibvis2(6))
    # Save recursion tree to a file
    vs.make_animation("fib2.gif", delay=2)


if __name__ == "__main__":
    main()