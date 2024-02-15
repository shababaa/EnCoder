def alphabet_dictionaries():
    #keys and values for dictionary
    indexes = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,
    14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]

    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    # Initialize alphabet dictionaries
    # letter : index 
    alph_to_index_dict = {}
    for i in range(len(alphabet)):
        alph_to_index_dict[alphabet[i]] = indexes[i]

    # index : letter 
    index_to_alph_dict = {}
    for i in range(len(alphabet)):
        index_to_alph_dict[indexes[i]] = alphabet[i]

    return alph_to_index_dict, index_to_alph_dict