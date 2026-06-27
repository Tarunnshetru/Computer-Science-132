from Graph_code import Graph


def build_social_network():
    vertices = ["Peter", "Jane", "Mark", "Cindy", "Wendy"]

    

    edges = [
        [0, 1], [1, 0],
        [0, 2], [2, 0],
        [1, 2], [2, 1],
        [1, 3], [3, 1],
        [2, 3], [3, 2],
        [2, 4], [4, 2],
        [3, 4], [4, 3]
    ]

    return Graph(vertices, edges)


def get_new_user_name(graph):
    print("Please add new user:")

    while True:
        name = input("Enter: ").strip()

        if name == "":
            print("The name cannot be blank,so please enter a name.")
        elif name in graph.getVertices():
            print("That user already exists. Please enter a different name.")
        else:
            return name


def print_friend_choices(graph, new_user_index):
    print("Please select who you want to add from this list, add one friend at a time, enter -1 to exit.")
    print()

    for i in range(graph.getSize()):
        if i != new_user_index:
            print(str(i) + ": " + graph.getVertex(i))

    print()


def add_friends_for_new_user(graph, new_user_index):
    while True:
        print_friend_choices(graph, new_user_index)

        choice_text = input("Enter: ").strip()

        try:
            choice = int(choice_text)
        except ValueError:
            print("Please enter a valid number.")
            print()
            continue

        if choice == -1:
            break

        if choice < 0 or choice >= graph.getSize():
            print("That number is not in the list.")
            print()
            continue

        if choice == new_user_index:
            print("You cannot friend yourself.")
            print()
            continue

        if graph.hasEdge(new_user_index, choice):
            print("You have already established friendship with " + graph.getVertex(choice) + ".")
            print()
            continue

        graph.addUndirectedEdge(new_user_index, choice)

        print("You have friended " + graph.getVertex(choice) + ".")
        print()


def display_all_friend_lists(graph):
    print("The friend list for all users are:")
    print()

    graph.printEdges()

    print()
    print("Also display the friend list as actual names:")
    print()

    graph.printFriendsByName()


def main():
    graph = build_social_network()

    new_user = get_new_user_name(graph)
    graph.addVertex(new_user)

    new_user_index = graph.getIndex(new_user)

    print()

    add_friends_for_new_user(graph, new_user_index)

    print()

    display_all_friend_lists(graph)

    graph.saveFriendDatabase("friend.txt")

    print()
    print("Friend relationships saved to friend.txt")


main()
