# 1. Input the cipher into the function

# 2. Then, run it through the decipher (basically the same as the cipher in caesar.py but only moving one forward.)
def decipher(plaintext):
    
    deciphertext = ""

    for ch in plaintext:
        if ord(ch) >= 65 and ord(ch) <= 90:
            ch = chr(ord(ch)+1)
            if ord(ch) < 90:
                deciphertext += ch
            if ord(ch) > 90:
                ch = chr(ord(ch)-26)
            deciphertext += ch
        if ord(ch) >= 97 and ord(ch) <= 122:
            ch = chr(ord(ch)+1)
            if ord(ch) < 122:
                deciphertext += ch
            if ord(ch) > 122:
                ch = chr(ord(ch)-26)
                deciphertext += ch
# 3. It asks the user if the cipher was properly decoded, promting a Yes or No string input.
    print(deciphertext)
    YesOrNo = ("Would you like to decipher again?(Please type Yes or No.): ")
# 4. A while loop is used to either re-run the decipher again, or complete the decipher.
    while YesOrNo == "Yes":
        decipher(deciphertext)
    else:
        print("Ok!")
# 5. The idea behind this decipher is to slowly reach a readable string of words again in a managable code.