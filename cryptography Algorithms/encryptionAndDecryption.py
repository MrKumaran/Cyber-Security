# Encrypts and decrypts a string into cipher contains symbols and alphabets

def encrypt(shiftValue, stringToEncrypt):
    encryptedText = ''
    for char in stringToEncrypt:
        key = ord(char) + shiftValue
        if key > 126:
            key %= 126
        if key < 32:
            key += 32
        encryptedText += chr(key)
    return encryptedText


def decrypt(shiftValue, stringToDecrypt):
    decryptedText = ''
    for char in stringToDecrypt:
        key = ord(char) - shiftValue
        if key < 32:
            rem = 32 - key
            key = 126 - rem
        decryptedText += chr(key)
    return decryptedText


if __name__ == "__main__":
    print("Key from 0 - 40")
    text = input('Enter the text to encrypt: ')
    key = int(input('Enter the key: '))
    cipher = encrypt(key, text)
    print(f'Cipher: {cipher}')
    decipher = decrypt(key, cipher)
    print(f'Decipher: {decipher}')


