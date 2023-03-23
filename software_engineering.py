# This program constitutes a simplified password encoder/decoder.
# Original developer: Conan Hooker Humphries

def encode(Password):
    """
    Function to encode an 8-digit password in string format containing only integers.

    * Parameter:
        Password
    * Return:
        EncodedPassword
    """
    EncodedPassword = ""
    for Digit in Password:
        NewDigit = int(Digit) + 3
        if NewDigit > 9:
            NewDigit -= 10
        EncodedPassword += str(NewDigit)
    return EncodedPassword


# Ian added decode function
def decode(Password):
    """
    Function to decode an 8-digit password in string format containing only integers.

    * Parameter:
        Password
    * Return:
        DecodedPassword
    """
    DecodedPassword = ""
    for Digit in Password:
        NewDigit = int(Digit) - 3
        if NewDigit < 0:
            NewDigit += 10
        DecodedPassword += str(NewDigit)
    return DecodedPassword


def main():

    while True:

        # The menu is displayed.
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit\n")

        Selection = int(input("Please enter an option: "))

        while Selection != 3:

            if Selection == 1:  # This selection encodes the password.
                Password = input("Please enter your password to encode: ")
                EncodedPassword = encode(Password)
                print("Your password has been encoded and stored!\n")
                break
            elif Selection == 2:  # This selection decodes the password.
                DecodedPassword = decode(EncodedPassword)
                print(f"The encoded password is {EncodedPassword}, and the original password is {DecodedPassword}.\n")
                break
        else:
            break


if __name__ == "__main__":
    main()
