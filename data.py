def alphabet_dictionaries():
    #keys and values for dictionary
    index1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    index2 = [14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
    indexes = index1 + index2
    letters1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm']
    letters2 = ['n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    alphabet = letters1 + letters2

    # Initialize alphabet dictionaries
    # char : index 
    alph_to_index_dict = {}
    for i in range(len(alphabet)):
        alph_to_index_dict[alphabet[i]] = indexes[i]

    # index : char 
    index_to_alph_dict = {}
    for i in range(len(alphabet)):
        index_to_alph_dict[indexes[i]] = alphabet[i]

    return alph_to_index_dict, index_to_alph_dict