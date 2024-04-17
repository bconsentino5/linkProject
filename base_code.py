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
          '12': ['dog', 'chair', 'sit'],
          '14': [],
          '15': [],
          '16': [],
          '17': [],
          '18': [],
          '19': [],
          '20': []}

curr_level = 1

for i in range(len(levels)):
  lives = 5
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
      lives -= 1
      print(f'incorrect. you have {lives} lives left.')
      print()
      # checking if they can continue to play
      if lives == 0:
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
    