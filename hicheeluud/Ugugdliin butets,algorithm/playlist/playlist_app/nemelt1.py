class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class Playsongs:
    def __init__(self):
        self.head = None
        self.tail = None
        self.current_node = None

    def add_song(self, song):
        new_node = Node(song)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.current_node = new_node
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = new_node
        print(f"Нэмэгдсэн дуу: {song}")

    def remove_song(self, song):
        if self.head is None:
            return
        if self.head.data == song:
            self.head = self.head.next
            if self.current_node == self.head:
                self.current_node = None
        else:
            current_node = self.head
            while current_node.next is not None:
                if current_node.next.data == song:
                    current_node.next = current_node.next.next
                    if current_node.next is None:
                        self.tail = current_node
                    if self.current_node == current_node.next:
                        self.current_node = current_node
                    print(f"Устгагдсан дуу: {song}")
                    return
                current_node = current_node.next
        print(f"Ийм дуу playlisted алга байна: {song}")

    def print_playlist(self):
        if self.head is None:
            print("Playlist хоосон байна")
        else:
            current_node = self.head
            while current_node is not None:
                if current_node == self.current_node:
                    print(">>", current_node.data)
                else:
                    print(current_node.data)
                current_node = current_node.next

    def move_to_next_song(self):
        if self.current_node is not None and self.current_node.next is not None:
            self.current_node = self.current_node.next
        if self.current_node.next is None:
            print("Playlist - ийн сүүлийн дуу")
            return

    def move_to_previous_song(self):
        if self.current_node is not None and self.current_node != self.head:
            current_node = self.head
            while current_node.next != self.current_node:
                current_node = current_node.next
            self.current_node = current_node
        print(self.current_node)
        if self.current_node.prev is None:
            print("Playlist - ийн эхний дуу байна")
            return

    def print_current_song(self):
        if self.current_node is not None:
            print("Одоо тоглогдож байгаа дуу:", self.current_node.data)
        else:
            print("Playlist хоосон байна")

my_playlist = Playsongs()

while True:
    command = input("Эдгээр командаас сонгоно уу (add, remove, next, previous, current, print, exit): ")

    if command == "add":
        song = input("Дуугаа оруулна уу: ")
        my_playlist.add_song(song)

    elif command == "remove":
        song = input("Дуугаа оруулна уу: ")
        my_playlist.remove_song(song)

    elif command == "next":
        my_playlist.move_to_next_song()
        my_playlist.print_current_song()

    elif command == "previous":
        my_playlist.move_to_previous_song()
        my_playlist.print_current_song()

    elif command == "current":
        my_playlist.print_current_song()

    elif command == "print":
        my_playlist.print_playlist()

    elif command == "exit":
        break

    else:
        print("Ийм команд байхгүй")
