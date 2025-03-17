def caesarchiffer(text):
    krypterad_text = ""
    
    for bokstav in text:
        if bokstav.isalpha():
            if bokstav.islower():
                ny_bokstav = chr((ord(bokstav) - ord('a') + 1) % 26 + ord('a'))
            elif bokstav.isupper():
                ny_bokstav = chr((ord(bokstav) - ord('A') + 1) % 26 + ord('A'))
            krypterad_text += ny_bokstav
        else: 
            krypterad_text += bokstav

    return krypterad_text


text = input("Mata in text som ska chiffreras: ")
krypterad = caesarchiffer(text)
print(f"Krypterad text: {krypterad}")

