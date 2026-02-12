import random
import time
# Cipher task
# Simulates a network call with sleep and randomness

def run(input:str, retries:int, **kwargs):
    # Takes an input string, makes it lowercase, ciphers it by a random amount, then tries to brute-force resolve the cipher
    # Returns either the cipher shift value (if discovered) or a failure message
    original_string = input.lower()
    offset_value = random.randint(1, 25)
    
    ciphered_string = encode_string(original_string, offset_value)
    print(f"Ciphered: {ciphered_string}")
    print("Attempting to decode")
    success, shift_value = attempt_decrypt(ciphered_string, retries, original_string)
    time.sleep(random.randint(1, 5))
    if success:
        print(f"Success! The string was ciphered with a shift value of {shift_value}")
        return True
    else: 
        print(f"Failure! The correct cipher was not guessed despite {retries} attempts.")
        return False
    
    
def attempt_decrypt(ciphered_text:str, retries:int, original_text:str):
    print(f"{ciphered_text} <----> {original_text}")
    for i in range(retries):
        decoded_string, shift_value = random_decode_string(ciphered_text)
        if compare_strings(original_text, decoded_string):
            return True, shift_value
    return False, None
    
    
def compare_strings(original_string:str, decoded_string:str) -> bool:
    if original_string == decoded_string:
        return True
    else:
        return False
    
def random_decode_string(input_text:str):
    shift_value = random.randint(1, 25)
    return decode_string(input_text, shift_value), shift_value
    
def decode_string(input_text:str, shift_value:int) -> str:
    output_text = ""
    for char in input_text:
        if not char.isalpha():
            output_text += char
            continue
        
        val: int = get_char_value(char)
        shifted_val = (val - shift_value) % 26
        char = chr(ord('a') + shifted_val)
        output_text += char
    return output_text
    
    
    

def encode_string(input_text:str, shift_value:int):
    output_text = ""
    for char in input_text: 
        if not char.isalpha():
            output_text += char
            continue
        
        val: int = get_char_value(char)
        shifted_val = (val + shift_value) % 26
        char = chr(ord('a') + shifted_val)
        output_text += char
    return output_text
        

def get_char_value(char:str):
    val = ord(char) - ord('a')
    return val

def test(in_string):
    print(f"Testing {in_string}")
    
    encoded_string = encode_string(in_string, 1)
    print(f"Encoded: {encoded_string}")
    


if __name__ == "__main__":
    main(input="Hello, World!", retries=26)