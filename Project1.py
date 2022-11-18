"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Eva Hrncarkova
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
cara = 60 * "-"
oddelovac = f"""
{cara}
"""
slovnik_textu = dict(enumerate(TEXTS, start=1))
#  print(slovnik_textu.keys())

#  TODO zadejte prihlasovaci udaje

uzivatelske_jmeno = input("Zadejte sve uzivatelske jmeno: ", )
heslo = input("Zadejte sve uzivatelske heslo: ", )

#  TODO je uzivatel mezi registrovanymi uzivateli? Pokud ano, pozdravit

registrovani_uzivatele = {
    "bob": 123,
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}

if uzivatelske_jmeno in registrovani_uzivatele.keys():
    print(f"Vitej na nasem portale, {uzivatelske_jmeno.capitalize()}\n")
    #  TODO uživatel si vybere ze 3 textu
    vybrany_text = input(
        "Vyberte si jeden z textu k analyze. Pro spravne zvoleni textu, napiste cislici 1, 2, nebo 3: ")
    #  print(type(vybrany_text))

    if vybrany_text.isnumeric() and (1 <= int(vybrany_text) <= 3):
        print(f"""Budeme analyzovat tento text: 
        '{slovnik_textu[int(vybrany_text)]}'""")

        #  TODO analyza vybraneho textu - rozdeleni textu na jednotliva slova
        vycistena_slova = list()
        jednotliva_slova = slovnik_textu[int(vybrany_text)].split()

        for slovo in jednotliva_slova:
            vycistena_slova.append(slovo.strip(",.:;?!-\n"))
        #  print(vycistena_slova)

        #  TODO spocitam pocet slov ve vybranem textu
        print(f"{oddelovac}Vami vybrany text obsahuje {len(vycistena_slova)} slov.")

        #  TODO spocitam pocet slov zacinajicich velkym pismenem
        slova_s_velkym = list()
        for slovo in vycistena_slova:
            if slovo.istitle():
                slova_s_velkym.append(slovo)
        print(f"Pocet slov zacinajicich velkym pismenem je {len(slova_s_velkym)} slov.")

        #  TODO spocitam pocet slov psanych velkymi pismeny
        slova_velce = list()
        for slovo in vycistena_slova:
            if slovo.isalpha() and slovo.isupper():
                slova_velce.append(slovo)
        print(f"Pocet slov psanych velkymi pismeny je {len(slova_velce)} slov.")

        #  TODO spocitam pocet slov psanych malymi pismeny
        slova_s_velkym = list()
        for slovo in vycistena_slova:
            if slovo.islower():
                slova_s_velkym.append(slovo)
        print(f"Pocet slov psanych malymi pismeny je {len(slova_s_velkym)} slov.")

        #  TODO spocitam pocet cisel (ne cifer)
        slova_jako_cisla = list()
        for slovo in vycistena_slova:
            if slovo.isnumeric():
                slova_jako_cisla.append(slovo)
        print(f"Pocet cisel v textu je {len(slova_jako_cisla)}.")

        #  TODO spocitam sumu cisel (ne cifer)
        suma_cisel = 0
        for slovo in vycistena_slova:
            if slovo.isnumeric():
                suma_cisel += int(slovo)
        print(f"Suma cisel v textu je {suma_cisel}.")

        #  TODO četnost různých délek slov v textu
        delka_1 = 0
        delka_2 = 0
        delka_3 = 0
        delka_4 = 0
        delka_5 = 0
        delka_6 = 0
        delka_7 = 0
        delka_8 = 0
        delka_9 = 0
        delka_10 = 0
        delka_11 = 0
        delka_12 = 0
        delka_13 = 0
        delka_14 = 0
        delka_15 = 0
        delka_16 = 0
        for slovo in vycistena_slova:
            if len(slovo) == 1:
                delka_1 += 1
            elif len(slovo) == 2:
                delka_2 += 1
            elif len(slovo) == 3:
                delka_3 += 1
            elif len(slovo) == 4:
                delka_4 += 1
            elif len(slovo) == 5:
                delka_5 += 1
            elif len(slovo) == 6:
                delka_6 += 1
            elif len(slovo) == 7:
                delka_7 += 1
            elif len(slovo) == 8:
                delka_8 += 1
            elif len(slovo) == 9:
                delka_9 += 1
            elif len(slovo) == 10:
                delka_10 += 1
            elif len(slovo) == 11:
                delka_11 += 1
            elif len(slovo) == 12:
                delka_12 += 1
            elif len(slovo) == 13:
                delka_13 += 1
            elif len(slovo) == 14:
                delka_14 += 1
            elif len(slovo) == 15:
                delka_15 += 1
            elif len(slovo) == 16:
                delka_16 += 1
        print(f"""
        LEN | OCCURENCIES          | NR.
        1   | {(delka_1 * "*"):<20} | {delka_1}
        2   | {(delka_2 * "*"):<20} | {delka_2}
        3   | {(delka_3 * "*"):<20} | {delka_3}
        4   | {(delka_4 * "*"):<20} | {delka_4}
        5   | {(delka_5 * "*"):<20} | {delka_5}
        6   | {(delka_6 * "*"):<20} | {delka_6}
        7   | {(delka_7 * "*"):<20} | {delka_7}
        8   | {(delka_8 * "*"):<20} | {delka_8}
        9   | {(delka_9 * "*"):<20} | {delka_9}
        10  | {(delka_10 * "*"):<20} | {delka_10}
        11  | {(delka_11 * "*"):<20} | {delka_11}
        12  | {(delka_12 * "*"):<20} | {delka_12}
        13  | {(delka_13 * "*"):<20} | {delka_13}  
        14  | {(delka_14 * "*"):<20} | {delka_14}
        15  | {(delka_15 * "*"):<20} | {delka_15}
        16  | {(delka_16 * "*"):<20} | {delka_16}                
  
              """)
    else:
        print("Pro spravne zvoleni textu, napiste cislici 1, 2, nebo 3. Vami zvolena hodnota neodpovida teto podmince.")

else:
    print(f"Uzivatel {uzivatelske_jmeno.capitalize()} neni registrovany. Pred pouzitim portalu se, prosim, registrujte")
