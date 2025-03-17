def caesar_decrypt(text):
    decrypted_text = ''
    for char in text:
        if char.isalpha(): 
            is_upper = char.isupper()
            base = ord('A') if is_upper else ord('a')
            decrypted_text += chr((ord(char) - base - 1) % 26 + base)
        else:
            decrypted_text += char 
    return decrypted_text


input_text = input("Skriv text att dekryptera: ")
decrypted_message = caesar_decrypt(input_text)
print(f"Dekrypterat: {decrypted_message}")