class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
    def insert(self, value):
        if self.value >= value:
            self.insert_left(value)
        else:
            self.insert_right(value)

    def insert_left(self, value):
        if self.left == None:
            self.left = Node(value)
        else:
            self.left.insert(value)

    def insert_right(self, value):
        if self.right == None:
            self.right = Node(value)
        else:
            self.right.insert(value)

def main():
    C = int(input())

    for i in range(C):
        N = int(input())

        tree = None

        numbers = [int(x) for x in input().split()]
        for number in numbers:
            if tree == None:
                tree = Node(number)
            else:
                tree.insert(number)

        output_string = ''
        node_queue = [tree]
        while len(node_queue) > 0:
            node = node_queue.pop(0)
            output_string += str(node.value) + ' '
            if node.left != None:
                node_queue.append(node.left)
            if node.right != None:
                node_queue.append(node.right)
        
        print('Case ' + str(i + 1) + ':')
        print(output_string[:-1] + '\n')


main()