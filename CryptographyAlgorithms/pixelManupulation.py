# manupilate the pixels of an image to encrypt or decrypt it using XOR operation

try:
    path = input("Enter the path of the image to encrypt or decrypt: ")
    key = int(input("Enter the key to encrypt or decrypt: "))
    file = open(path, "rb")
    image = file.read()
    file.close()
    image = bytearray(image)
    for index, value in enumerate(image):
        image[index] = value ^ key
    file = open(path, "wb")
    file.write(image)
    file.close()

except Exception:
    print("Have fun resolving errors!")
    print(Exception.__name__)