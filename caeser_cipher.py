def caesar_cipher(message, shift):
    # Confirm arguments are the correct type
    if not isinstance(message, str):
        raise TypeError("Message must be a string.")
    
    elif not isinstance(shift, int):
        raise TypeError("Shift must be an integer.")
    
    # Otherwise, arguments must be correct
    else:
        # Initialize an output
        output = ""

        # Iterate through each character in string
        for char in message:
            # If character is alphabetic
            if char.isalpha():

                # Get the ordinal value starting at "A" or "a"
                # Convert character to 0-based index
                if char.isupper():
                    start = ord('A')
                elif char.islower():
                    start = ord('a')

                # Add shift to character ordinal value
                # Modulus by 26 so shift will wrap around the alphabet,(z becomes b, etc.)
                # Add character to output
                shifted_ord = (ord(char) - start + shift) % 26 + start
                output += chr(shifted_ord)

            # If character is not alphabetic, add it to output without modification
            else:
                output += char
        # Return the final output
        return output
    

test_1 = caesar_cipher("abc", 3) #Output:  "def"  
test_2 = caesar_cipher("xyz", 2) #Output:  "zab"  
test_3 = caesar_cipher("Hello, World!", 5) #Output:  "Mjqqt, Btwqi!"

print(test_3)