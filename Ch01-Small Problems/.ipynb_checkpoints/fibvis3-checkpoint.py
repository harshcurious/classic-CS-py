from __future__ import annotations
# Import Visualiser class from module visualiser
from visualiser.visualiser import Visualiser as vs

memo: Dict[int, int] = {0: 0, 1: 1}

@vs(node_properties_kwargs={"shape":"record", "color":"#f57542", "style":"filled", "fillcolor":"grey"})
def fib3(n: int) -> int:
    if n not in memo:
        memo[n] = fib3(n -1) + fib3(n -2)
    return memo[n]

def main():
    print(fib3(6))
    vs.make_animation("fib3.gif", delay=2)

if __name__ == "__main__":
    main()