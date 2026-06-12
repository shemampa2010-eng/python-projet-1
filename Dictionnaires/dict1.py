

notes  = {
    "maths": 15,
    "francais": 12,
    "anglais": 18
}
nb_notes=(len(notes))
liste = list(notes.values())
print(liste)
total = sum(liste)

moyenne = sum (liste) / len(liste)
print (moyenne)