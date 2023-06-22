print
("""###############################
ENTER YOUR CREDIT CARD NUMBER
EBUBEKİR TİLBAÇ
###############################
""")

#get credit number from the user
cardno = input("Enter your credit card number:")

# find your credit card type (Visa, MasterCard, or Amex)
# MasterCard must have the first digit as 5
# Visa must have the first digit as 4
# Amex must have the first two digits as 34 or 37

if len(cardno)==16:
    if cardno[0]=="4":
        card_type="Visa"
    elif cardno[0]=="5":
        card_type="MasterCard"
    else:
        print("INVALID")
elif len(cardno)==15 and cardno[0]=="3"and(cardno[1]=="4"or cardno[1]=="7"):
    card_type="Amex"
else:
    print("INVALID")

#LUHN ALGORİTHM
def luhn_check(cardno):
    #Convert the card number to a list of digits
    digits = [int(x) for x in cardno]

    #Double every second digit, starting from the rightmost digit
    for i in range(len(digits) - 2, -1, -2):
        digits[i] *= 2
        if digits[i] > 9:
            digits[i] -= 9

    #Sum all the digits
    total = sum(digits)

    #Check if the total is divisible by 10
    if total % 10 == 0:
        return True
    else:
        return False

# Get credit card number from the user
cardno = input("Enter your credit card number: ")

# Remove any whitespace characters from the input
cardno = cardno.replace(" ", "")

# Check if the card number is valid using the Luhn algorithm
if luhn_check(cardno):
    # Determine the card type
    if len(cardno) == 16:
        if cardno[0] == "4":
            card_type = "Visa"
        elif cardno[0] == "5":
            card_type = "MasterCard"
        else:
            card_type = "INVALID"
    elif len(cardno) == 15 and cardno[0] == "3" and (cardno[1] == "4" or cardno[1] == "7"):
        card_type = "Amex"
    else:
        card_type = "INVALID"

    print("Valid credit card number.")
    print("Card type: {}".format(card_type))
else:
    print("Invalid credit card number.")