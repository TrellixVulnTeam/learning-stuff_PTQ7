# -*- coding: utf-8 -*-


from urllib.request import urlopen
with urlopen('http://sixty-north.com/c/t.txt')as story:
    story_words=[]
    for line in story:
        line_words=line.split()
        for word in line_words:
            story_words.append(word)

for word in story_words:
    print(word)


