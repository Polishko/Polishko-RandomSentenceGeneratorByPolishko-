import random
names = ["Genc", "Nalan", "Tanya", "Elena", "Leman", "Erkin", "Sultan", "Taner", "Ozge"]
places = ["Istanbul", "space", "the village", "the big city", "the sea side", "Hollywood", "the block", "the cave"]
verbs = ["ate", "slept", "cried", "went", "swam", "heard", "cooked", "drove", "read", "played", "walked", "farted"]
nouns = ["icecream", "beach", "mercedes", "guitar", "story", "gamble", "bacon", "cat", "dog", "strange sounds", "sofa", "beans"]
adverbs = ["sleepily", "ferociously", "crazily", "calmly", "surprisingly", "interestingly", "playfully", "sadly", "awfully"]
details = ["at the cafe", "in the barn", "in public", "on the highway", "at work", "at their grandma's", "on the balcony"]


def randomize_words(words):
    return random.choice(words)


initial_input = input("Press [Enter] to generate a random sentence")

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
