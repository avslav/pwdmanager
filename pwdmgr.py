# run pip install bcrypt

import secrets
import string
import hashlib
import bcrypt


def menu():
    
    print("\nHello! Welcome to avslav's password manager!\n\nPress 1 to generate a safe password\nPress 2 to save a password\nPress 0 to exit")

    choice = input()

    if choice == "0":
        return print("\nThanks for using avslav's password manager!\nSee you soon!")
    
    elif choice == "1":
        generate()
    
    elif choice == "2":
        addpwd()
    
    else:
        print("Invalid choice! Please type 1 or 0 next time.\n\n")
        menu()

def generate():
    print("\nPlease choose the length of your password in characters (A length of at least 8 is recommended)...")
    length = input()
    
    finalLength = int(length)
    symbols = "!@#$%^&*()[]/?.,"
    chars = string.ascii_letters + string.digits + symbols
    password = ''.join(secrets.choice(chars) for i in range(finalLength))

    print(f"\nYour password: {password}")

def addpwd():
    # Getting password details
    print("\nLet's start! First of all, what platform are you going to use this password for? (e.g. Facebook)\n")
    global platform
    platform = input()
    print(f"\nOk. You will use this password for your {platform} account.\nNow, what email will you use for this account?\n")
    global email
    email = input()
    print(f"Ok. The email you chose will be {email}. \nFinally, what is the password you are going to use?\n")
    password = input()

    # Hint to remember the password without decrypting
    print("\nNow, since the password will be encrypted, please type a hint that will help you remember the password without needing to decrypt it\n")
    global hint
    hint = input()

    # Choosing where to dump the password
    print("\nBefore we move on to hashing, what is the filename that you would like to use to save this password? (e.g. Type \"secretfile\" if you want to save this password in a file named \"secretfile.txt\"\n")
    global filename
    filename = input()
    
    # Choosing any file extension
    print("\nNow, please choose a file extension (without typing the period). You can make up an extension, or use an existing text extension such as .txt")
    global fext 
    fext = input()
    
    # Check if they included a period in their file extension
    if "." in fext:
        print("Please don't include a period in your file extension!\n\nTry again...")
        addpwd()
    else:
        pass

    # Creating a legit file to dump passwords
    global fullfname
    fullfname = filename + "." + fext
    fullfname.strip()
    
    # Hash the password before dumping
    hashPwd(password)
    
def hashPwd(pwd):
    
    # Hash algorithm menu
    print("\nChoose the hashing algorithm for your password:\n1. SHA-512\n2. SHA-256\n3. SHA-224\n4. Bcrypt (recommended)\n5. CombinedHash (experimental)\n\n")
    hashMeth = input()
    
    # SHA-512
    if hashMeth == "1":
        toSha512 = hashlib.sha512(str(pwd).encode("utf-8") ).hexdigest()
        print(toSha512)
        print("\nOk. Your password has been encrypted to SHA-512 and saved.")

        with open(fullfname, "a") as f:
            f.write(f"Password for: {platform}\nEmail: {email}\nPassword Hint: {hint}\nPassword: {toSha512}\n\n")
        continueOrExit()

    # SHA-256
    elif hashMeth == "2":
        toSha256 = hashlib.sha256(str(pwd).encode("utf-8")).hexdigest()
        print(toSha256)
        print("\nOk. Your password has been encrypted to SHA-256 and saved.")

        with open(fullfname, "a") as f:
             f.write(f"Password for: {platform}\nEmail: {email}\nPassword Hint: {hint}\nPassword: {toSha256}\n\n")
        continueOrExit()

    # SHA-224
    elif hashMeth == "3":
        toSha224 = hashlib.sha224(str(pwd).encode("utf-8")).hexdigest()
        print(toSha224)
        print("\nOk. Your password has been encrypted to SHA-224 format and saved.")

        with open(fullfname, "a") as f:
             f.write(f"Password for: {platform}\nEmail: {email}\nPassword Hint: {hint}\nPassword: {toSha224}\n\n")

        continueOrExit()
    
    # Bcrypt with salt
    elif hashMeth == "4":
        
        salt = bcrypt.gensalt()
        toBcrypt = bcrypt.hashpw(pwd.encode('utf8'), salt)
        
        print(toBcrypt)
        print("\nOk. Your password has been encrypted to \"bcrypt\" format and saved.")

        with open(fullfname, "a") as f:
             f.write(f"Password for: {platform}\nEmail: {email}\nPassword Hint: {hint}\nPassword: {toBcrypt}\n\n")
        
        continueOrExit()
    
    # Random hashing algorithm I made up which hashes a string 4 times
    elif hashMeth == "5":
        
        salt = bcrypt.gensalt()
        toBcrypt = bcrypt.hashpw(pwd.encode('utf8'), salt)
        toSha224 = hashlib.sha224(str(toBcrypt).encode("utf-8")).hexdigest()
        toSha512 = hashlib.sha512(str(toSha224).encode("utf-8") ).hexdigest()
        finalHash = hashlib.sha256(str(toSha512).encode("utf-8")).hexdigest()
        
        print("\nOk. Your password has been encrypted to \"Combined Hash\" format and saved.\n\n**Warning! This type of Hash is hard to decrypt!**\n\n")

        with open(fullfname, "a") as f:
             f.write(f"Password for: {platform}\nEmail: {email}\nPassword Hint: {hint}\nPassword: {finalHash}\n\n")
        continueOrExit()
    else:
        print("\nInvaid choice! Please try again.")
        addpwd()

def continueOrExit():

    # Continue saving passwords or exit

    print("Would you like to save another password or exit?\n\nPress 0 to exit\nPress any character to save another password\n\n")
    choice = input()

    if choice == "0":
        print("Thanks for using my password manager!\nSee you soon!\n\n")
    
    else:
        addpwd()

menu()