def main():
        try:
            fuel=input("Enter Fraction: ")
            # get int x and y
            x=fuel[ :fuel.find("/")]
            y=fuel[fuel.find("/")+1: ]
            # from string to int
            X=int(x)
            Y=int(y)

            if X>Y or X<0 or Y<0:
                raise ValueError
            if Y==0:
                raise ZeroDivisionError
            
            fuel_per=int( (X/Y)*100)

            if fuel_per >=99 and fuel_per <=100:
                print("F")
            elif fuel_per<=1 and fuel_per >=0:
                print("E")
            else:
                print(fuel_per,"%")

        except ValueError:
            main()
        except ZeroDivisionError:
            main()
        except TypeError:
            main()

main() 