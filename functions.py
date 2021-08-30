def sayHello(name, verbo):
    print("Waddup "+ name +", I heard you tryna " + verbo + ".")
    print("\n")

sayHello("Chris", "fly")
sayHello("Sadie", "vibe")
sayHello("Ock", "ride")

def sayHello():
    print("hello")

def top_3(num1, num2, num3):
    gone = num1 + num2 + num3 + 10 * 2
    if gone > 20:
        print("Your lucky number is %d." % gone)
        print("\n")
    else:
        print("Your unlucky number is %d. But without darkness no one would see the light. Enjoy your unlucky day." % gone)
   

top_3(2,6,7)
top_3(1,1,2)

