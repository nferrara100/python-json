import os
import re


def stats_for_file(file, query):
    pattern = f"(?<=\s){re.escape(query)}(?![a-z])"
    regex = re.compile(pattern, flags=re.IGNORECASE)
    with open(file) as f:
        lines = f.read()
        results = regex.findall(lines)
        matches = len(results)
        examples = []
        if matches > 0:
            sentences = lines.split(".")
            for sentence in sentences:
                if regex.search(sentence):
                    examples.append(" ".join(sentence.split()) + ".")
        return {"matches": matches, "examples": examples}


def get_stats(query, source="data/"):
    count = 0
    examples = []
    in_documents = []
    script_dir = os.path.dirname(__file__)
    abs_source_path = os.path.join(script_dir, source)
    for filename in os.listdir(abs_source_path):
        abs_filename = os.path.join(abs_source_path, filename)
        stats = stats_for_file(abs_filename, query)
        if stats["matches"] > 0:
            count += stats["matches"]
            examples += stats["examples"]
            in_documents.append(filename)
    return {"count": count, "in_documents": in_documents, "examples": examples}


def get_all_stats(queries, source):
    for query in queries:
        stats = get_stats(query, source)
        print(
            f"Word or Phrase (Total Occurrences): {query}({stats['count']}), Documents: {stats['in_documents']}, Sentences containing the word: {stats['examples'][0]}"
        )
