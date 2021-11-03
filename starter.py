# Recitation Activity 1

def countWords(aString):
    '''
        >>> expected = {'he': 2, 'is': 2, 'here': 2, 'now': 1}
        >>> countWords('#He is here,HERE he is now..') == expected
        True
        >>> text = """I scream, you scream, we all scream for
        ...        ice cream. I love chocolate,so WE can all
        ...        agree that it is my favorite ice cream flavor!!!"""
        >>> expected = {'i': 2, 'scream': 3, 'you': 1, 'we': 2, 'all': 2, 'for': 1, 'ice': 2, 'cream': 2, 'love': 1, 'chocolate': 1, 'so': 1, 'can': 1, 'agree': 1, 'that': 1, 'it': 1, 'is': 1, 'my': 1, 'favorite': 1, 'flavor': 1}
        >>> countWords(text) == expected
        True
    '''
    for char in aString:
      if not char.isalpha():
        aString = aString.replace(char, " ")
    newDict = {}
    newList = aString.split()
    for word in newList:
      word = word.lower()
      if word not in newDict:
        newDict[word] = 1
      else:
        newDict[word] += 1
    return newDict

print(countWords("I scream, you scream, we all scream for ice cream. I love chocolate,so WE can all agree that it is my favorite ice cream flavor!!!"))
