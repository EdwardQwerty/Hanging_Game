import random


class HangingGame:
    def __init__(self, allowed_misses: int = 15):
        
        if allowed_misses < 5 or allowed_misses > 15:
            raise ValueError('Allowed misses should be more than 5 and less than 15')

        self.__allowed_misses = allowed_misses
        self.__word = ""
        self.__lettered_word = []
        self.__showing_word = []
        self.__tries_passed = 0
        self.__used_letters = set()

    #randomly generating word using dictionfry file
    def word_generation(self):
        path_to_file = "Q:\\Code Prog\\Projects\\Hanging_game_2\\venv\\Code\\Dictionary_RUS.txt"
        words = []
        with open (path_to_file, "r", encoding = "utf-8") as Dict:
            for line in Dict:
                words.append(line.strip())
        self.__word = words[random.randint(0, len(words))]
        self.__lettered_word = [i for i in self.__word]
        self.__showing_word = [" _" for i in self.__lettered_word]
        return self.__word
    
    #method to showing "_" for every letter of generated word
    def show_word(self):
        for i in range(len(self.__showing_word)):
            print(self.__showing_word[i], end = "")
        print()
        
    #method to checking player's input letter
    def checking_letter(self, player_guess):
        self.__used_letters.add(player_guess)
        if player_guess not in self.__lettered_word:
            self.__tries_passed += 1
            print('\nSorry, there is no this letter\n')
        else:
            print('\nYour guess is right!\n')
            for i in range(len(self.__lettered_word)):
                if self.__lettered_word[i] == player_guess:
                    self.__showing_word[i] = player_guess

    #method to checking player's win when they input whole word
    def checking_win(self):
        if (self.__allowed_misses - self.__tries_passed) >= 0 \
                and (self.__showing_word == self.__lettered_word):
            return True
        else:
            return False

    #method to checking player's input word
    def checking_word(self, player_guess):
        if player_guess.lower() == self.__word:
            return True
        else:
            self.__tries_passed += 1
            return False

    #method to check that player still have tries
    def checking_remaining_tries(self):
        if (self.__allowed_misses - self.__tries_passed) > 0:
            return True
        else:
            return False
    
    #method to show letters already used by player
    def used_letters(self):
        if self.__used_letters == set():
            print("You don't use any letter yet")
        else:
            print("Your used letters are: ", end="")
            used_lettres_list = list(self.__used_letters)
            used_lettres_list.sort()
            for i in range(len(used_lettres_list)):
                print(used_lettres_list[i], end="  ")
            print()


    @property
    def word_len(self):
        return len(self.__lettered_word)

    @property
    def tries_remaining(self):
        return self.__allowed_misses - self.__tries_passed

    @property
    def used_letters_property(self):
        return self.__used_letters

    @property
    def generated_word(self):
        return self.__word