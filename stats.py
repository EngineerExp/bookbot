def get_num_words(text):
    words = text.split()
    return len(words)

def get_char_and_nums(text):
    char_count = {}
    for char in text:
        char = char.lower()  # Normalize to lowercase
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

test_dict = {'a': 5, 'b': 2, 'c': 9, 'd': 1," ":7, "1":3, "!":4}

def sort_dict_by_value(input_dict):
    new_dict = {}
    sorted_items = sorted(input_dict.items(), key=lambda item: item[1], reverse=True)
    for k, v in sorted_items:
        if k.isalpha():  # Only print alphabetic characters
            # print(f"{k}: {v}")
            new_dict[k] = v
    return new_dict

# print(sort_dict_by_value(test_dict))


#---------------This doesn't work----------------
# def get_key_value_list(input_dict):
#     k_list = []
#     v_list = []

#     for k in input_dict:
#         k_list.append(k)
#         v_list.append(input_dict[k])
#     return k_list, v_list

# def make_dict_from_lists(k_list, v_list):
#     if len(k_list) != len(v_list):
#         raise ValueError("Lists must be of the same length")
#     result_dict = {}

#     for i in range(len(k_list)):
#         result_dict["letter"]
#     return result_dict


# def 
# print(make_dict_from_lists(get_key_value_list(test_dict)))

# print(make_dict_from_lists(get_key_value_list(test_dict)))