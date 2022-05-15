import sys


def convert(num, verbose=True):
    res = ""
    index = 0
    original = num # used if verbose is true
    while num != 0:
        remainder = num % 2
        if verbose:
            print(f"{num} = 2 * {num // 2} + {remainder} * 2^{index}")
            index += 1
        num = num // 2

        # append the remainder to the front of exisiting sequence
        res = str(remainder) + res
    
    if verbose:
        print(f"{original} (base 10) -> {res} (base 2)")
    return res

def test():
    res = convert(verbose=False, num=38)
    if res != "100110":
        return False
    return True

if __name__ == "__main__":
    try:
        num = int(input("Enter an integer: "))
    except ValueError:
        print(f"Input cannot be converted to integer type")
        sys.exit()
    
    if test() == True:
        res = convert(num)
    else:
        print("Incorrect implementation")