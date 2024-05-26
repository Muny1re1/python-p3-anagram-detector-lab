class Anagram:
    def __init__(self, word):
            self.word = word.lower()
            self.sorted_word = sorted(self.word)

    def match(self, list):
        matched = []

        for word in list:
            if self.sorted_word == sorted(word.lower()) and self.word != word:
                matched.append(word)
                
        return matched

    