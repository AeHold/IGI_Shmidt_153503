import re
from constants import ABBREVIATIONS

def find_sentences(text):
    number_of_sentences = 0
    result = re.findall(r'((\w+)(\.\.\.|!|\?|\.)?)',text, flags=0)
    for word in result:
        if word[2] != '':
            for ban_words in ABBREVIATIONS:
                if word[1] == ban_words:
                    number_of_sentences -= 1
            number_of_sentences += 1
    return number_of_sentences

def find_nondeclarative(text):
    nondeclarative_number = 0
    result = re.findall(r'((\w+)(\.\.\.|!|\?|\.)?)',text, flags=0)
    for word in result:
        if word[2] != '':
            if (word[2] == '?' or word[2] =='!'):
                nondeclarative_number += 1
    return nondeclarative_number

def average_sentence_length(text):
    average_length_sentence = 0
    counter = 0
    length = 0
    result = re.findall(r'((\w+)(\.\.\.|!|\?|\.)?)',text, flags=0)
    reg = r'[0-9]+'
    for word in result:
        if re.search(reg, word[1]):
            counter -= 1
        if (word[2] != '.' or word[2] != '?' or word[2] != '!' or word[2] != '...'):
            length += len(word[1])
        if (word[2] == '.' or word[2] == '?' or word[2] == '!' or word[2] == '...'):
            counter += 1
            average_length_sentence += length
            length = 0
    return average_length_sentence / counter
    
def average_word_length(text):
    result = re.findall(r'((\w+)(\.\.\.|!|\?|\.)?)',text, flags=0)
    reg = r'[0-9]+'
    word_counter = 0
    word_length = 0
    for word in result:
        if re.search(reg, word[1]):
            continue
        if word != ' ':
            word_counter += 1
            word_length += len(word[1])
    return word_length / word_counter

def n_grams(text, n = 4, k = 10):
    n_grams = {}
    result = re.findall(r'((\w+)(\.\.\.|!|\?|\.)?)',text, flags=0)
    reg = r'[0-9]+'
    for word in result:
        if re.search(reg, word[1]):
            continue
        for i in range(len(word[1]) - n + 1):
            s = word[0][i:i + n]
            n_grams[s] = n_grams.get(s, 0) + 1
    top_k = sorted(n_grams.items(), key = lambda x: x[1],reverse=True)[:k]
    return top_k

if __name__ == '__main__':
    text = input("Input text: ")
    print('Number of sentences is:', find_sentences(text))
    print('Number of non-declarative sentences is:', find_nondeclarative(text))
    print('Average sentence length in characters is:', average_sentence_length(text))
    print('Average word length in the text is:', average_word_length(text))
    try:
        n = int(input("Input N(press Enter to setup default): "))
        k = int(input("Input K(press Enter to setup default): "))
        print(f'First top-{k} {n}-grams are: {n_grams(text, n, k)}')
    except ValueError:    
        print(f'First top-{10} {4}-grams are: {n_grams(text, 4, 10)}')