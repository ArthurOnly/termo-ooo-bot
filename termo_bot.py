import string
from threading import Thread

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
        self.find_start_thread()
        return self.result_set

    # improve performance on search
    def find_start_thread(self):
        word = ""

        def start_find_thread(word):
            self.find_rec(word)
            print("Finished for "+word)

        threads = []
        for i in range(25):
            letter = self.alph[i]
            thread = Thread(target=start_find_thread, args=(word+letter))
            threads.append(thread)

        # Start them all
        for thread in threads:
            thread.start()

        # Wait for all to complete
        for thread in threads:
            thread.join()

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
        if len(word) in self.contains_exact.keys():
            word += self.contains_exact[len(word)]
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

    def _letters_in_position_words(self, words):
        result = {0: {}, 1: {}, 2: {}, 3: {}, 4: {}}
        for word in words:
            for index, letter in enumerate(word):
                if letter in result[index].keys():
                    result[index][letter] += 1
                else:
                    result[index][letter] = 1

        return result

    def get_words_sugestion(self):
        words_score = []
        letters_position = self._letters_in_position_words(self.result_set)
        for word in self.result_set:
            score = self._score_of_word(word, letters_position)
            words_score.append((score, word))
        return sorted(words_score)


    def _score_of_word(self, word, letters_in_positions):
        word_score = 0
        for index, letter in enumerate(word):
            if index in self.contains_exact.keys():
                continue
            else:
                if word.count(letter) > 1:
                    word_score += letters_in_positions[index][letter] / 2
                else:
                    word_score += letters_in_positions[index][letter]
        return word_score
            

    def last_letter_is_valid(self, word):
        if len(word) > 0 and word[-1] in self.no_contains:
            return False
        if len(word) - 1 in self.no_contains_exact.keys() and word[-1] in self.no_contains_exact[len(word) - 1]:
            return False

        valid = False
        for fword in self.words:
            if fword.startswith(word):
                valid = True
                break
        if not valid:
            return False

        return True
                
    
