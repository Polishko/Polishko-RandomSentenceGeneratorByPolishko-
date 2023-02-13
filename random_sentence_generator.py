import random


def randomize_words(words):
    return random.choice(words)


while True:

    names = input("Enter your friends' names separated by comma (eg. Jane, Eyre) then press Enter ").split(", ")
    print()
    places = input("Enter locations separated by comma (eg. the village, space) then press Enter ").split(", ")
    print()
    adverbs = input("Enter adverbs separated by comma (eg. calmly, rapidly) then press Enter ").split(", ")
    print()
    verbs = input("Enter actions separated by comma (eg. cooked, sang) then press Enter ").split(", ")
    print()
    nouns = input("Enter nouns separated by comma (eg. ice cream, guitar) then press Enter ").split(", ")
    print()
    details = input("Enter details separated by comma (eg. at the party, on the highway) then press Enter ").split(", ")
    print()

    new_game = False

    while not new_game:

        random_name = randomize_words(names)
        random_place = randomize_words(places)
        random_verb = randomize_words(verbs)
        random_noun = randomize_words(nouns)
        random_adverb = randomize_words(adverbs)
        random_detail = randomize_words(details)

        print(f"{random_name} from {random_place} {random_adverb} {random_verb} {random_noun} {random_detail}")
        print()

        print("Enter (Y)es to generate another random sentence, (R)estart to enter new input or (N)o to exit")
        print()

        valid_input = False

        while not valid_input:
            user_input = input().lower()

            if user_input == "y" or user_input == "yes":
                valid_input = True
            elif user_input == "n" or user_input == "no":
                quit()
            elif user_input == "r" or user_input == "restart":
                new_game = True
                break
            else:
                print("Invalid input! Please enter again.")
                print()
