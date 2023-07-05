print("Hi welcome to Domino's.")
print("I am Domio, your asssistant")
cart=0
pizza=int(input("""HERE IS OUR MENU:
press (1) for Tomato pizza.
press (2) for Veg loaded pizza.
press (3) for Farm fresh pizza.
press (4) for Cheese pizza:: """))
if(pizza==1):
    size=int(input(f"""Thanks for choosing Tomato pizza.

                        KINDLY SELECT THE REQUIRED SIZE YOU WANT TO ORDER:
                        press (1) for small size(100).
                        press (2) for medium size(150).
                        press (3) for large size(220):: """))
    if(size==1):
           cart=cart+100
    elif(size==2):
           cart=cart+150
    elif(size==3):
           cart=cart+220
elif(pizza==2):
    size=int(input(f"""Thanks for choosing Veg loaded pizza.

                        KINDLY SELECT THE REQUIRED SIZE YOU WANT TO ORDER:
                        press (1) for small size(150).
                        press (2) for medium size(200).
                        press (3) for large size(300)::"""))
    if(size==1):
           cart=cart+150
    elif(size==2):
           cart=cart+200
    elif(size==3):
           cart=cart+300
elif(pizza==3):
    size=int(input(f"""Thanks for choosing Farm freash.

                        KINDLY SELECT THE REQUIRED SIZE YOU WANT TO ORDER:
                        press (1) for small size(140).
                        press (2) for medium size(190).
                        press (3) for large size(290)."""))
    if(size==1):
           cart=cart+140
    elif(size==2):
           cart=cart+190
    elif(size==3):
           cart=cart+290
elif(pizza==4):
    size=int(input(f"""Thanks for choosing cheese pizza.

                        KINDLY SELECT THE REQUIRED SIZE YOU WANT TO ORDER:
                        press (1) for small size(170).
                        press (2) for medium size(210).
                        press (3) for large size(310)."""))
    if(size==1):
           cart=cart+170
    elif(size==2):
           cart=cart+210
    elif(size==3):
           cart=cart+310
print("thanks for choosing the pizza")
dip=int(input("if you need extra cheese then select (1) or press (2) for no extra cheese(cost:+50)"))
if(dip==1):
    cart=cart+50
elif(dip==2):
    cart=cart+0
print(f"your cart total is Rs.{cart}.")
if(pizza==1):
    print("pizza - tomato pizza")
elif(pizza==2):
    print("pizza - veg loaded pizza")
elif(pizza==3):
    print("pizza - farm fresh pizza")
elif(pizza==4):
    print("pizza - cheese pizza")
if(dip==1):
    print("your extra cheese is loaded in your pizza for 50 ruppes.")
elif(dip==1):
    print("No extra cheese is added")
    

