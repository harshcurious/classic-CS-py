from __future__ import annotations
# Import Visualiser class from module visualiser
from visualiser.visualiser import Visualiser as vs
from functools import lru_cache


# Ordering in Decorators
## the lwer one is run faster
## in other words:
## fib4 will first be wrapped in @vs
## then the result is rewrapped in @lru_cache

@lru_cache(maxsize=None)
@vs(node_properties_kwargs={"shape":"record", "color":"#f57542", "style":"filled", "fillcolor":"grey"})
def fib4(n: int) -> int:
    if n < 2:
        return n
    return fib4(n -2) + fib4(n - 1)

def main():
    print(fib4(6))
    vs.make_animation("fib4.gif", delay=2)

if __name__  == "__main__":
    main()