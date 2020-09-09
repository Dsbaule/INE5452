from BucketSort.src.BucketSort import bucket_sort

def main():
    # Get input
    n, k = input().split()
    input_list = input().split()

    if k != 'x':
        k = int(k)
        for element in input_list:
            if len(element) != k:
                raise Exception("Invalid input")

    sorted_list = bucket_sort(input_list)

    output = ""
    for element in sorted_list:
        output += str(element) + " "
    output = output[:-1]

    print(output)

main()