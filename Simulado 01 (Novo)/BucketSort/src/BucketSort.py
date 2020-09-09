from BucketSort.src.InsertionSort import insertion_sort
import string

def bucket_sort(input_list: list):
    # If list is empty or has only 1 item, no sorting needed
    if len(input_list) <= 1:
        return input_list

    # Get possible characters
    alphabet = list(string.digits + string.ascii_lowercase)

    # Create one bucket for each char
    buckets = [list() for _ in range(len(alphabet))]

    # Add each element in correct bucket
    for element in input_list:
        buckets[alphabet.index(element[0])].append(element)
    # Sort each bucket using insertion sort
    buckets = [insertion_sort(bucket) for bucket in buckets]

    # Join buckets
    sorted_list = list()
    for bucket in buckets:
        sorted_list += bucket

    # Return sorted list
    return sorted_list