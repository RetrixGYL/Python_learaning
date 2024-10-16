def single_root_words(root_word, *other_words):
    same_words = []
    print(f"Слово для подбора {root_word}")
    print(f"Список слов: {other_words}")
    for i in list(other_words):
        if root_word.lower() in i.lower():
            same_words.append(i)
        elif i.lower() in root_word.lower():
            same_words.append(i)
        else:
            continue
    print(f"Однокоренные слова к слову {root_word}: {same_words}")
single_root_words("tic", "ricTic", "betica", "jorka", "ticapar")
# single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
# single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')