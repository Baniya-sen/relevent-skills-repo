# Caesar Cipher is a substitution cipher where each letter in the plaintext is shifted a fixed number of positions
# down the alphabet. It provides basic encryption but is easily breakable. Despite  its simplicity,
# it's historically significant and introduces the concept of encryption through shifting.


def main():
    print(logo)
    print()

    """Program runs until user types "exit" when asked"""
    while True:
        print()

        options = input("Enter \"Encode\" to Encrypt, \"Decode\" to Decrypt: ").lower()
        if "encode" != options != "decode":
            print("Invalid choice fool!")
            break

        plain_text = input("Enter Message: ").lower()

        while True:
            try:
                key = int(input("Enter Shift Key: "))
            except ValueError:
                continue
            break

        print(cipher(options, plain_text, key))

        if input("Input any key to continue, \"Exit\" to exit ").lower() == "exit":
            print("Ram Ram bhai sareya ne!!")
            break


def cipher(options, message, key):
    cipher_text = ""
    alpha_len = len(alpha)

    """Cipher text key is shifted forward with key value in encoding, and shifted backwards when decoding"""
    if options == "decode":
        key = -key

    for char in message:
        if char in alpha:
            """We take index of char of message from alpha list, add shift key to index,
            use % so it won't go out of bounds"""
            cipher_text += alpha[(alpha.index(char) + key) % alpha_len]
        else:
            cipher_text += char

    return cipher_text


alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
         'v', 'w', 'x', 'y', 'z']

logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""

if __name__ == "__main__":
    main()
