def main():
    choice = input("Type 'encode' to encrypt, type 'decode' to decrypt : ")
    msg = input("Type your message : ").lower()
    s = int(input("Enter shift value : "))

    z = ''
    for i in msg:
        if i == " ":
            z += i
        if choice == "decode":
            z += chr(ord(i) - 3)
        else:
            z += chr(ord(i) + 3)
    print(f"your {choice}d message is {z}.")

    ch = input("Type 'Yes' if you want to go again; Otherwise type 'No' :").lower()
    if ch == "yes":
        main()
    else:
        return


main()
