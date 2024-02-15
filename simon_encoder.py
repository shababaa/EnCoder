# Developer: Simon Akhter
# The EnCoder

import common

def main():
    valid_part = False
    while not valid_part:
        part = input("What part do you want to run? [A, B, C, D]: ").lower()
        if part == 'a':
            valid_part = True
            part_a_main()
        elif part == 'b':
            valid_part = True
            part_b_main()
        elif part == 'c':
            pass
            valid_part = True
            part_c_main()
        elif part == 'd':
            pass
            valid_part = True
            part_d_main()
        else:
            print("Enter a valid letter [A, B, C, D] please.")


def part_a_main():
    list_of_msgs = []
    common.print_name("A")
    shift_num = common.get_shift_num()
    while True:
        message = common.get_message()
        if message == 'x':
            common.find_fake(list_of_msgs)
            return False
        else:
            print("Message: ", message)
            
            encoded_message = common.encode_message(message, shift_num)
            list_of_msgs.append(encoded_message)
            print("Encoded Message: ", encoded_message)

def part_b_main():
    list_of_msgs = []
    common.print_name("B")

    file = open("asgt_messages.txt", "r")
    lines = file.readlines()
    shift_num = int(lines[0].strip("\n"))
    initial_close_program = False
    close_program = common.validate_shift_num(shift_num, initial_close_program)

    if close_program == True:
        return False
    #TODO special characters case in file
    #TODO validation messages?
    for line in lines[1:]:
        message = line.strip()
        if message.isalpha():
            encoded_message = ""
            encoded_message = common.encode_file(message, shift_num)
            list_of_msgs.append(encoded_message)
            if message.lower() == "x":
                list_of_msgs.remove(list_of_msgs[-1])
                common.find_fake(list_of_msgs)
                return False
            print ("Message:", message)
            print ("Encoded message:", encoded_message)
        else:
            print(f"Invalid character type: {message}. Moving to next message.")


    
    file.close()

    

def part_c_main():
    list_of_msgs = []
    common.print_name("C")

def part_d_main():
    list_of_msgs = []
    common.print_name("D") 

            
main()
