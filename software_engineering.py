# This program constitutes a simplified password encoder/decoder.
# Original developer: Conan Hooker Humphries

def encode(Password):
    EncodedPassword = ""
    for Digit in password:
        NewDigit = int(Digit) + 3
        if NewDigit > 9:
            NewDigit -= 10
        EncodedPassword += str(NewDigit)
    return EncodedPassword

#Ian added decode function
def decode(password):
    DecodedPassword = ""
    for Digit in password:
        NewDigit = int(Digit) - 3
        if NewDigit < 0:
            NewDigit += 10
        DecodedPassword += str(NewDigit)
    return DecodedPassword


def main():

    while True:

        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit\n")

        Selection = int(input("Please enter an option: "))

        while Selection != 3:

            if Selection == 1:
                Password = input("Please enter your password to encode: ")
                EncodedPassword = encode(Password)
                print("Your password has been encoded and stored!\n")
                break
            elif Selection == 2:
                DecodedPassword = decode(EncodedPassword)
                print(f"The encoded password is {EncodedPassword}, and the original password is {DecodedPassword}.\n")
                break
        else:
            break


if __name__ == "__main__":
    main()
