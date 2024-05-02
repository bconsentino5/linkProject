from nltk.corpus import wordnet
import random
import requests

word_site = "https://www.mit.edu/~ecprice/wordlist.10000"
response = requests.get(word_site)
WORDS = response.content.split()

max_levels = 2
levels = {'1': ['mom', 'dad', 'parents'], 
          '2': ['bird', 'plane', 'fly'],
          '3': ['heel', 'bark', 'dog'],
          '4': ['tree', 'glue', 'stick'],
          '5': ['theme', 'swing', 'park'],
          '6': ['football', 'smartphone', 'screen'],
          '7': ['computer', 'door', 'key'],
          '8': ['technology', 'fruit', 'apple'],
          '9': ['trust', 'religion', 'faith'],
          '10': ['animal', 'pooper', 'party'],
          '11': ['wind', 'string', 'instrument'],
          '12': ['bowtie', 'wheel', 'pasta'],
          '13': ['dog', 'chair', 'sit'],
          '14': ['pumpkin', 'slipper', 'cinderella'],
          '15': ['cheese', 'color', 'wheel'],
          '16': ['shoe', 'spirit', 'soul'],
          '17': ['leap', 'amphibian', 'frog'],
          '18': ['slice', 'italy', 'pizza'],
          '19': ['heart', 'music', 'beat'],
          '20': ['dairy', 'nut', 'butter']}


class Link():
    def __init__(self):
        self.curr_level = 1
        self.lives = 5
        self.ans = ""
        self.called_levels = []

    def ans_len(self):
        return int(len(self.ans))
    
    def get_ans(self):
        return self.ans
    
    def get_curr_level(self):
        return self.curr_level
    
    def get_lives(self):
        return self.lives
    
    def set_lives(self, num):
        self.lives = num

    def get_words(self):
        temp = 0
        if self.curr_level > max_levels:
            while temp == 0:
                curr_word = random.choice(WORDS).decode('utf-8')
                if len(curr_word) < 8:
                    temp = 1

            synonyms = []
            syn1 = ""
            syn2 = ""

            for ss in wordnet.synsets(curr_word):
                for sim in ss.similar_tos():
                    synonyms.append(format(sim)[8:-7])

            while len(synonyms) < 2:
                temp = 0
                while temp == 0:
                    curr_word = random.choice(WORDS).decode('utf-8')
                    if len(curr_word) < 8:
                        temp = 1
                for ss in wordnet.synsets(curr_word):
                    for sim in ss.similar_tos():
                        synonyms.append(format(sim)[8:-7])

            while (syn1 == "") or (syn1 == curr_word):
                syn1 = random.choice(synonyms)
            while (syn2 == "") or (syn2 == curr_word) or (syn2 == syn1):
                syn2 = random.choice(synonyms)


            # levels.update({str(self.curr_level): [str(syn1), str(syn2), str(curr_word)]})
            
            print(f"Found levels: {str(syn1)}, {str(syn2)}, {str(curr_word)}")

            word1 = str(syn1) # words[0]
            word2 = str(syn2) # words[1]
            self.ans = str(curr_word) # words[2]
        else:
            lev = 0
            isin = False
            while isin == False:
                lev = random.randrange(1, 21)
                if lev in self.called_levels:
                    isin = False
                else:
                    isin = True
                    self.called_levels.append(lev)
            words = levels.get(str(lev))
            word1 = words[0]
            word2 = words[1]
            self.ans = words[2]
            print(self.called_levels)
        
        return word1, word2

    def check_guess(self, guess):
        if self.ans == guess:
            self.curr_level += 1
            return True
        else:
            return False
        
    def get_hint(self, ans_display):
        hint_string = ""
        hint_i = 0
        if len(ans_display) < self.ans_len():
            for i in range(self.ans_len()):
                ans_display += "_"
        for i in range(len(ans_display)):
            if ans_display[i] == "_":
                hint_i = i
        for i in range(self.ans_len()):
            if i == hint_i:
                hint_string += self.ans[i]
            else:
                hint_string += ans_display[i]
        ans_display = hint_string
        return ans_display
        # for i in range(self.ans_len()):
        #     if i == hint_i:
        #         if (hint_string[i] == "_"):
        #             hint_string += self.ans[i]
        #         else:
        #             hint_i = random.randrange(0, self.ans_len())
        #             i -= 1
        #     else:
        #         hint_string += "_"
            # still need to make it print the hints and figure out a way to get the hint word to stay the same for the whole round

