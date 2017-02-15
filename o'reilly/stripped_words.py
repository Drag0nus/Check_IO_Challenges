VOWELS = "AEIOUY"
CONSONANTS = "BCDFGHJKLMNPQRSTVWXZ"
SEPARATORS = ".,?"


def check_io(text):
    result = 0

    # Splitting text
    print("\nText: " + text)
    for separator in SEPARATORS:
        text = text.replace(separator, " ")
    words = text.split()

    # Checking each word
    for word in words:
        if len(word) < 2:
            continue

        i = 0
        while i < len(word) - 1:
            if VOWELS.count(word[i].upper()) == 0 and CONSONANTS.count(word[i].upper()) == 0 or \
                            VOWELS.count(word[i].upper()) == VOWELS.count(word[i + 1].upper()) or \
                            CONSONANTS.count(word[i].upper()) == CONSONANTS.count(word[i + 1].upper()):
                print("Bad word: " + word + " - Reason: " + word[i] + word[i + 1])
                i = len(word)
            i += 1
            if i == len(word) - 1:
                print("Correct word: " + word)
                result += 1

    print("Result: " + str(result))
    return result


#
# #These "asserts" using only for self-checking and not necessary for auto-testing
# if __name__ == '__main__':
#     assert check_io("My name is ...") == 3, "All words are striped"
#     assert check_io("Hello world") == 0, "No one"
#     assert check_io("A quantity of striped words.") == 1, "Only of"
#     assert check_io("Dog,cat,mouse,bird.Human.") == 3, "Dog, cat and human"

check_io("My name is ...")
check_io("A quantity of striped words.")
check_io("Hello world") == 0
