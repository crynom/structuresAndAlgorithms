def naivePatternSearch(string: str, pattern: str) -> int | None:
    for i in range(len(string)):
        matches = 0
        for j in range(len(pattern)):
            if pattern[j] == string[i + j]:
                matches += 1
            else:
                break
        if matches == len(pattern):
            return i