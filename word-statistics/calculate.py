import os
import re


def stats_for_file(file, word):
    pattern = f"\s{re.escape(word)}[^a-z]"
    script_dir = os.path.dirname(__file__)
    abs_file_path = os.path.join(script_dir, file)
    with open(abs_file_path) as f:
        lines = f.read()
        results = re.findall(pattern, lines, flags=re.IGNORECASE)
        matches = len(results)
        examples = []
        if matches > 0:
            sentence_pattern = f"[^.]*\s{re.escape(word)}[^a-z][^.]*"
            sentences = re.findall(sentence_pattern, lines, flags=re.IGNORECASE)
            for sentence in sentences:
                examples.append(" ".join(sentence.split()) + ".")
        return {"matches": matches, "examples": examples}


def get_word_stats(word):
    count = 0
    examples = []
    in_documents = []
    for i in range(1, 7):
        document_name = f"doc{i}.txt"
        document_path = f"data/{document_name}"
        stats = stats_for_file(document_path, word)
        if stats["matches"] > 0:
            count += stats["matches"]
            examples += stats["examples"]
            in_documents.append(document_name)

    return {"count": count, "in_documents": in_documents, "examples": examples}
