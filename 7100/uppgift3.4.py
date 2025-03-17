def caesar_encrypt_custom(text, shift):
    encrypted_text = ''
    for char in text:
        if char.isalpha(): 
            is_upper = char.isupper()
            base = ord('A') if is_upper else ord('a')  
            encrypted_text += chr((ord(char) - base + shift) % 26 + base)
        else:
            encrypted_text += char 
    return encrypted_text


input_text = input("Skriv text att kryptera: ")
shift = int(input("Ange skift (antal steg): ")) 
encrypted_message = caesar_encrypt_custom(input_text, shift)
print(f"Krypterat: {encrypted_message}")