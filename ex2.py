class Node:
    def __init__(self, song):
        self.song = song
        self.next = None


class Playlist:
    def __init__(self):
        self.head = None

    def add_song(self, song):
        new_node = Node(song)

        if self.head is None:
            self.head = new_node
            print(song, "added to playlist")
            return

        current = self.head
        while current.next:
            current = current.next

        current.next = new_node
        print(song, "added to playlist")

    def delete(self, song):
        if self.head is None:
            print("Playlist is empty")
            return

        if self.head.song == song:
            self.head = self.head.next
            print(song, "deleted from playlist")
            return

        current = self.head
        while current.next:
            if current.next.song == song:
                current.next = current.next.next
                print(song, "deleted from playlist")
                return
            current = current.next

        print(song, "not found in playlist")

    def search(self, song):
        current = self.head

        while current:
            if current.song == song:
                print(song, "found in playlist")
                return
            current = current.next

        print(song, "not found in playlist")

    def display(self):
        if self.head is None:
            print("Playlist is empty")
            return

        print("\nPlaylist:")
        current = self.head

        while current:
            print(current.song, end=" --> ")
            current = current.next

        print("END")


playlist = Playlist()

while True:
    print("\n--- MUSIC PLAYLIST ---")
    print("1. Add Song")
    print("2. Delete Song")
    print("3. Search Song")
    print("4. Display Playlist")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        song = input("Enter song name: ")
        playlist.add_song(song)

    elif choice == 2:
        song = input("Enter song name to delete: ")
        playlist.delete(song)

    elif choice == 3:
        song = input("Enter song name to search: ")
        playlist.search(song)

    elif choice == 4:
        playlist.display()

    elif choice == 5:
        print("Exit...")
        break

    else:
        print("Invalid choice!")