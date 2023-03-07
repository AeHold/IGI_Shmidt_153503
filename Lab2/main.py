import re

if __name__ == '__main__':
    str = input("Input text: ")
    abbreviates = ('Dr', 'Mr')
    number_of_sentences = 0
    result = re.findall(r'((\w+)(\.\.\.|!|\?|\.)?)',str, flags=0)

    for word in result:
        if word[2] != '':
            for trap in abbreviates:
                if word[1] == trap:
                    number_of_sentences -= 1
            number_of_sentences += 1
    print(number_of_sentences)
