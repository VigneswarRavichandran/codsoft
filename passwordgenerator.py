import random
import string
try:
    #getting input from the user
    length=int(input("Enter the length of the password to be generated:"))
    #creaing a function
    def generate_password(length):
        characters=string.ascii_letters+string.digits+string.punctuation
        password=''.join(random.choice(characters) for i in range(length))
        return password
    #calling the function
    obtained_password=generate_password(length)
    #displays the password
    print("Generated Password:"+obtained_password)
except:
    print("Invalid input")
