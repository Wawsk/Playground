
def add_prefix_un(word):
    return "un" + word

def make_word_groups(vocab_words):
    prefix = vocab_words[0]
    words = vocab_words[1:]
    prefixed_words = [prefix + word for word in words]
    return " :: ".join([prefix] + prefixed_words)

def remove_suffix_ness(word):
    if word.endswith("ness"):
        root = word[:-4]
        if root[-1] == 'i':
            return root[:-1] + 'y'
        else:
            return root
    return word

def adjective_to_verb(sentence, index):
    words = sentence.split()
    adjective = words[index]
    if adjective.endswith('.'):
        adjective = adjective[:-1]
    return adjective + 'en'

# Testing the functions
print()
print("'un' function:")
print(add_prefix_un("happy"))
print(add_prefix_un("manageable"))
print()
print("'suffix group' function:")
print(make_word_groups(['en', 'close', 'joy', 'lighten']))
print(make_word_groups(['pre', 'serve', 'dispose', 'position']))
print(make_word_groups(['auto', 'didactic', 'graph', 'mate']))
print(make_word_groups(['inter', 'twine', 'connected', 'dependent']))
print()
print("'ness' function:")
print(remove_suffix_ness("heaviness"))
print(remove_suffix_ness("sadness"))
print()
print("'en' function:")
print(adjective_to_verb('I need to make that bright.', -1))
print(adjective_to_verb('It got dark as the sun set.', 2))
print()
