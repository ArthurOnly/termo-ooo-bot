import string

class TermoBot:
    contains = []
    no_contains = []
    contains_exact = {}
    no_contains_exact = {}
    words = []
    alph = list(string.ascii_lowercase)
    result_set = []

    def __init__(self, words_file):
        self.words = words_file.readlines()

    def add_contains(self, letter):
        self.contains.append(letter)

    def add_no_contains(self, letter):
        self.no_contains.append(letter)

    def add_contains_exact(self, letter, position):
        self.contains_exact[position] = letter

    def add_no_contains_exact(self, letter, position):
        if position not in self.no_contains_exact.keys():
            self.no_contains_exact[position] = [letter]
        else:
            self.no_contains_exact[position].append(letter)

    def reset(self):
        self.contains = []
        self.no_contains = []
        self.contains_exact = {}
        self.no_contains_exact = {}

    def find(self):
        self.result_set = []
        self.find_rec("")
        return self.result_set

    def find_rec(self, word, results=[]):
        # reject
        if not self.last_letter_is_valid(word):
            return

        # accept
        if len(word) == 5:
            is_valid = self.validate_word(word)
            if is_valid:
                self.result_set.append(word)
                return word
            return
            
        self.next_letter(word)

    def next_letter(self, word):
        if len(word)+1 in self.contains_exact.keys():
            word += self.contains_exact[len(word)+1]
            self.find_rec(word)
            word = word[:-1]
        else:
            for i in range(25):
                word += self.alph[i]
                self.find_rec(word)
                word = word[:-1]

    def validate_word(self, word):
        for letter in self.contains:
            if letter not in word:
                return False

        if word+"\n" not in self.words:
            return False

        return True

    def last_letter_is_valid(self, word):
        if len(word) > 0 and word[-1] in self.no_contains:
            return False
        if len(word) in self.no_contains_exact and word[-1] in self.no_contains_exact[len(word)]:
            return False
        return True
                
    
