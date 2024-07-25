alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
s_i=direction

def encrypt(plainText, number):
    pt=""
    for i in plainText:
        n=alphabet.index(i)
        r=n+number
        pt+=(alphabet[r])
    print(pt)

if s_i=="encode":
    encrypt(plainText=text, number=shift)
else:
    print("Try again next time!!")
