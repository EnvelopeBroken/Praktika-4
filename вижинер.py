def vigenere_cipher(text, key):
    ciphered_text = ''
    key = key * (len(text) // len(key)) + key[:len(text) % len(key)]
    
    for i in range(len(text)):
        if text[i].isalpha() and text[i].islower():
            shift = ord(key[i]) - ord('а')
            new_char = chr((ord(text[i]) - ord('а') + shift) % 32 + ord('а'))
            ciphered_text += new_char
        elif text[i].isalpha() and text[i].isupper():
            shift = ord(key[i]) - ord('А')
            new_char = chr((ord(text[i]) - ord('А') + shift) % 32 + ord('А'))
            ciphered_text += new_char
        else:
            ciphered_text += text[i]
    
    return ciphered_text

text = input("Введите текст, который нужно зашифровать: ")
key = input("Введите ключ: ")

ciphered_text = vigenere_cipher(text, key)
print("Зашифрованный текст:", ciphered_text)
