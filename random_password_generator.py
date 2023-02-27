import sys
import string
import secrets


def random_password(length):
    alp = string.ascii_letters + string.digits
    password = ''.join(secrets.choice(alp) for i in range(length))
    return password


def main():
    while True:
        intake = input("Do you want a password?(Y/N)")
        try:
            if intake == "Y":
                length = int(input("Length?"))
                output = random_password(length)
                print(
                    f"Your password is {output}.\n You can also find it in the output file.")
                return output
            elif intake == "N":
                print("Thank you for using our program!")
                break
            else:
                print("Please Try again!")
                continue
            
        except ValueError as err:
            return f"Error Fetching:{err} Try again!"


output = main()
with open("output.txt", "w+") as f:
    f.write(output)
