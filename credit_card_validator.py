# Credit Card Validator - Takes in a credit card number from a
# common credit card vendor (Visa, MasterCard, American Express,
#  Discoverer) and validates it to make sure that it is a valid
# number (look into how credit cards use a checksum).

def check_creditordebit_card():
    cardnum = input("enter your card number :\n")
    oddsum = 0
    evensum = 0
    sumc = 0
    evenmul1 = 0
    evenmul2 = 0
    if(len(cardnum) == 16):
        for i in range(0, len(cardnum)):
            if(i % 2 != 0):
                oddsum = oddsum+int(cardnum[i])
            elif(i % 2 == 0):
                a = str(int(cardnum[i])*2)
                if(len(a) == 1):
                    evenmul1 = evenmul1+(int(a))
                else:
                    b = int(a[0])+int(a[1])
                    evenmul2 = evenmul2+b
                evensum = evenmul1+evenmul2
        sumc = oddsum+evensum
        if(sumc % 10 == 0):
            print(("valid card"))
        else:
            print("not a valid card")
    else:
        print(("invaild Card"))


check_creditordebit_card()
