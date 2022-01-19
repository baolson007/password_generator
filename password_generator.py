import random
import urllib.request, urllib.error
import string

# generate password between 8-15 chars, with 1 capital letter,
# 1 special char. User can specify wanting to use 2 words in password
# word source is moby dick from project gutenberg


class PasswordGenerator:
    global full_word_dict

    def __init__(self, num_words=2):
        special_chars = [
            '~',
            '`',
            '!',
            '@',
            '#',
            '$',
            '%',
            '^',
            '&',
            '*',
            '(',
            ')',
            '_',
            '-',
            '+',
            '=',
            '{',
            '[',
            '}',
            ']',
            '|',
            ':',
            ';',
            '\"',
            '\'',
            '<',
            '>',
            '.',
            '?',
            '/']

        self.generate_words()
        self.word_list = self.select_word(num_words)
        self.number = (random.randint(0, 100))
        self.special_char = random.choice(special_chars)
        self.password = self.generate_pwd(
            self.word_list, self.number, self.special_char)

    def __repr__(self):
        return self.password

    def generate_words(self):
        try:
            with urllib.request.urlopen('https://www.powermobydick.com/Moby001.html') as response: #https://www.gutenberg.org/files/2701/2701-0.txt') as response:
                html = response.read().decode('utf-8')
    
            full_word_list = set(html.split())
            indexes = list(range(len(full_word_list)))
            global full_word_dict
            full_word_dict = dict(zip(indexes, full_word_list))
        except Exception as e:
            raise SystemExit(e, "Unable to connect with Project Gutenberg at this time, please try again later")

    def select_word(self, num_words):

        max_idx = len(full_word_dict) - 1
        words = []

        for num in range(num_words):
            rand_idx = random.randint(0, max_idx)
            word = full_word_dict[rand_idx]
            
            #while selection is too short or contains extra
            #punctuation, choose new word
            while self.contains_punctuation(word) or len(word) < 4:
                rand_idx = random.randint(0, max_idx)
                word = full_word_dict[rand_idx]
            words.append(word)
        return words
        
    def contains_punctuation(self, word):
        for c in word:
            if c in string.punctuation or c == '—':
                return True
        return False

    def generate_pwd(self, word, number, special_char):
        num_words_in_pwd = len(self.word_list)
        word_to_modify = None
        remaining_word = None

        if num_words_in_pwd == 2:
            word_choice_idx = random.choice([0, 1])
            word_to_modify = self.word_list[word_choice_idx]
            if word_choice_idx == 0:
                remaining_word = self.word_list[1]
            else:
                remaining_word = self.word_list[0]
        else:
            word_to_modify = self.word_list[0]

        len_word = len(word_to_modify)

        capital_idx = random.choice(list(range(len_word)))

        modified_word = ''

        for i, c in enumerate(word_to_modify):

            if i == capital_idx:
                modified_word += modified_word.join(c.upper())
            else:
                modified_word += modified_word.join(c)

        pwd_list = [modified_word, str(number), special_char]

        if remaining_word:
            pwd_list.append(remaining_word)

        random.shuffle(pwd_list)
        return "".join(pwd_list)


#for _ in range(3):
#    pwd = PasswordGenerator()
#    print(pwd)
