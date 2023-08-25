# Implement a function that adds two numbers together and returns their sum in binary. The conversion can be done before, or after the addition.

# The binary number returned should be a string.

# Examples:(Input1, Input2 --> Output (explanation)))

# 1, 1 --> "10" (1 + 1 = 2 in decimal or 10 in binary)
# 5, 9 --> "1110" (5 + 9 = 14 in decimal or 1110 in binary)
def add_binary(a,b):
    #your code here
    sum = a+b
    b_sum = []

    while(sum > 0):
        d = sum % 2
        b_sum.append(d)
        sum = sum // 2
    b_sum.reverse()

    binary_sum = ''

    for n in b_sum:
        binary_sum += str(n)

    return binary_sum
