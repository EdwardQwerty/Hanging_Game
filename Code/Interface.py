from GameClass import HangingGame

should_continue = True
#cycle "Do you want to play again or not?"
while should_continue == True:
      print("\nThis is a Hanging game\n")
      print("The PC will generates a random word and you need to \n"
            "guess it for a limited amount of tries")
      #make instance of HangingGame class, asking number of tries and checking input
      while True:
            try:
                  allowed_misses = int(input("How many tries do you want? (from 5 to 15) "))
                  current_game = HangingGame(allowed_misses)
                  break
            except:
                  print("\nThe number of tries could be from 5 to 15 only! Choose again!\n")
                  continue
      CurrentGame = HangingGame(allowed_misses)
      CurrentGame.word_generation()
      print("_________________________________________________________")
      print(f"The word cosist of {CurrentGame.word_len} letters")
      
      alphabet = {
            'а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к',
            'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц',
            'ч', 'ш', 'щ', 'ь', 'ы', 'ъ', 'э', 'ю', 'я'
      }
      
      #variable which define game status
      # 1 - game in progress
      # 2 - player guessed the word => win
      # 3 - player guessed the word letter by letter => win
      # 4 - tries are over => lose
      is_end_of_game = 1

      #main game cycle, checking player's guessed letter or whole word with checking player's input
      while is_end_of_game == 1:
      
            print("Try to guess a letter or whole word")
            CurrentGame.show_word()
            CurrentGame.used_letters()
            if CurrentGame.tries_remaining <= allowed_misses:
                  print(f"{CurrentGame.tries_remaining} tries remaining")
            elif CurrentGame.tries_remaining == 1:
                  print(f"This is your last try to guess word")

            while True:
                  player_guess = input("Enter the whole word or a letter ")
                  player_guess_lettered = {i for i in player_guess.lower()}
                  if player_guess_lettered.issubset(CurrentGame.used_letters_property):
                        print("This letter was used, try another.\n")
                        continue
                  elif len(player_guess) > 1 and len(player_guess) != CurrentGame.word_len:
                        print("Your word has more or less letters than guessed word has\n")
                        continue
                  elif player_guess_lettered.issubset(alphabet):
                        break
                  else:
                        print("The input is wrong. Use the letters only!\n")
                        continue
                        
            if len(player_guess_lettered) > 1:
                  print("Checking the guessed word")
                  does_word_win = [CurrentGame.checking_word(player_guess), CurrentGame.checking_remaining_tries()]
                  if all(does_word_win) == True:
                        print("Wow! You've guessed whole word!\n")
                        is_end_of_game = 2
                  else:
                        print("Sorry, your word is wrong")
                        continue
            else:
                  CurrentGame.checking_letter(player_guess)
                  print("_________________________________________________________")
                  if CurrentGame.checking_win() == True:
                        is_end_of_game = 3

            #state when you lose because of out of tries
            if CurrentGame.checking_remaining_tries() == False:
                  print("You have spent all tries")
                  is_end_of_game = 4
            else:
                  continue
      #defining other situations about wining and losing
      if is_end_of_game == 2 or is_end_of_game == 3:
            # 1 - game in progress
            # 2 - player guessed the word => win
            # 3 - player guessed the word letter by letter => win
            # 4 - tries are over => lose
            print("Сongratulations! You win!")
      
      elif is_end_of_game == 4:
            print("Sorry, you lose")

      #asking about repeat and checking input
      while True:
            should_continue_player = input("Do you want to play again? [y/n] ")
            if should_continue_player.lower() in ["y", "yes"]:
                  print("Starting the new game...")
                  print("_________________________________________________________")
                  break
            elif should_continue_player.lower() in ["n", "no"]:
                  print("Quiting the game")
                  should_continue = False
                  break
            else:
                  print("Your input is not correct. Try again.\n")