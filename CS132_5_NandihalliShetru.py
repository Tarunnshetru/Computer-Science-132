SONG_FILE = "song_list.txt"


class Node:
    def __init__(self, e):
        self.element = e
        self.next = None


class LinkedList:
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__size = 0

    def addLast(self, e):
        newNode = Node(e)

        if self.__tail is None:
            self.__head = self.__tail = newNode
        else:
            self.__tail.next = newNode
            self.__tail = self.__tail.next

        self.__size += 1

    def add(self, e):
        self.addLast(e)

    def removeAt(self, index):
        if index < 0 or index >= self.__size:
            return None

        elif index == 0:
            temp = self.__head
            self.__head = self.__head.next
            self.__size -= 1

            if self.__head is None:
                self.__tail = None

            return temp.element

        else:
            previous = self.__head

            for i in range(1, index):
                previous = previous.next

            current = previous.next
            previous.next = current.next

            if current == self.__tail:
                self.__tail = previous

            self.__size -= 1

            return current.element

    def getSize(self):
        return self.__size

    def __iter__(self):
        return LinkedListIterator(self.__head)


class LinkedListIterator:
    def __init__(self, head):
        self.current = head

    def __next__(self):
        if self.current is None:
            raise StopIteration
        else:
            element = self.current.element
            self.current = self.current.next
            return element

    def __iter__(self):
        return self


class Song:
    def __init__(self, title, artist, year):
        self.title = title
        self.artist = artist
        self.year = year

    def __str__(self):
        return self.title + "," + self.artist + "," + self.year


def load_songs():
    playlist = LinkedList()

    with open(SONG_FILE, "r") as file:
        first_line = True

        for line in file:
            line = line.strip()

            if line == "":
                continue

            if first_line:
                first_line = False

                if line.lower().replace(" ", "") == "song,artist,year":
                    continue

            parts = line.split(",")

            if len(parts) == 3:
                title = parts[0].strip()
                artist = parts[1].strip()
                year = parts[2].strip()

                playlist.add(Song(title, artist, year))

    return playlist


def save_songs(playlist):
    with open(SONG_FILE, "w") as file:
        file.write("Song,Artist,Year\n")

        for song in playlist:
            file.write(str(song) + "\n")


def display_menu():
    print("\nMusic play simulator\n")
    print("A. play all")
    print("B. add a song")
    print("C. delete a song")
    print("D. start playing from a song")
    print("E: Exit")


def print_song(song):
    print(f"{song.title:<25}{song.artist:<20}{song.year}")


def play_all(playlist):
    print("playing")

    for song in playlist:
        print_song(song)


def add_song(playlist):
    print("Enter the song in this format: song,artist,year")

    user_input = input()

    parts = user_input.split(",")

    if len(parts) != 3:
        print("Invalid format")
        return

    title = parts[0].strip()
    artist = parts[1].strip()
    year = parts[2].strip()

    playlist.add(Song(title, artist, year))

    print("the song has been added")


def delete_song(playlist):
    print("Enter the name of the song:")

    song_name = input().strip()

    index = 0

    for song in playlist:
        if song.title.lower() == song_name.lower():
            deleted_song = playlist.removeAt(index)
            print(deleted_song.title + " is deleted")
            return

        index += 1

    print(song_name + " was not found")


def play_from_song(playlist):
    print("Enter the song to start")

    song_name = input().strip()

    found = False

    for song in playlist:
        if song.title.lower() == song_name.lower():
            found = True
            print("playing")

        if found:
            print_song(song)

    if not found:
        print(song_name + " was not found")


def main():
    playlist = load_songs()

    while True:
        display_menu()

        choice = input().strip().upper()

        if choice == "A":
            play_all(playlist)

        elif choice == "B":
            add_song(playlist)

        elif choice == "C":
            delete_song(playlist)

        elif choice == "D":
            play_from_song(playlist)

        elif choice == "E":
            save_songs(playlist)
            print("music play simulator off")
            break

        else:
            print("Invalid option")


main()
