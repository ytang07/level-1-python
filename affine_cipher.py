# affine cipher using ascii values
def encode():
    word = input("Give a word to encode in an affine cipher: ")
    print("Your affine cipher encoded word: ")
    encoded = " ".join([str(ord(x)) for x in word])
    print(encoded)
    return encoded

encode()

def decode():
    encoded_list = input("What are is the encoded affine cipher? ")
    decoded = "".join(chr(int(x)) for x in encoded_list.split(" "))
    print(decoded)
    return decoded

decode()
