from tokenize import group


def are_anagrams(a: str, b: str):
   a = sorted(a.lower())
   b = sorted(b.lower())
   return a == b

def remove_duplicates(entries: list[str]):
    uniques = []
    cleaned = []
    for entry in entries:
        if sorted(entry.lower()) in uniques:
            continue
        uniques.append(sorted(entry.lower()))
        cleaned.append(entry)
    print(cleaned)
    return len(cleaned)

entries = ["abc", "bca", "GhZH", "gzHH", "Yujian is Awesome", "Awesome Yujian Is"]
# print(remove_duplicates(entries))

def group_anagrams(entries: list[str]):
    grouped = {}
    for entry in entries:
        _sorted = "".join(sorted(entry.lower()))
        if _sorted not in grouped:
            grouped[_sorted] = [entry]
        elif _sorted in grouped.keys():
            grouped[_sorted].append(entry)
    return grouped

print(group_anagrams(entries))