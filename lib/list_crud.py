def create_an_empty_list():
    create_an_empty_list = []
    return create_an_empty_list

def create_a_list():
    create = ["hello", "how", "are", "you"]
    return create

def add_element_to_end_of_list(my_list, element):
    my_list.append(element)
    # print(my_list)
    return my_list
add_element_to_end_of_list(["h", "e", "l", "l"], "o")

def add_element_to_start_of_list(l, element):
    l.insert(0, element)
    # print(l)
    return l
add_element_to_start_of_list(["t", "a", "r"], "s")

def remove_element_from_end_of_list(l):
    l.pop(len(l) - 1)
    return l

def remove_element_from_start_of_list(l):
    l.pop(0)
    return l

def retrieve_first_element_from_list(l):
    first = l[0]
    return first

def retrieve_element_from_index(l, index):
    retrieve = l[index]
    return retrieve


def retrieve_last_element_from_list(l):
    last = l[-1]
    return last
