import data
import random


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

def find_fake(list_of_msgs, total_msgs):
    #calculate the chance of a random message being fake
    print("Remaining Messages Not Encoded:")
    if not list_of_msgs:
        print ("No messages to check.\nEnding program")
        return
    for msgs in list_of_msgs:
        print(" ".join(msgs))

    length = total_msgs
    chance = round((100 / length), 1)
    # weigh the chance of a message being fake
    weights = [chance]*len(list_of_msgs)
    #random choice of message
    chosen_msgs = random.choices(list_of_msgs, weights=weights, k=1)
    
    for msgs in chosen_msgs:
        chosen_msg = " ".join(msgs)
        print(f"There is a {chance}% chance {chosen_msg} is a fake message")

def pop_from_stack(list_of_msgs, shift_numbers, isFirst=False):
    #remove the last message and shift number from the list
    removed_msgs = list_of_msgs[-1]
    list_of_msgs.remove(list_of_msgs[-1])
    removed_shift_num = int(shift_numbers[-1])
    shift_numbers.remove(shift_numbers[-1])
    encoded_msgs = []

    for message in removed_msgs:
        encoded_msg = encode_message(message, removed_shift_num)
        encoded_msgs.append(encoded_msg)
    #return encoded_msg
    if isFirst:
        print ("Encoded message:", " ".join(encoded_msgs),"\n")


def print_msgs_in_list (list_of_msgs):
    for message in list_of_msgs:
        print (message)
