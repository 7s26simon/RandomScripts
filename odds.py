import click

def odds ():
    a = ("What were the fractional odds you bet on? (E.g if 5/4, type '5' enter, '4' enter)")
    print(a)
    y = int(input())
    z = int(input())
    print ("What did you bet? E.g for £20, type '20' followed by enter")
    yourBet = int(input())
    winnings = (z * y) + z
    if click.confirm(("\nSo the fractional odds were: %d/%d? and you bet £%d" %(y,z,yourBet)), default=True):
        print("\n")
        print ("\nYour winnings would be:", "£"+str(winnings)+"\n")
        print("Good luck, and thank you for using this script!")
    else:
        print("\nRestarting script...")
        odds()

odds()
