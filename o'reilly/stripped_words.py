VOWELS = "AEIOUY"
CONSONANTS = "BCDFGHJKLMNPQRSTVWXZ"
SEPARATORS = ".,?"


def check_io(text):
    result = 0

    # Splitting text
    print("\nText: " + text)
    for separator in SEPARATORS:
        text = text.replace(separator, " ")
    words = text.upper().split()

    for word in words:
        if len(word) < 2:
            continue

        odd_letters = []
        even_letters = []

        for i in range(0, len(word)):
            if i % 2 == 0:
                even_letters.append(word[i])
            elif i % 2 != 0:
                odd_letters.append(word[i])

        if even_letters and odd_letters:
            if all(v in VOWELS for v in even_letters) and all(c in CONSONANTS for c in odd_letters) or \
                        all(v in CONSONANTS for v in even_letters) and all(c in VOWELS for c in odd_letters):
                result += 1
    print(result)
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
check_io("Dog,cat,mouse,bird.Human.")
