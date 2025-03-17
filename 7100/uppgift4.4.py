def caesar_break(text):
    results = []
    for shift in range(26): 
        decrypted_text = ''
        for char in text:
            if char.isalpha(): 
                is_upper = char.isupper()
                base = ord('A') if is_upper else ord('a')
                decrypted_text += chr((ord(char) - base - shift) % 26 + base)
            else:
                decrypted_text += char 
        results.append((shift, decrypted_text)) 
    return results


encrypted_text = input("Skriv text att knäcka: ") 
results = caesar_break(encrypted_text)

print("\nAlla möjliga dekrypteringar:")
for shift, result in results:
    print(f"Skift {shift:2}: {result}")