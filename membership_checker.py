print("What level of membership are you? 1,2 or 3? : ")
membership = int(input("Enter you membership level with no spaces or capitals. : "))
if membership == 1:
    print(f"You get a 5% discount. ")
elif membership == 2:
    print(f"You get a 10% discount. ")
elif membership == 3:
    print(f"You get a 15% discount. ")