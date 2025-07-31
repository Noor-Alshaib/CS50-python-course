# proplem set 0, playback speed

def playback(str):
    string=str.split()
    for i in string:
        if i==string[len(string)-1]:
            print(i)
            break
        
        print(i+"...", end="")
           
def main():
    str=input("enter string: ")
    playback(str)

main()
