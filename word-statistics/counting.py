from collections import Counter

from files import get_file_paths


# Returns a list of the most common words in the source directory's text files. The
# total amount returned and the minimum size of the words are configurable.
def get_common_words(source=None, amount=10, min_length=7):
    files = get_file_paths(source)
    counter = Counter()

    for file in files:
        with open(file) as f:
            # Read all lines into memory to make it easier to search. Does not work for
            #  very large files.
            lines = f.read()
            words = lines.split()
            for word in words:
                # Discard English punctuation and normalize in lowercase.
                filtered_word = word.strip(".,!?'\";-").lower()
                # Only include words that are at least the minimum size.
                if len(filtered_word) > min_length:
                    counter.update({filtered_word: 1})

    most_common = counter.most_common(amount)
    # Discard total occurrences and return as list.
    result_list = [i[0] for i in most_common]
    return result_list
