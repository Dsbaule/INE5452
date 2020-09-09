def insertion_sort(input_list: list):
    # If list is empty or has only 1 item, no sorting needed
    if len(input_list) <= 1:
        return input_list

    # For each element, move back until it's in order
    for i in range(len(input_list)):
        # Get new element
        elected = input_list[i]

        # Find new element's spot on list before it
        j = i - 1
        while j >= 0 and input_list[j] > elected:
            input_list[j + 1] = input_list[j]
            j -= 1
        input_list[j + 1] = elected

    # Return sorted list
    return input_list