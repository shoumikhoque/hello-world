def is_formation_possible(words, target):
    word_set=set(words)
    for i in range(len(target)):
        if target[0:i] in word_set and target[i:len(target)] in word_set:
            return True
    return False



if __name__ == '__main__':
    words_list = [["flower", "moon", "plant", "sun", "star"],
                  ["sand", "water", "fly"],
                  ["paper", "pen", "book", "page", "note", "pencil"],
                  ["door", "light", "window", "balcony", "attic", "roof"],
                  ["bow", "rain"]]
    targets = ["sunflower", "waterfall", "notebook", "lighthouse", "rainbow"]

    for i in range(len(words_list)):
        print("Words in the table:", words_list[i])
        print("Target word:", targets[i])
        print("Found:", is_formation_possible(words_list[i], targets[i]))
        print("-" * 100)