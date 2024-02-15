import data
import random

def print_name(part):
    if part == "A":
        print("This program is titled The EnCoder")
        # TODO edit description
        print("Description: implements part A\n")
    if part == "B":
        print("This program is titled The EnCoder")
        # TODO edit description
        print("Description: implements part B\n")
    if part == "C":
        print("This program is titled The EnCoder")
        # TODO edit description
        print("Description: implements part C\n")
    if part == "D":
        print("This program is titled The EnCoder")
        # TODO edit description
        print("Description: implements part D\n")
        
def get_shift_num():
    shift_num = int(input("What is the shift number? "))
    while shift_num < 0 or shift_num > 25:
        print("You did not enter a valid shift number.")
        print("Please enter a number between 0 and 25 inclusive.")
        shift_num = int(input("Enter your desired shift number! "))
    
    return shift_num

def validate_shift_num(shift_num, close_program):
    if shift_num < 0:
        print("Invalid shift number, integer must be >= 0.")
        close_program = True
        return close_program

def get_message():
    valid_message = False
    while not valid_message:
        message = input("Enter the message you want to encode: ").lower()
        words = message.split(' ')
        i = 0
        valid_word = True
        while i < len(words) and valid_word:
            if words[i] == "":
                i += 1
            elif words[i].isalpha():
                i += 1
            else:
                print("Please enter an alphabetical message.") 
                valid_word = False
        if valid_word:
            valid_message = True
    return message
    
def encode_message (message, shift_num):
    
    alph_to_index_dict, index_to_alph_dict = data.alphabet_dictionaries()
    encoded_message = ""

    if shift_num == 0 or shift_num == 26:
        return message
    
    for i in range(len(message)):
        char = message[i]
        if char == " ":
            encoded_message += char
        else:
            index = alph_to_index_dict [char.lower()]
            if (shift_num > 25):
                # 26 resets to original index
                # remainder becomes the new shift number
                shift_num = shift_num % 26 
            index += shift_num
            if (index > 25):
                # 26 resets to original index
                # remainder becomes the new encoded index
                index = index % 26
            encoded_char = index_to_alph_dict[index]
            encoded_message += encoded_char
    
    return encoded_message

def encode_file(message, shift_num):
    alph_to_index_dict, index_to_alph_dict = data.alphabet_dictionaries()
    encoded_message = ""

    if shift_num == "0": 
        return message
    
    for i in range(len(message)):
        char = message[i]
        if char == " ":
            encoded_message += char
        else:
            index = alph_to_index_dict[char.lower()]
            index += shift_num
            if (index > 25):
                index = index - 26
            encoded_char = index_to_alph_dict[index]
            encoded_message += encoded_char
    
    return encoded_message

def encode_part_d(message, shift_num):
    alph_to_index_dict, index_to_alph_dict = data.alphabet_dictionaries()
    encoded_message = ""

    if shift_num == "0": #TODO is 'string' correct? 
        return message
    
    for i in range(len(message)):
        char = message[i]
        if char == " ":
            encoded_message += char
        else:
            index = alph_to_index_dict[char.lower()]
            index += shift_num
            if (index > 25):
                index = index - 26
            encoded_char = index_to_alph_dict[index]
            encoded_message += encoded_char

def find_fake(list_of_msgs, total_msgs):
    print("\nRemaining Messages Not Encoded:")
    for msgs in list_of_msgs:
        print(" ".join(msgs))

    length = total_msgs
    chance = round((100 / length), 1)
    weights = [chance]*len(list_of_msgs)
    chosen_msgs = random.choices(list_of_msgs, weights=weights, k=1)
    
    for msgs in chosen_msgs:
        chosen_msg = " ".join(msgs)
        print(f"There is a {chance}% chance {chosen_msg} is a fake message")

def pop_from_stack(list_of_msgs, shift_numbers, isFirst=False):
    removed_msgs = list_of_msgs[-1]
    list_of_msgs.remove(list_of_msgs[-1])
    removed_shift_num = int(shift_numbers[-1])
    shift_numbers.remove(shift_numbers[-1])
    encoded_msgs = []

    for message in removed_msgs:
        encoded_msg = encode_message(message, removed_shift_num)
        encoded_msgs.append(encoded_msg)
    
    if isFirst:
        print("Encoded messages:")

    print_msgs_in_list(encoded_msgs)

def print_msgs_in_list(list_of_msgs):
    for message in list_of_msgs:
        print (message)