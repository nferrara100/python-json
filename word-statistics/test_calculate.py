from calculate import get_stats


def test_correct_count():
    stats = get_stats("me")
    assert stats["count"] == 35
    assert len(stats["examples"]) == 35


def test_multiple_word_query():
    stats = get_stats("Old State Capitol")
    assert stats["in_documents"] == ["doc1.txt"]


def test_simple_example_sentence():
    stats = get_stats("Thank")
    assert "Thank you." in stats["examples"]


def test_long_example_sentence():
    stats = get_stats("biological")
    assert (
        "And we need to work together to obtain a bilateral agreement on biological threat reduction."
        in stats["examples"]
    )


def test_word_end_of_sentence():
    stats = get_stats("kiev")
    assert (
        "We were in Ukraine, visiting a pathogen laboratory in Kiev."
        in stats["examples"]
    )


def test_case_insensitive():
    stats = get_stats("DiFfIcUlT")
    assert "It will be difficult." in stats["examples"]


def test_nonalphabetic_char():
    stats = get_stats("my family's")
    assert (
        "In many ways, then, my family's life reflects some of the contradictions of Kenya, and indeed, the African continent as a whole."
        in stats["examples"]
    )
