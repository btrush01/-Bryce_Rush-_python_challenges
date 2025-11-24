#Basic solution
def reverse_string(string):
    return string[::-1]

test_1 = "Hello World"
print(reverse_string(test_1))




#As a for loop
def reverse_string_for(string):
    new_string = ""
    i = -1

    for letter in string:
        current_character = string[i]
        new_string += current_character
        i -= 1

    return new_string
    
test_2 = "Coding is easy"
print(reverse_string_for(test_2))