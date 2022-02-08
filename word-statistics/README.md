# Word stats command line utility

This python command line utility accepts text files and outputs basic statistics on the
frequency of a given word in them. It runs using only the Python standard library, but
the test suite requires Pytest.

Given more time, the following additional features could be implemented:

1.  Switch to [NLTK](https://www.nltk.org/index.html) for text and sentence processing.
    The current implementation handles the most common cases, but numerous edge cases
    exist in the parsing of words and sentences that could cause suboptimal output. For
    instance, "The U.S. Congress did x." is currently regarded as three sentences
    because of the additional periods. Intelligently catching acronyms like that would
    still be possible with complicated regex logic, but a far more readable and
    maintainable solution would be to use a third-party library.
2.  Increase the size of the test suite to include more edge cases.
3.  Search all words by default and rank them by order of frequency. The current
    implementation might have to be rewritten since reads the file again every time it
    searches for a new word.
