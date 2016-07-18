"""Dictionaries Practice

**IMPORTANT:** these problems are meant to be solved using
dictionaries and sets.
"""


def without_duplicates(words):
    """Given a list of words, return list with duplicates removed.

    For example::

        >>> sorted(without_duplicates(
        ...     ["rose", "is", "a", "rose", "is", "a", "rose"]))
        ['a', 'is', 'rose']

    You should treat differently-capitalized words as different:

        >>> sorted(without_duplicates(
        ...     ["Rose", "is", "a", "rose", "is", "a", "rose"]))
        ['Rose', 'a', 'is', 'rose']

        An empty list should return an empty list::

        >>> sorted(without_duplicates(
        ...     []))
        []

    The function should work for a list containing integers::

        >>> sorted(without_duplicates([111111, 2, 33333, 2]))
        [2, 33333, 111111]
    """
    #changing type of inputted list into a set, saving it to new variable
    unique_words = set(words)
    #changing type from set to list
    words = list(unique_words)
    #returning a list of unique words
    return words


def find_unique_common_items(items1, items2):
    """Produce the set of *unique* common items in two lists.

    Given two lists, return a list of the *unique* common items
    shared between the lists.

    **IMPORTANT**: you may not use `'if ___ in ___``
    or the method `list.index()`.

    This should find [1, 2]::

        >>> sorted(find_unique_common_items([1, 2, 3, 4], [2, 1]))
        [1, 2]

    However, now we only want unique items, so for these lists,
    don't show more than 1 or 2 once::

        >>> sorted(find_unique_common_items([3, 2, 1], [1, 1, 2, 2]))
        [1, 2]

    The elements should not be treated as duplicates if they are
    different data types::

        >>> sorted(find_unique_common_items(["2", "1", 2], [2, 1]))
        [2]
    """
    #make the first list into a set so there's only unique items
    first_list = set(items1)
    #make the second list into a set so there's only unique
    second_list = set(items2)

    #find the common items between first and second list sets
    common_items = first_list & second_list
    #turn the common_items from a set into a list
    common_items_list = list(common_items)

    return common_items_list

def get_sum_zero_pairs(numbers):
    """Given list of numbers, return list of pair summing to 0.

    Given a list of numbers, add up each individual pair of numbers.
    Return a list of each pair of numbers that adds up to 0.

    For example::

        >>> sort_pairs(get_sum_zero_pairs([1, 2, 3, -2, -1]))
        [[-2, 2], [-1, 1]]

        >>> sort_pairs(get_sum_zero_pairs([3, -3, 2, 1, -2, -1]))
        [[-3, 3], [-2, 2], [-1, 1]]

    This should always be a unique list, even if there are
    duplicates in the input list::

        >>> sort_pairs(get_sum_zero_pairs([1, 2, 3, -2, -1, 1, 1]))
        [[-2, 2], [-1, 1]]

    Of course, if there are one or more zeros to pair together,
    that's fine, too (even a single zero can pair with itself)::

        >>> sort_pairs(get_sum_zero_pairs([1, 3, -1, 1, 1, 0]))
        [[-1, 1], [0, 0]]
    """

    #turn list into a set to get unique numbers
    unique_numbers = set(numbers)
    #turn set back into a list
    numbers = list(unique_numbers)

    #sort the list of numbers
    numbers.sort()

    #create an empty list that will contain the pairs of numbers
    pairs_list = []

    #using indexing, compare the first number to the rest of the numbers in the
    #list
    for i in range(len(numbers)):
        #create a list of the rest of the numbers after the numbers in the list
        rest_of_numbers = numbers[i+1:]

        #if a number is 0, add [0,0] to the pairs list
        if numbers[i] == 0:
            pairs_list.append([0,0])
        #otherwise, go through the entire list and see if the number + another
        #number in the list is equal to 0
        else:
            for index in range(len(rest_of_numbers)):
                if numbers[i] + rest_of_numbers[index] == 0:
                    #if = 0, add the two numbers as a list to the pairs_list
                    pairs_list.append([numbers[i], rest_of_numbers[index]])

    return pairs_list


def top_chars(phrase):
    """Find most common character(s) in string.

    Given an input string, return a list of character(s) which
    appear(s) the most the input string.

    If there is a tie, the order of the characters in the returned
    list should be alphabetical.

    For example::

        >>> top_chars("The rain in spain stays mainly in the plain.")
        ['i', 'n']

    If there is not a tie, simply return a list with one item.

    For example::

        >>> top_chars("Shake it off, shake it off.")
        ['f']

    Do not count spaces, but count all other characters.

    """

    #eliminate the spaces in the string using replace method
    phrase = phrase.replace(" ", "")
    #make phrase all lower case letters
    phrase = phrase.lower()

    #create an empty dictionary that will contain the letters and their counts
    letter_count = {}

    #use a loop, use get function, if doesn't exist add letter:1 otherwise += 1
    for letter in phrase:
        letter_count[letter] = letter_count.get(letter, 0) + 1

    #an empty list that will contain the keys with highest values
    key_highest_values = []
    #finding the highest value of the dictionary to compare other values to
    highest_value = max(letter_count.values())

    #iterate through each item of the dictionary
    for key, value in letter_count.iteritems():
        #if the value is equivalent to our highest_value variable
        if value == highest_value:
            #add the corresponding key to the key_highest_values list
            key_highest_values.append(key)


    return key_highest_values

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
