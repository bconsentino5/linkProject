# ---------------------------------------------------------------#




from nltk.corpus import wordnet
import random
import requests

word_site = "https://www.mit.edu/~ecprice/wordlist.10000"

response = requests.get(word_site)
WORDS = response.content.split()

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

curr_level = 1
lives = 5

while lives != 0:
  if lives <= 0:
    break
  else:
    # initialize level
    lives = 5
    print(f'-- LEVEL {curr_level} --')
    print()
    words = levels.get(str(curr_level))
    print(f'{words[0]}     {words[1]}')
    print()
    print(f'LINK is {len(words[2])} characters long:')
    print()
    ans = input()

    # incorrect
    while ans != words[2]:
      if len(ans) != len(words[2]):
         print(f'answer is the wrong length. LINK is {len(words[2])} characters long. try again:')
         ans = input()
      else:
        lives -= 1
        for i in range(len(words[2])):
          if words[2][i] == ans[i]:
              print(words[2][i], end="")
          else:
              print("_", end="")
        print()
        print(f'incorrect. you have {lives} lives left.')
        print()
        # checking if they can continue to play
        if lives == 0:
          print(f'>> the LINK was {words[2]} <<')
          print('*** game over ***')
          break
        else:
          ans = input()

    # correct   
    if ans == words[2]:
      print()
      print("*** correct! onto the next level ***")
      print()
      curr_level += 1
      temp = 0
      if curr_level > 20:
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

        levels.update({str(curr_level): [str(syn1), str(syn2), str(curr_word)]})
          

    