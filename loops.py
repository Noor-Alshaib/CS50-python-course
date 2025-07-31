
#problem set 2: loops, drink machine, sells drinks for 50
def main():
    amount_due=50
    while amount_due!=0 and amount_due > 0:
        print("Amount due: ", amount_due)
        x=int(input("Insert coin: "))
        # only accept 25 or 10 or 5 
        if x==25 or x==10 or x==5:
            amount_due=amount_due-x
    #end loop
    
    print("Change owed: ", abs(amount_due))       

main()
