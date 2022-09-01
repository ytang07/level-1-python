# affine cipher using ascii values
def encode():
    word = input("Give a word to encode in an affine cipher: ")
    print("Your affine cipher encoded word: ")
    encoded = " ".join([str(ord(x)) for x in word])
    print(encoded)
    return encoded

# encode()

def decode():
    encoded_list = input("What are is the encoded affine cipher? ")
    decoded = "".join(chr(int(x)) for x in encoded_list.split(" "))
    print(decoded)
    return decoded

# decode()

# take the distance from the letter 'a' as the intercept
# allow an entry, m, for the scaling
def custom_encode(word, m = 1, b = 0, base = 'a', return_string = False):
    encoded = []
    for char in word:
        x = ord(char) - ord(base)
        y = m * x + b
        encoded.append(y)
    if return_string:
        return ' '.join(encoded)
    else:
        return encoded

# x = (y - b)/m
def custom_decode(encoded, m = 1, b = 0, base = 'a', return_string = True):
    decoded = []
    for y in encoded:
        x = (y-b)//m
        x = chr(x + ord(base))
        decoded.append(x)
    if return_string:
        return ''.join(decoded)
    else:
        return decoded

# basic 
cipher = custom_encode("ego")
print(f"Encoded affine cipher is: {cipher}")
word = custom_decode(cipher)
print(f"Custom decoded affine cipher word is: {word}")

# customized
cipher = custom_encode("ego", m=2, b=3)
print(f"Encoded affine cipher is: {cipher}")
word = custom_decode(cipher, m=2, b=3)
print(f"Custom decoded affine cipher word is: {word}")

# incorrect
cipher = custom_encode("ego", m=2, b=3)
print(f"Encoded affine cipher is: {cipher}")
word = custom_decode(cipher, m=3, b=1)
print(f"Custom decoded affine cipher word is: {word}")