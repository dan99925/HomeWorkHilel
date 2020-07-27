
words = {

   'apple': ['malum', 'pomum', 'popula'],

   'fruit': ['baca', 'bacca', 'popum'],

   'punishment': ['malum', 'multa']

}
trans_to_words = {}

for word in words:
    for translate in words[word]:
        if translate in trans_to_words:
            trans_to_words[translate].append(word)
        else:
            trans_to_words[translate] = [word]

print(trans_to_words)