# shift the letters in the text by s places

def encrypt(text, s):
    result = ""
    for char in text:
        if char.isupper():
            key = ord(char) + s - 65
            key = key % 26
            key = key + 65
            result += chr(key)
        else:
            key = ord(char) + s - 97
            key = key % 26
            key = key + 97
            result += chr(key)
    return result


def decrypt(text, s):
    result = ""
    for char in text:
        if char.isupper():
            key = ord(char) - s - 65
            key = key % 26
            key = key + 65
            result += chr(key)
        else:
            key = ord(char) - s - 97
            key = key % 26
            key = key + 97
            result += chr(key)
    return result

if __name__ == "__main__":
    text = input("Text: ")
    s = int(input("Shift: "))
    cipher = encrypt(text, s)
    decipher = decrypt(cipher, s)
    print("Cipher: " + cipher)
    print("Decipher: " + decipher)