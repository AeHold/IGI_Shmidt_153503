import re

if __name__ == '__main__':
    str = input("Input text: ")
    abbreviations = ('Dr', 'Mr', 'Ms', 'Mrs', 'etc', 'e.g', 'B.C', 'A.C', 'inc')
    number_of_sentences = 0
    nondeclarative_number = 0
    result = re.findall(r'((\w+)(\.\.\.|!|\?|\.)?)',str, flags=0)

    for word in result:
        if word[2] != '':
            for ban_words in abbreviations:
                if word[1] == ban_words:
                    number_of_sentences -= 1
            number_of_sentences += 1
            if (word[2] == '?' or word[2] =='!'):
                nondeclarative_number += 1
    print('Number of sentences is:', number_of_sentences)
    print('Number of non-declarative sentences is:', nondeclarative_number)
  
