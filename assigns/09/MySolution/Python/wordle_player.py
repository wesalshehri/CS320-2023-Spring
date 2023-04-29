########################
# HX-2023-04-15: 20 points
########################
"""
Given a history of wordle hints, this function returns a
word as the player's guess.
"""
########################################################################

def wordle_guess(hints):
    guess_string = "$" * len(hints[0])
    counts_dict = {}
    ignore_set = set()

    for hint in hints:
        word = pylist_make_map(pylist_make_filter(hint, lambda x: x[0] != 0), lambda x: x[1])
        count_in_word = {x: word.count(x) for x in word}

        for i in count_in_word:
            if i not in counts_dict or count_in_word[i] > counts_dict[i]:
                counts_dict[i] = count_in_word[i]

        for i, j in enumerate(hint):
            if j[0] == 1:
                guess_string = replace_string(guess_string, i, j[1])
            else:
                ignore_set.add((i, j[1]))

    counts_list = []
    for i in counts_dict:
        counts_list += ([i] * counts_dict[i])
        
    def is_word_safe(word):
        def is_position_safe(string):
            return foreach_to_iforall(string_foreach)(string, lambda i, j: (not (i, j) in ignore_set))

        def is_count_safe(d, string):
            word_list = list(string)
            count_in_word = {x: word_list.count(x) for x in word_list}
            res = True
            for k in d:
                if not ((k in count_in_word) and count_in_word[k] >= d[k]):
                    res = False
            return res

        return is_position_safe(word) and is_count_safe(counts_dict, word) and (not '$' in word)

    def get_nexts(next_word):
        child_words = []
        try:
            i = next_word.index('$')
            return string_imap_pylist(counts_list, lambda _, j: replace_string(next_word, i, j))
        except ValueError:
            return []

    if '$' in guess_string:
        temp = stream_make_filter(graph_dfs([guess_string], get_nexts), lambda s: is_word_safe(s))
        return stream_get_at(temp, 0)
    else:
        return guess_string


def replace_string(string, index, new):
    return string[:index] + new + string[index + 1:]


########################################################################
