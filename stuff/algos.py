def find_max(word1, word2):
    if word1 > word2:
        return word1
    elif word1 < word2:
        return word2
    else:
        return word1


def search_possible_word(word, iterator):
    result = word[:iterator] + word[iterator + 1:]
    return result


def find_max_chain(list, dictionary):
    largest_chain = 0
    for word in list:
        current_max = 1
        iterator = 0
        while iterator < len(word):
            possible_word = search_possible_word(word, iterator)

            if possible_word in dictionary:
                current_max = find_max(current_max, dictionary[possible_word])

            iterator += 1
        dictionary[word] = current_max+1
        largest_chain = find_max(largest_chain, current_max)

    return largest_chain
