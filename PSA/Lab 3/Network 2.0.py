import json
import nltk
import re
import matplotlib.pyplot as plot
from collections import Counter

# downloading the tweets from the file
try:
    net = open("tweets.json", encoding='utf8')
    data = json.loads(net.read())

except Exception as e:
    print(e)
finally:
    net.close()

# PRINTING 10 MOST POPULAR WORDS
# we use the Counter tool from collections module
# which can detect n most popular elements in a
# data set using most_common(n) method
list_of_words = list()
restrictions = list()
restrictions.append("https")
restrictions.append("http")
restrictions.append("RT")
restrictions.append("things")
restrictions.append("https")
for tweet in data:
    words = nltk.word_tokenize(tweet["text"])
    for j in range(0, len(words)):
        if words[j].isalpha() and (words[j] not in restrictions):
            list_of_words.append(words[j])

"""
Counter = Counter(list_of_words)
most_popular = Counter.most_common(10)
print("10 most popular words are:")
for i in range(0, len(most_popular)):
    print(f"{most_popular[i][0]}  {most_popular[i][1]}")
"""

# 10 MOST POPULAR NOUNS
nouns = list()
for word, pos in nltk.pos_tag(list_of_words):
    if (pos == 'NN') or (pos == 'NNP') or (pos == 'NNS') or (pos == 'NNPS'):
        if word != 'years':
            nouns.append(word)

"""
Counter = Counter(nouns)
most_popular = Counter.most_common(10)
print("10 most popular nouns are:")
for i in range(0, len(most_popular)):
    print(f"{most_popular[i][0]}  {most_popular[i][1]}")
"""

"""
# 10 MOST POPULAR PROPER NOUNS
proper_nouns = list()
tagged = nltk.pos_tag(list_of_words)
for word, tag in tagged:
    if (tag == 'NNP') and (word != 'A'):
        proper_nouns.append(word)

Counter = Counter(proper_nouns)
most_popular = Counter.most_common(10)
print("10 most popular proper nouns are:")
for i in range(0, len(most_popular)):
    print(f"{most_popular[i][0]}  {most_popular[i][1]}")
"""

"""
# FREQUENCY BAR GRAPH FOR THE GIVEN WORD
word = input("Enter the word to find out its frequency over the time: ")
months = list()
frequency = list()
for i in range(0, 7):
    frequency.append(0)

index = -1
for block in data:
    month = block["created_at"][0:7]
    if month not in months:
        index += 1
        months.append(month)

    word_set = re.findall(r"\w+", block["text"])
    frequency[index] += word_set.count(word)

# creating the graph and the structures which will build its basis
graph = plot.figure(figsize=(10, 5))

# plotting the bar graph
plot.bar(months, frequency, color='blue', width=0.5)
plot.xlabel("Months")
plot.ylabel("Word's frequency")
plot.title(f'Frequency bar chart of the word "{word}"')
plot.show()
"""

"""
# 10 MOST POPULAR NOUNS (2-ND EDITION)
def rating(f, nR, nL):
    return f * (1.4 + nR) * (1.2 + nL)

boofer = list()
ratings = list()
r_copy = list()
for i in range(0, len(nouns)):
    print(i)
    frequency = nouns.count(nouns[i])
    normRetweet = 0
    normLikes = 0
    if (nouns[i] not in boofer) and (len(nouns[i]) > 2) and (nouns[i] not in restrictions):
        boofer.append(nouns[i])
        for block in data:
            word_set = re.findall(r"\w+", block["text"])
            if nouns[i] in word_set:
                normRetweet += block["retweets"]
                normLikes += block["likes"]
        ratings.append(rating(frequency, normRetweet, normLikes))
        r_copy.append(rating(frequency, normRetweet, normLikes))

ratings.sort()
j = len(ratings) - 1
count = 0
print("10 most popular nouns (2-nd version)")
while count < 10:
    for k in range(0, len(r_copy)):
        if r_copy[k] == ratings[j]:
            print(f"{boofer[k]}  {r_copy[k]}")
            count += 1
            break
    j -= 1
"""

"""
# <<typing prediction>>
# ---------------------
# SUGGESTIONS
piece = input('Enter the starting piece of a word: ')
suggestions = list()
for i in range(0, len(list_of_words)):
    if list_of_words[i].startswith(piece):
        suggestions.append(list_of_words[i])

Counter = Counter(suggestions)
most_popular = Counter.most_common(3)
print("The possible words are:")
for i in range(0, len(most_popular)):
    print(f"{most_popular[i][0]} ({most_popular[i][1]})")
"""


# SUGGESTION OCCURRENCES
word = input("Enter a certain word: ")
suggestions_2 = list()
for tweet in data:
    words = nltk.word_tokenize(tweet["text"])
    for j in range(0, len(words) - 1):
        if (words[j] == word) and (words[j + 1].isalpha()) and (words[j + 1] not in restrictions):
            suggestions_2.append(words[j + 1])

Counter = Counter(suggestions_2)
most_popular = Counter.most_common(3)
print("The following words are associated with the given one:")
for i in range(0, len(most_popular)):
    print(f"{most_popular[i][0]} ({most_popular[i][1]})")

