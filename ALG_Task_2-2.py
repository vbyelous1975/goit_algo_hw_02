from collections import deque


def if_polindrome(input_string):
    input_string = input_string.lower().replace(" ","")
    d = deque(input_string)

    while len(d) > 1:
        if d.pop() != d.popleft():
            print("This is not polindrome")
            return False
        print("This is polindrome")
        return True
if_polindrome("asdsA")