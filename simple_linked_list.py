class Node:
    def __init__(self, song_id: int):
        self.song_id = song_id
        self.next = None

class LinkedList:

    # Initially the list is empty
    def __init__(self):
        self.head = None


    def add(self, song_id):
        new_node = Node(song_id)
        if not self.head:
            # the new node becomes the head
            self.head = new_node
        else:
            # trying to find the last node, so that we can attach the new one
            #starting from the first one
            current = self.head
            #checking if the current node has a self.next value
            while current.next:
                #if it does, we move to the next node becoming the current one
                current = current.next
            #if it doesnt, we attach the new one to it
            current.next = new_node

    def print_songs(self):
        current = self.head
        #printing not only if there is a next one, but  if there is a current one
        while current:
            print(current.song_id, end='-->')
            current = current.next
        print('None')

    def reverse(self):
        #overriding the values prev, cur, next
        prev = None
        current = self.head
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev



