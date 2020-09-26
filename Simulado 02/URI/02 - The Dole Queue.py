class QueueMember:
    def __init__(self, number):
        self.number = number
        self.next = self
        self.prev = self
    def set_next(self, next):
        self.next = next
    def get_next(self):
        return self.next
    def set_prev(self, prev):
        self.prev = prev
    def get_prev(self):
        return self.prev
    def insert_after(self, new_next):
        new_next.set_next(self.next)
        new_next.set_prev(self)
        self.next.set_prev(new_next)
        self.set_next(new_next)
    def remove(self):
        if not self.last():
            self.next.set_prev(self.prev)
            self.prev.set_next(self.next)
    def last(self):
        return self.next == self


def main():
    while True:
        input_string = input()

        if input_string == '0 0 0':
            return

        N, k, m = [int(x) for x in input_string.split()]

        dole_queue = None
        for i in range(N):
            if dole_queue is None:
                dole_queue = QueueMember(i + 1)
            else:
                dole_queue.insert_after(QueueMember(i + 1))
                dole_queue = dole_queue.get_next()
        
        officer_1 = dole_queue
        officer_2 = dole_queue.get_next()

        output_string = ''

        while True:
            for _ in range(k):
                officer_1 = officer_1.get_next()
            for _ in range(m):
                officer_2 = officer_2.get_prev()
            
            if officer_1 == officer_2:
                output_string += ('   ' + str(officer_1.number))[-3:]
                if officer_1.last():
                    print(output_string)
                    break
                officer_1 = officer_1.get_prev()
                officer_2 = officer_2.get_next()
                officer_2.get_prev().remove()
            else:
                output_string += ('   ' + str(officer_1.number))[-3:]
                officer_1 = officer_1.get_prev()
                officer_1.get_next().remove()
                output_string += ('   ' + str(officer_2.number))[-3:]
                if officer_2.last():
                    print(output_string)
                    break
                if officer_1 == officer_2:
                    officer_1 = officer_1.get_prev()
                officer_2 = officer_2.get_next()
                officer_2.get_prev().remove()
            
            output_string += ','


main()