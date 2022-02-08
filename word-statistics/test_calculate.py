from calculate import get_word_stats


def test_count_word_me():
    assert get_word_stats("me")["count"] == 35


def test_state_capital_in_docs():
    assert get_word_stats("Old State Capitol")["in_documents"] == ["doc1.txt"]


def test_example_word_azerbaijan():
    assert "Thank you." in get_word_stats("Thank")["examples"]


def test_example_word_biological():
    assert (
        "And we need to work together to obtain a bilateral agreement on biological threat reduction."
        in get_word_stats("biological")["examples"]
    )
