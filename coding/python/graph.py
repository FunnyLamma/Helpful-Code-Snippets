#This is a weird graph calculater, I don't know why you need it because if you can code you can probably do this in your head.#
import math

def graph():
    num1 = int(input("What is the first number?"))
    num2 = int(input("What is the second number?"))
    one_or_two = int(input("1 or 2"))
    if one_or_two == 1:
        ans1 = num2
        ans2 = -num1
        ans3 = [ans1, ans2]
        print(ans3)
    if one_or_two == 2:
        ans1 = -num2
        ans2 = num1
        ans3 = [ans1, ans2]
        print(ans3)
