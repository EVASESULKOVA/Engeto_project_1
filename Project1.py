"""
projekt_1.py: first project from Engeto Online Python Akademie

author: Eva Sesulkovva
email: e.hrncarkova@gmail.com
discord: Eva H. #3953
"""

TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
         '''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
         '''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
         ]
line = 60 * "-"
separator = f"""
{line}
"""
dictionary_texts = dict(enumerate(TEXTS, start=1))
#  print(dictionary_texts.keys())

#  signing of a user

user_name = input("Enter your user name: ", )
password = input("Enter your password: ", )

#  control of the credentials of the user

registered_users = {
    "bob": 123,
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}

if user_name in registered_users.keys():
    print(f"{separator}Welcome on the portal, {user_name.capitalize()}\n")

    #  choose a text for analyses

    selected_text = input(
        "Please, select a text for the analyses. Use one of the following options: 1, 2, or 3: ")

    if selected_text.isnumeric() and (1 <= int(selected_text) <= 3):
        print(f"""The following text will be analyzed:
        '{dictionary_texts[int(selected_text)]}'""")

        #  division of the text to separated words + analyses of a selected text
        words_cleaned = list()
        words_separated = dictionary_texts[int(selected_text)].split()
        titlecase_words = list()
        uppercase_words = list()
        lowercase_words = list()
        numeric_string = list()
        sum_of_numbers = 0
        for word in words_separated:
            words_cleaned.append(word.strip(",.:;?!-\n"))
            if word.istitle():
                titlecase_words.append(word)
            if word.isalpha() and word.isupper():
                uppercase_words.append(word)
            if word.islower():
                lowercase_words.append(word)
            if word.isnumeric():
                numeric_string.append(word)
            if word.isnumeric():
                sum_of_numbers += int(word)
        print(f"{separator}Your chosen text includes {len(words_cleaned)} words.")
        print(f"Your chosen text includes {len(titlecase_words)} titlecase words.")
        print(f"Your chosen text includes {len(uppercase_words)} upper case words.")
        print(f"Your chosen texts includes {len(lowercase_words)} lower case words.")
        print(f"There are {len(numeric_string)} numeric strings in your chosen text.")
        print(f"The sum of all the numbers is {sum_of_numbers}.{separator}")

        #  analyses of the length of the words in the chosen text

        length_of_words = {}
        for word in words_cleaned:
            if len(word) not in length_of_words.keys():
                length_of_words[len(word)] = 1
            else:
                length_of_words[len(word)] += 1

        print(f"{'LENGTH': <10}|{'NUMBER': <10}|{'OCURRENCES': <50} {separator}")

        for key in sorted(length_of_words):
            print(f"{key: <10}|{length_of_words[key]: <10}|{(length_of_words[key]) * '*': <50}")


    else:
        print(f"For correct selection of the analysed text, please enter 1, 2 or 3. The entered value {selected_text} doesn't meet this condition")

else:
    print(f"The user {user_name.capitalize()} is not registered on the portal. Please, register")
