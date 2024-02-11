import data
import random

def print_name():
    print("This program is titled The EnCoder")
    # TODO edit description
    print("Description: implements part A\n")

def get_shift_num():
    shift_num = int(input("What is the shift number? "))
    while shift_num < 0 or shift_num > 25:
        print("You did not enter a valid shift number.")
        print("Please enter a number between 0 and 25 inclusive.")
        shift_num = int(input("Enter your desired shift number! "))
    
    return shift_num

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
    
def encode_message(message, shift_num):
    alph_to_index_dict, index_to_alph_dict = data.alphabet_dictionaries()
    encoded_message = ""

    if shift_num == 0:
        return message
    
    for i in range(len(message)):
        char = message[i]
        if char == " ":
            encoded_message += char
        else:
            index = alph_to_index_dict[char]
            index += shift_num
            if (index > 25):
                index = index - 26
            encoded_char = index_to_alph_dict[index]
            encoded_message += encoded_char
    
    return encoded_message

def find_fake(list_of_msgs):
    print(list_of_msgs)
    length = len(list_of_msgs)
    chance = round(100 / length)
    weights = [chance]*length
    chosen_msg = random.choices(list_of_msgs, weights=weights, k=1)
        
    print(f"There is a {chance}% chance {chosen_msg} is a fake message") 