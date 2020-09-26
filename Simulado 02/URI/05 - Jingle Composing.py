note_map = {
    'W' : 1.0,
    'H' : 1.0/2.0,
    'Q' : 1.0/4.0,
    'E' : 1.0/8.0,
    'S' : 1.0/16.0,
    'T' : 1.0/32.0,
    'X' : 1.0/64.0
}

def main():
    while True:
        input_string = input()

        if input_string == '*':
            return
        
        compositions = [x for x in input_string.split('/') if x != '']

        total = 0
        for composition in compositions:
            measure = 0.0
            for note in composition:
                measure += note_map[note]
            if measure == 1.0:
                total += 1
        
        print(total)


main()