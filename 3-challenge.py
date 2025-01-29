'find acroname in words'
def genrarate_acroname(sentence):
    acroname = ''
    for word in sentence.split(' '):
        acroname += word[0].capitalize()
    return acroname

print(genrarate_acroname('Random Access Memory'))
