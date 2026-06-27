class Edge:
    def __init__(self, u, v):
        self.u = u
        self.v = v


class Graph:
    def __init__(self, vertices=None, edges=None):
        if vertices is None:
            vertices = []
        if edges is None:
            edges = []

        self.vertices = list(vertices)
        self.neighbors = self.getAdjacencyLists(edges)

    # this will return a list of adjacency lists for edges
    def getAdjacencyLists(self, edges):
        neighbors = []

        for i in range(len(self.vertices)):
            neighbors.append([])

        for edge in edges:
            u = edge[0]
            v = edge[1]

            if 0 <= u < len(self.vertices) and 0 <= v < len(self.vertices):
                neighbors[u].append(Edge(u, v))

        return neighbors

    # kept this for compatibility with the originally given  misspelled method name
    def getAdjacnecyLists(self, edges):
        return self.getAdjacencyLists(edges)

    def getSize(self):
        return len(self.vertices)

    def getVertices(self):
        return self.vertices

    def getVertex(self, index):
        return self.vertices[index]

    def getIndex(self, v):
        return self.vertices.index(v)

    def getNeighbors(self, index):
        return self.neighbors[index]

    def getDegree(self, v):
        return len(self.neighbors[self.getIndex(v)])

    def printEdges(self):
        for u in range(len(self.neighbors)):
            print(str(self.getVertex(u)) + " (" + str(u), end="): ")

            for j in range(len(self.neighbors[u])):
                print("(" + str(u) + ", " + str(self.neighbors[u][j].v), end=")")

                if j != len(self.neighbors[u]) - 1:
                    print(", ", end="")

            print()

    def addVertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices.append(vertex)
            self.neighbors.append([])

    def getIndexFromNameOrNumber(self, value):
        if isinstance(value, int):
            return value

        return self.getIndex(value)

    def addEdge(self, u, v):
        indexU = self.getIndexFromNameOrNumber(u)
        indexV = self.getIndexFromNameOrNumber(v)

        if indexU < 0 or indexU >= self.getSize():
            return False

        if indexV < 0 or indexV >= self.getSize():
            return False

        if self.hasEdge(indexU, indexV):
            return False

        self.neighbors[indexU].append(Edge(indexU, indexV))
        return True

    # Adding a mutual friendship both ways
    def addUndirectedEdge(self, u, v):
        self.addEdge(u, v)
        self.addEdge(v, u)

    def hasEdge(self, u, v):
        indexU = self.getIndexFromNameOrNumber(u)
        indexV = self.getIndexFromNameOrNumber(v)

        for edge in self.neighbors[indexU]:
            if edge.v == indexV:
                return True

        return False

    def getFriendNames(self, index):
        friend_names = []

        for edge in self.neighbors[index]:
            friend_names.append(self.vertices[edge.v])

        return friend_names

    def printFriendsByName(self):
        for i in range(self.getSize()):
            friends = self.getFriendNames(i)

            if len(friends) == 0:
                print("Friends of " + self.vertices[i] + ": None")
            else:
                print("Friends of " + self.vertices[i] + ": " + ", ".join(friends))

    def saveFriendDatabase(self, filename="friend.txt"):
        file = open(filename, "w")

        file.write("The friend list for all users are:\n")

        for u in range(len(self.neighbors)):
            file.write(str(self.getVertex(u)) + " (" + str(u) + "): ")

            for j in range(len(self.neighbors[u])):
                file.write("(" + str(u) + ", " + str(self.neighbors[u][j].v) + ")")

                if j != len(self.neighbors[u]) - 1:
                    file.write(", ")

            file.write("\n")

        file.write("\nAlso display the friend list as actual names:\n")

        for i in range(self.getSize()):
            friends = self.getFriendNames(i)

            if len(friends) == 0:
                file.write("Friends of " + self.vertices[i] + ": None\n")
            else:
                file.write("Friends of " + self.vertices[i] + ": " + ", ".join(friends) + "\n")

        file.close()
