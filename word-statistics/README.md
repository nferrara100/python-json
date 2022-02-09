# Word stats command line utility

This python command line utility accepts text files and outputs basic statistics on the
frequency of a given word in them. It requires tabulate to format its output and Pytest
to run the test suite. It is case insensitive and supports searching for phrases when
quotation marks are used. By default it reads from the `example_data` directory, but
supports any directory.

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
4.  Create a package that can be installed by a package manager so that the utility can
    be used anywhere easily from the command line and updates can be issued.
5.  Run on multiple directories at the same time.
6.  Customise the amount of example sentences shown with a command line argument.
7.  The current implementation is not memory efficient on large files because it reads
    the entire file into memory before parsing it. This could be improved, but would
    make the solution more complicated.
8.  Outputting to a .txt file, a .rtf file to allow formatting such as bold words, or a
    webpage via HTML to allow interactive results.
9.  Support searching file formats other than .txt.
10. Support searching directories recursively.
