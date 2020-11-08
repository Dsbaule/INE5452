note_map = {
    'C' : 'C',
    'B#' : 'C',

    'C#' : 'C#',
    'Db' : 'C#',

    'D' : 'D',

    'D#' : 'D#',
    'Eb' : 'D#',

    'E' : 'E',
    'Fb' : 'E',

    'F' : 'F',
    'E#' : 'F',

    'F#' : 'F#',
    'Gb' : 'F#',

    'G' : 'G',

    'G#' : 'G#',
    'Ab' : 'G#',

    'A' : 'A',

    'A#' : 'A#',
    'Bb' : 'A#',

    'B' : 'B',
    'Cb' : 'B'
}

tone_map = {
    'C' : 1,
    'C#' : 2,
    'D' : 3,
    'D#' : 4,
    'E' : 5,
    'F' : 6,
    'F#' : 7,
    'G' : 8,
    'G#' : 9,
    'A' : 10,
    'A#' : 11,
    'B' : 12,
}

def diff_tone(note1_original, note2_original):
    note1 = tone_map[note1_original]
    note2 = tone_map[note2_original]

    if note1 < note2:
        return note2 - note1
    else:
        return 12 - (note1 - note2)

def main():
    while True:
        M, T = [int(x) for x in input().split()]

        if M == 0 and T == 0:
            return

        song = [note_map[x] for x in input().split()]
        sequence = [note_map[x] for x in input().split()]

        distance_song = list()
        for i in range(len(song) - 1):
            distance_song.append(str(diff_tone(song[i], song[i + 1])))

        distance_sequence = list()
        for i in range(len(sequence) - 1):
            distance_sequence.append(str(diff_tone(sequence[i], sequence[i + 1])))

        if ' '.join(distance_sequence) in ' '.join(distance_song):
            print('S')
        else:
            print('N')

main()