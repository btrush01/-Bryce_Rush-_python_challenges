def find_max(numbers):
    if numbers == []:
        raise ValueError("The list is empty.")

    elif not isinstance(numbers, list):
        raise TypeError("Input must be a list.")

    else:
        maximum = numbers[0]
        i = 0

        for n in numbers:
            if n > maximum:
                maximum = n
                i = numbers.index(n)

        return (maximum, i)

test_1 = [-1, 0, 3, 7]
test_2 = []
test_3 = "Hello world!"


print(f"The (maximum, index) is {find_max(test_1)}")