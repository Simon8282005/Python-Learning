a_tuple = 1, 2, 3, 4, 5, 6
b_list = [60, 5, 27, 832, 256]


def print_item_in_tuple():
    for content in a_tuple:
        print(content)


def b():
    for index in range(len(b_list)):
        print('index=', index, "the number in this list=", b_list[index])
        # Output: index= 4 the number in this list= 256


b()
