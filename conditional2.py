
def main():
    x=input("File name: ")
    extension=x[x.find(".")+1: ]
    file(extension)

def file (f):
    match f:
        case "gif":
            print("image/gif")

        case "jpg":
            print("image/gif")

        case "jpeg":
            print("image/gif")

        case "pdf":
            print("pdf file")

        case "txt":
            print("text file ")
        
        case _:
            print("application/octet-stream")# default case
            
main()