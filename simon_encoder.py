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
            pass
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
    common.print_name()
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

            
main()
