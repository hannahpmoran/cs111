# input cipher


def decipher(plaintext):
    
    deciphertext = ""

    YesOrNo = input("Would you like to decipher this text?(Please type Yes or No.): ")

    if YesOrNo == str("Yes"):
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
    else:
        print("Ok, bye.")
    

#user says "yes" if the cipher is readble

#user says no if unreadable and goes thru it again