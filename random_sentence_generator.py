import random
names = input("Enter your friends' names separated by comma (eg. Jane, Eyre) then press Enter ").split(", ")
places = input("Enter locations separated by comma (eg. the village, space) then press Enter ").split(", ")
adverbs = input("Enter adverbs separated by comma (eg. calmly, rapidly) then press Enter ").split(", ")
verbs = input("Enter actions separated by comma (eg. cooked, sang) then press Enter ").split(", ")
nouns = input("Enter nouns separated by comma (eg. ice cream, guitar) then press Enter ").split(", ")
details = input("Enter details separated by comma (eg. at the party, on the highway) then press Enter ").split(", ")


def randomize_words(words):
    return random.choice(words)


while True:

    random_name = randomize_words(names)
    random_place = randomize_words(places)
    random_verb = randomize_words(verbs)
    random_noun = randomize_words(nouns)
    random_adverb = randomize_words(adverbs)
    random_detail = randomize_words(details)

    print(f"{random_name} from {random_place} {random_adverb} {random_verb} {random_noun} {random_detail}")

    print("Enter (Y)es to generate another random sentence or (N)o to exit")

    valid_input = False

    while not valid_input:
        user_input = input().lower()

        if user_input == "y":
            valid_input = True
        elif user_input == "n":
            exit()
        else:
            print("Invalid input! Please enter again.")
