def is_prime(number):
    if not isinstance(number, int):
        raise TypeError("Input must be a positive integer.")

    elif number < 0:
        raise ValueError("Negative numbers are not prime.")
    
    else:
        for i in range (2, number):
            if number % i == 0:
                return False
            else:
                return True
            
test_1 = 7
test_2 = -3
test_3 = "Hello World!"

print(f"Is {test_1} a prime number? {is_prime(test_1)}")