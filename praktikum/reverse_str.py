def balik_string(input_string):
    reversed_string = ""

    for i in range(len(input_string) - 1, -1, -1):
        reversed_string += input_string[i]

    print(reversed_string)
