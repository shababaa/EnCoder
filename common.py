import data
import random

def print_intro ():
    print ("This program is titled The EnCoder!\n")
    print ("This program implements Part D of the assignment") 
    print ("This program will use data from the file, asgt_messages.txt")
    print ("The each line in the file will contain an instruction or message line")
    print ("Message lines will contain a shift number to encode the message", end=" ")
    print ("and the message to be encoded")
    print ("For instruction lines, 'x' or 'X' will exit the program.")
    print ("And 'e' or 'E' will encode the last messages in the list after", end=" ")
    print ("removing it.\nHave fun!\n")

def encode_message (message, shift_num):
    
    alph_to_index_dict, index_to_alph_dict = data.alphabet_dictionaries()
    encoded_message = ""

    if shift_num == 0 or shift_num == 26:
        return message
    
    for i in range(len(message)):
        char = message[i]
        if char == " ":
            encoded_message += char
        elif char.lower() in alph_to_index_dict:
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
        else:
            encoded_message += char
    
    return encoded_message

def find_fake(list_of_msgs, list_of_msgs_copy):
    #calculate the chance of a random message being fake
    print("\nRemaining Messages Not Encoded:")
    if not list_of_msgs:
        print ("No messages to check.\nEnding program")
        return
    for msgs in list_of_msgs:
        print(" ".join(msgs))

    length = len(list_of_msgs_copy)
    chance = round((100 / length), 1)
    # weigh the chance of a message being fake
    weights = [chance]*len(list_of_msgs_copy)
    #random choice of message
    chosen_msgs = random.choices(list_of_msgs_copy, weights=weights, k=1)
    
    for msgs in chosen_msgs:
        chosen_msg = " ".join(msgs)
        print(f"\nThere is a {chance}% chance {chosen_msg} is a fake ", end="")
        print(f"message out of {len(list_of_msgs_copy)} messages\n")

def pop_from_stack(list_of_msgs, shift_numbers):
    #remove the last message and shift number from the list
    removed_msgs = list_of_msgs[-1]
    list_of_msgs.remove(list_of_msgs[-1])
    removed_shift_num = int(shift_numbers[-1])
    shift_numbers.remove(shift_numbers[-1])
    encoded_msgs = []

    for message in removed_msgs:
        encoded_msg = encode_message(message, removed_shift_num)
        encoded_msgs.append(encoded_msg)
    
    print ("Encoded message:", " ".join(encoded_msgs),"\n")


def print_msgs_in_list (list_of_msgs):
    for message in list_of_msgs:
        print (message)
