class Anagram:
    def __init__(self, word):
        self.word = word.lower()
       
    def match(self, word_list):
        anagrams = []

        for letter in word_list:
            if letter.lower() != self.word and sorted(letter.lower()) == sorted(self.word):
                anagrams.append(letter)

        return anagrams
          