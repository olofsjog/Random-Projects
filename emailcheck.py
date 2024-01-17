#Verified Domains
validDomains = ["gmail.com", "yahoo.com", "outlook.com"]

#Loop if Invalid
while True:

    #Inputting Email and Name
    email = input("Email: ")
    name = input("Name: ")

    #Extract the Email Domain
    domain = email.split("@")

    if len(domain) != 2:
        print(domain)
        print("\nInvalid Email\n\n\n\n")

    #Checking if Domain is in ValidDomains
    elif domain[1] in validDomains:

        #Checking if Name is Valid
        if name.isalpha():
            print("\nCongratulations! The streams are on their way.")
            quit()

        #When Name is Invalid
        else:
            print("\nInvalid Name\n\n\n\n")

    #When Domain is Invalid
    else:
        print("\nInvalid Email\n\n\n\n")