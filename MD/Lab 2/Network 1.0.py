import json
import re
import nltk

# POPULAR HASHTAGS
# we read each line of txt file representing json code
# and representing it as a dictionary
# we also create a list to store only the text of each tweet
# it is called the (hashtags list)

tweets = list()
try:
    network = open('tweets.txt')
    for line in network:
        data = json.loads(line)
        for i in data:
            if i == 'text':
                tweets.append(data['text'])

except Exception as e:
    print(e)
finally:
    network.close()

hashtags = list()
for i in range(0, len(tweets)):
    words = re.findall(r"\w+", tweets[i])

    for j in range(0, len(words)):
        index = tweets[i].find(words[j])
        if tweets[i][index - 1] == '#':
            hashtags.append('#' + words[j])
            break

frequencies = list()
for i in range(0, len(hashtags)):
    frequencies.append(hashtags.count(hashtags[i]))

frequencies = list(set(frequencies))
frequencies.sort()

print("The list of popular hashtags with their occurrences:")
count = 0
j = 1
boofer = list()
while count < 10:
    i = 0
    while (i < len(hashtags)) and (count < 10):
        if (frequencies[len(frequencies) - j] == hashtags.count(hashtags[i])) and (hashtags[i] not in boofer):
            boofer.append(hashtags[i])
            print(f"{hashtags[i]} -------> {frequencies[len(frequencies) - j]}")
            count += 1

        i += 1
    j += 1

# EMOTIONAL ANALYSIS
# for this task we will need to analyze
# the given in the text file dictionary
# (corresponds to emotional_dict list)
# also we will calculate the rank of each tweet
# and add it into the emotional_ranking list
# finally we will create emotional_list to store
# the id and the rank of each tweet simultaneously


emotional_dict = list()
try:
    dictionary = open('AFINN-111.txt')
    for line in dictionary:
        i = 0
        l = re.findall(r"\w+", line)
        tokens = nltk.word_tokenize(line)

        if line[line.find(l[len(l) - 1]) - 1] == '-':
            l[len(l) - 1] = '-' + l[len(l) - 1]

        lin = list()
        lin.append(tokens[0])
        lin.append(l[len(l) - 1])

        emotional_dict.append(lin)

except Exception as e:
    print(e)
finally:
    network.close()

emotional_ranking = list()
for i in range(0, len(tweets)):
    rank = 0
    words = nltk.word_tokenize(tweets[i])

    for j in range(0, len(words)):
        for k in range(0, len(emotional_dict)):
            if words[j] == emotional_dict[k][0]:
                rank += int(emotional_dict[k][1])
                break
    emotional_ranking.append(rank)

emotion_list = list()
try:
    network = open('tweets.txt')
    index = 0
    for line in network:
        data = json.loads(line)
        lin = list()
        for i in data:
            if i == 'created_at':
                lin.append(data['text'])
                lin.append(data['id'])
                lin.append(emotional_ranking[index])
                index += 1
                emotion_list.append(lin)

except Exception as e:
    print(e)
finally:
    network.close()

# writing the tweets and their ranks into the file
try:
    with open("Tweets ranks.txt", "w") as t:
        t.write("First: id; Second: the rank")
        for i in range(0, len(emotion_list)):
            li = list()
            li.append(emotion_list[i][1])
            li.append(emotion_list[i][2])
            t.write("\n" + str(li))
except Exception as e:
    print(e)
finally:
    t.close()
    print()
    print()
    print()
    print()
    print("The data was written into the file successfully")


# MOST POSITIVE AND NEGATIVE TWEETS

emotional_ranking.sort()
print()
print()
print()
print()
print("10 most positive tweets:")
print()
print()

count = 0
boofer = list()
while count < 10:
    i = len(emotional_ranking) - 1
    while (i > 0) and (count < 10):
        for j in range(0, len(emotion_list)):
            if (emotional_ranking[i] == emotion_list[j][2]) and (emotion_list[j][0] not in boofer) and (count < 10):
                boofer.append(emotion_list[j][0])
                print(f"{emotion_list[j][0]} -------> {emotion_list[j][2]}")
                print()
                count += 1

        i -= 1

print()
print()
print()
print()
print("10 most negative tweets:")
print()
print()

count = 0
boofer = list()
while count < 10:
    i = 0
    while (i < len(emotional_ranking)) and (count < 10):
        for j in range(0, len(emotion_list)):
            if (emotional_ranking[i] == emotion_list[j][2]) and (emotion_list[j][0] not in boofer) and (count < 10):
                boofer.append(emotion_list[j][0])
                print(f"{emotion_list[j][0]} -------> {emotion_list[j][2]}")
                print()
                count += 1

        i += 1

# it takes about 45 seconds to execute the code
