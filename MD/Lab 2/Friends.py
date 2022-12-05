import nltk

# reading each line from the file in order to
# fill the matrix of relationships

try:
    friends = open('matrix.txt', 'r')
    matrix = list()

    for line in friends:
        lis = list()
        boofer = ''
        i = 0
        counter = 0
        while (line[i] != '|') and (counter <= 1):
            boofer += line[i]
            i += 1
            if line[i] == ' ':
                counter += 1
        lis.append(boofer)

        i = 0
        while i < len(line):
            if line[i] in ['0', '1']:
                lis.append(int(line[i]))
            i += 1
        # print(lis)
        matrix.append(lis)

except Exception as e:
    print(e)
finally:
    friends.close()

# find the person with the most friends
# the following list contains the number of friends
# of each person
list_of_friends = list()
for i in range(1, 21):
    list_of_friends.append(matrix[i].count(1))

max = 0
for i in range(0, len(list_of_friends)):
    if max < list_of_friends[i]:
        max = list_of_friends[i]

# appending the number of friends to each row in the matrix
for i in range(1, 21):
    matrix[i].append(matrix[i].count(1))

# we print all the persons with the maximum number of friends
print("The people with maximum friends are: ")
for i in range(1, 21):
    # print(matrix[i])
    if matrix[i][len(matrix[i]) - 1] == max:
        print(matrix[i][0])

print()
print("-----------------------------------------------------")
print()

# sort people by the number of friends
# boofer_list is used to avoid printing duplicates
list_of_friends.sort()
print("The descending list of people and their friends:")
i = len(list_of_friends) - 1
boofer_list = list()
while i >= 0:
    for j in range(1, 21):
        if (list_of_friends[i] == matrix[j][len(matrix[j]) - 1]) and (matrix[j][0] not in boofer_list):
            print(f"{matrix[j][0]} ---------> {list_of_friends[i]}")
            boofer_list.append(matrix[j][0])
    i -= 1


# CREATING RATINGS (SHORTEST PATH ALGORITHM)
# utility function to form edge between two vertices
# source and dest
def add_edge(adj, src, dest):
    adj[src].append(dest)
    adj[dest].append(src)


# a modified version of BFS that stores predecessor
# of each vertex in array p
# and its distance from source in array d
def BFS(adj, src, dest, v, pred, dist):
    # a queue to maintain queue of vertices whose
    # adjacency list is to be scanned as per normal
    # DFS algorithm
    queue = []

    # boolean array visited[] which stores the
    # information whether ith vertex is reached
    # at least once in the Breadth first search
    visited = [False for i in range(v)]

    # initially all vertices are unvisited
    # so v[i] for all i is false
    # and as no path is yet constructed
    # dist[i] for all i set to infinity
    for i in range(v):
        dist[i] = 1000000
        pred[i] = -1

    # now source is first to be visited and
    # distance from source to itself should be 0
    visited[src] = True
    dist[src] = 0
    queue.append(src)

    # standard BFS algorithm
    while len(queue) != 0:
        u = queue[0]
        queue.pop(0)
        for i in range(len(adj[u])):

            if not visited[adj[u][i]]:
                visited[adj[u][i]] = True
                dist[adj[u][i]] = dist[u] + 1
                pred[adj[u][i]] = u
                queue.append(adj[u][i])

                # We stop BFS when we find
                # destination.
                if adj[u][i] == dest:
                    return True

    return False


# utility function to print the shortest distance
# between source vertex and destination vertex
def printShortestDistance(adj, s, dest, v):
    # predecessor[i] array stores predecessor of
    # i and distance array stores distance of i
    # from s
    pred = [0 for i in range(v)]
    dist = [0 for i in range(v)]

    if not BFS(adj, s, dest, v, pred, dist):
        return 0

    # vector path stores the shortest path
    path = []
    crawl = dest
    path.append(crawl)

    while pred[crawl] != -1:
        path.append(pred[crawl])
        crawl = pred[crawl]

    # distance from source is in distance array
    return dist[dest]


# no. of vertices
v = 20

# array of vectors is used to store the graph
# in the form of an adjacency list
adj = [[] for i in range(v)]

# creating graph given in the above diagram.
# add_edge function takes adjacency list, source
# and destination vertex as argument and forms
# an edge between them.
for i in range(1, 20):
    for j in range(i + 1, 21):
        if matrix[i][j] == 1:
            add_edge(adj, i - 1, j - 1)

# finding the rating for each person
listOfRatings = list()
for source in range(0, 20):
    rating = 0
    for dest in range(0, 20):
        if source != dest:
            rating += (printShortestDistance(adj, source, dest, v)) - 1
    listOfRatings.append(rating)

print()
print("-----------------------------------------------------")
print()
print("People and their ratings (1-st version)")
for i in range(0, 20):
    print(f"{matrix[i + 1][0]} ---------> {listOfRatings[i]}")


# CREATING A NEW RATING FOR EACH PERSON
# USING THEIR INFLUENCE COEFFICIENT

# first we update our list of ratings
try:
    inf = open('influence.txt', 'r')
    index = 0
    for line in inf:
        words = nltk.word_tokenize(line)
        listOfRatings[index] *= 0.5 * float(words[3])
        matrix[index + 1].append(listOfRatings[index])
        index += 1

except Exception as e:
    print(e)
finally:
    inf.close()

listOfRatings.sort()
print()
print("-----------------------------------------------------")
print()
print("People and their ratings (2-nd version with respect of influence)")
i = 19
while i >= 0:
    for j in range(1, 21):
        if matrix[j][22] == listOfRatings[i]:
            print(f"{matrix[j][0]} ---------> {listOfRatings[i]}")
    i -= 1


# ANALYZING THE TITLE OF THE BOOK
title = 'From T-Rex to Multi Universes: How the Internet has Changed Politics, Art and Cute Cats'
title_words = nltk.word_tokenize(title)

print()
print("-----------------------------------------------------")
print()
print("Specter of interests of the book:")
book_interests = list()
try:
    interests = open("interests.txt", 'r')
    for line in interests:
        line_words = nltk.word_tokenize(line)

        if line_words[0] in title_words:
            print(line_words[0])
            book_interests.append(line_words[0])

except Exception as e:
    print(e)
finally:
    interests.close()


# PROMOTING THE BOOK
# first we count the number of common words
# in people's interests and book topics
interest_occurencies = list()
try:
    people_interests = open('people_interests.txt', 'r')
    for line in people_interests:
        count = 0
        interest_words = nltk.word_tokenize(line)
        for i in range(2, len(interest_words)):
            if interest_words[i] in book_interests:
                count += 1
        interest_occurencies.append(count)

except Exception as e:
    print(e)
finally:
    people_interests.close()

final_score = list()
for i in range(1, 21):
    final_score.append(0.2 * matrix[i][22] * interest_occurencies[i - 1])
    matrix[i].append(0.2 * matrix[i][22] * interest_occurencies[i - 1])

final_score.sort()
count = 0
i = len(final_score) - 1
print()
print("-----------------------------------------------------")
print()
print("Promotion score:")
while i >= 0:
    for j in range(1, 21):
        if (final_score[i] == matrix[j][23]) and (count < 5):
            count += 1
            print(f"{matrix[j][0]} ---------> {matrix[j][23]}")
    i -= 1
