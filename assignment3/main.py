# Veer Singh, COMP 1701 FALL 2025
#

import math

def main()->None:
    quit = False
    while(not(quit)):
        userInput = input("Enter Command: ")
        command = userInput.split(" ")[0]
        arguments = userInput.splut(" ")[1:]


        match command:
            case "exit":
                quit = True
                break

            case "read":
                #expected arguements: filename
                pass

            case "save":
                #expected arguements: filename
                pass

            case "print":
                pass

            case "project":
                #expected arguments: column names
                





if(__name__ == "__main__"):
    main()