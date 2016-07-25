"""Dictionaries Assessment

**IMPORTANT:** these problems are meant to be solved using
dictionaries and sets.
"""

def count_words(phrase):
    """Count unique words in a string.

    This function should take a single string and return a dictionary
    that has all of the distinct words as keys, and the number of
    times that word appears in the string as values.

    For example::

        >>> print_dict(count_words("each word appears once"))
        {'appears': 1, 'each': 1, 'once': 1, 'word': 1}

    Words that appear more than once should be counted each time::

        >>> print_dict(count_words("rose is a rose is a rose"))
        {'a': 2, 'is': 2, 'rose': 3}

    It's fine to consider punctuation part of a word (e.g., a comma
    at the end of a word can be counted as part of that word) and
    to consider differently-capitalized words as different::

        >>> print_dict(count_words("Porcupine see, porcupine do."))
        {'Porcupine': 1, 'do.': 1, 'porcupine': 1, 'see,': 1}
    """

    #split the string into a list using " "
    words = phrase.split(" ")

    #empty dictionary that will contain the word with how many times it appears
    unique_words = {}

    #iterate through list of words
    for word in words:
        #either add word with value to dictionary or increase amount
        unique_words[word] = unique_words.get(word, 0) + 1

    return unique_words


def get_melon_price(melon_name):
    """Given a melon name, return the price of the melon
    
    Here are a list of melon names and prices:
    Watermelon 2.95
    Cantaloupe 2.50
    Musk 3.25
    Christmas 14.25 
    (it was a bad year for Christmas melons -- supply is low!)

        >>> get_melon_price('Watermelon')
        2.95

        >>> get_melon_price('Musk')
        3.25
        
        >>> get_melon_price('Tomato')
        'No price found'
    """
    #dictionary containing the melon names as keys with the price as values
    melons = {
            "Watermelon":2.95,
            "Cantaloupe":2.50,
            "Musk": 3.25,
            "Christmas": 14.25
    }

    print melons.get(melon_name, "'No price found'")


def word_length_sorted(words):
    """Return list of word-lengths and words.

    Given a list of words, return a list of tuples, ordered by
    word-length. Each tuple should have two items --- a number that
    is a word-length, and the list of words of that word length.

    In addition to ordering the list by word length, order each
    sub-list of words alphabetically.

    For example::

        >>> word_length_sorted(["ok", "an", "apple", "a", "day"])
        [(1, ['a']), (2, ['an', 'ok']), (3, ['day']), (5, ['apple'])]
    """

    #create an empty dictionary that will contain the letter length and words
    counts_words = {}

    #iterate through the words in the list
    for word in words:
        #save letter length count as a variable
        letter_count = len(word)
        #if letter count key doesn't exist, add key with empty list; otherwise
        #add the new word to the current list
        counts_words[letter_count] = counts_words.get(letter_count, [])
        counts_words[letter_count].append(word)

    #create an empty list that will be returned
    counts_words_list = []

    #iterate through the key, value in the dictionary
    for key, value in counts_words.iteritems():
        #sort the values of each key
        counts_words[key] = value.sort()
        #add the key and value as a tuple to the list
        counts_words_list.append((key, value))

    #sort the tuples in the list
    counts_words_list.sort()

    return counts_words_list


def translate_to_pirate_talk(phrase):
    """Translate phrase to pirate talk.

    Given a phrase, translate each word to the Pirate-speak
    equivalent. Words that cannot be translated into Pirate-speak
    should pass through unchanged. Return the resulting sentence.

    Here's a table of English to Pirate translations:

    ----------  ----------------
    English     Pirate
    ----------  ----------------
    sir         matey
    hotel       fleabag inn
    student     swabbie
    man         matey
    professor   foul blaggart
    restaurant  galley
    your        yer
    excuse      arr
    students    swabbies
    are         be
    restroom    head
    my          me
    is          be
    ----------  ----------------

    For example::

        >>> translate_to_pirate_talk("my student is not a man")
        'me swabbie be not a matey'

    You should treat words with punctuation as if they were different
    words::

        >>> translate_to_pirate_talk("my student is not a man!")
        'me swabbie be not a man!'
    """
    #create a dictionary with the pirate translation in key and value
    pirate_translation = {
                    "sir":"matey",
                    "hotel":"fleabag inn",
                    "student":"swabbie",
                    "man":"matey",
                    "professor":"foul blaggart",
                    "restaurant":"galley",
                    "your":"yer",
                    "excuse":"arr",
                    "students":"swabbies",
                    "are":"be",
                    "restroom":"head",
                    "my":"me",
                    "is":"be"
    }

    #split the phrase into a list
    phrase_list = phrase.split(" ")

    #iterate through each word in the list
    for word in phrase_list:
        #if the word exists in the keys of the dictionary
        if word in pirate_translation.keys():
            #replace the word with the pirate dictionary value
            phrase = phrase.replace(word, pirate_translation[word])

    return phrase


def kids_game(names):
    """Play a kids' word chain game.

    Given a list of names, like::

      bagon baltoy yamask starly nosepass kalob nicky

    Do the following:

    1. Always start with the first word ("bagon", in this example).

    2. Add it to the results.

    3. Use the last letter of that word to look for the next word.
       Since "bagon" ends with n, find the *first* word starting
       with "n" in our list --- in this case, "nosepass".

    4. Add "nosepass" to the results, and continue. Once a word has
       been used, it can't be used again --- so we'll never get to
       use "bagon" or "nosepass" a second time.

    5. When you can't find an unused word to use, you're done!
       Return the list of output words.

    For example::

        >>> kids_game(["bagon", "baltoy", "yamask", "starly",
        ...            "nosepass", "kalob", "nicky", "booger"])
        ['bagon', 'nosepass', 'starly', 'yamask', 'kalob', 'baltoy']

    (After "baltoy", there are no more y-words, so we end, even
    though "nicky" and "booger" weren't used.)

    This is a tricky problem. In particular, think about how using
    a dictionary (with the super-fast lookup they provide) can help;
    good solutions here will definitely require a dictionary.
    """

    results = [names[0]]

    changing_names_list = names[1:]

    first_letter_to_words = {}

    for name in changing_names_list:

      if name[0] not in first_letter_to_words:
        first_letter_to_words[name[0]] = [name]
      else:
        first_letter_to_words[name[0]].append(name)

    while True:

      last_character = results[-1][-1]

      if not first_letter_to_words.get(last_character):
        break
      else:
        word = first_letter_to_words[last_character].pop(0)
        results.append(word)

    return results

#####################################################################
# You can ignore everything below this.

def print_dict(d):
    # This method is used to print dictionaries in key-alphabetical
    # order, and is only for our doctests. You can ignore it.
    if isinstance(d, dict):
        print "{" + ", ".join(
            "%r: %r" % (k, d[k]) for k in sorted(d)) + "}"
    else:
        print d


def sort_pairs(l):
    # Print sorted list of pairs where the pairs are sorted. This is
    # used only for documentation tests. You can ignore it.
    return sorted(sorted(pair) for pair in l)


if __name__ == "__main__":
    print
    import doctest
    if doctest.testmod().failed == 0:
        print "*** ALL TESTS PASSED ***"
    print
