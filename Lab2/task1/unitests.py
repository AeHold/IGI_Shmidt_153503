import unittest
from main import find_sentences, find_nondeclarative, n_grams, average_sentence_length, average_word_length

class T(unittest.TestCase):
    def test_sentence_counter(self):
        self.assertEqual(find_sentences("Hello Mr. Watson. How are you?"), 2)
        self.assertEqual(find_sentences(""), 0)
        self.assertEqual(find_sentences("What should I do now... I want to know! It is scared me."), 3)

    def test_nondeclarative_counter(self):
        self.assertEqual(find_nondeclarative("Do you know the way? Yes, of course!"), 2)
        self.assertEqual(find_nondeclarative("Hello, my name is Nikita. I like do nothing."), 0)
        self.assertEqual(find_nondeclarative("Are you happy now? Because I am dying..."), 1)

    def test_average_sentence_length(self):
        self.assertEqual(average_sentence_length("Hello dear."), 9)
        self.assertEqual(average_sentence_length("Hello my world. I love you!"), 10)
        self.assertEqual(average_sentence_length("Do you wanna see a trick? I am gonna show you. It is bounced."), 15)
    
    def test_average_word_length(self):
        self.assertEqual(average_word_length("Hello"), 5)
        self.assertEqual(average_word_length("I want to know your nam."), 3)
        self.assertEqual(average_word_length("If everything okay, it is okay?"), 4)

    def test_n_grams(self):
        self.assertEqual(n_grams("Will come calling out", 2, 5), [("ll",2),("Wi",1),("il",1),("co",1),("om",1)])
        self.assertEqual(n_grams("Nothing ever comes without a consequence or cost, tell me"), 
                         [('Noth', 1), ('othi', 1), ('thin', 1), ('hing', 1), ('ever', 1), ('come', 1), ('omes', 1), ('with', 1), ('itho', 1), ('thou', 1)])
        self.assertEqual(n_grams("Rather be the hunter than the prey", 1, 7), [('e', 6), ('t', 5), ('h', 5), ('r', 3), ('a', 2), ('n', 2), ('R', 1)])
    
if __name__ == '__main__':
    unittest.main()