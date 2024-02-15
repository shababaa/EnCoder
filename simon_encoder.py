# Developer: Simon Akhter
# Date: 2021-10-15
# The EnCoder
# Description: This program covers part D. This program is an encoder that takes 
# messages and shifts the letters by a certain number of places through file 
# readings. After, it prints the encoded message. The program also has the 
# ability to detect fake messages and print the number of fake messages in the 
# file.

print ("This program is titled The EnCoder!" + "\n") 
print ("This program will use data from the file, asgt_messages.txt")
print ("The each line in the file will contain an instruction or message line.")
print ("Message lines will contain a shift number to encode the message")
print ("and the message to be encoded.")
print ("For instruction lines, 'x' or 'X' will exit the program.")
print ("And 'e' or 'E' will encode the last messages in the list after")
print ("removing it.\nHave fun!\n")

import common

# Main function

def main():
    shift_numbers = []
    list_of_msgs = []
    list_of_elements = []
    total_msgs = 0
    isFirst = True
    close_program = False

    file = open("asgt_messages.txt", "r")
    lines = file.readlines()

    # Check if the first line starts with 'X' or 'x'
    # If so, close the program
    first_line = lines[0].strip()
    if first_line.lower().startswith('x'):
        file.close()
        close_program = True
        print("\nNo messages to encode.\nThe program is now closing.")

    for line in lines:
        if not close_program:
            list_of_elements = line.split()
            # split words into a list
            instruction = list_of_elements[0]
            
            # message line
            if list_of_elements[0].isnumeric():
                valid = True
                for word in list_of_elements[1:]:
                    if not word.isalpha():
                        print(f"The word '{word}' is not a valid message.")
                        print("This message will be skipped.\n")
                        valid = False
                if valid:
                    total_msgs += 1
                    shift_numbers.append(list_of_elements[0])
                    list_of_msgs.append(list_of_elements[1:])
            # instruction line
            elif instruction.isalpha() and not instruction.isnumeric():
                if instruction.lower() == 'e':
                    if len(list_of_msgs) == 0:
                        print("Encode instruction received but there are no messages left to encode")
                    else:
                        if isFirst:
                            print("Message:", " ".join(list_of_msgs[-1]))
                            common.pop_from_stack(list_of_msgs, shift_numbers, isFirst)
                            isFirst = True
                        else:
                            common.pop_from_stack(list_of_msgs, shift_numbers)
                elif instruction.lower() == 'x':
                    file.close()
                    common.find_fake(list_of_msgs, total_msgs)
                    return False
            else:
                print("Invalid line in input file")

main()
input()