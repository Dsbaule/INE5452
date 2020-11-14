from datetime import datetime

def main():
    distance = 0

    speed = None
    previousTime = None

    while True:
        data = input().split()

        time = datetime.strptime(data[0],"%H:%M:%S")
        
        if previousTime:
            diff = (time - previousTime).seconds / 3600
            distance += speed * diff
            distance = int(distance)

        if len(data) == 1:
            print("%s %.2f km" % (str(time.time()), distance))
        else:
            speed = int(data[1])

            if speed == 0:
                return
        
        previousTime = time

try:
    main()
except EOFError:
    pass