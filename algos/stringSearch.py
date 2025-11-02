from time import perf_counter

def naivePatternSearch(pattern: str, string: str) -> int:
    occurrences = 0
    for i in range(len(string)):
        matches = 0
        for j in range(len(pattern)):
            if i + j == len(string):
                break
            if pattern[j] == string[i + j]:
                matches += 1
            else:
                break
        if matches == len(pattern):
            occurrences += 1
    return occurrences

def rabinKarp(pattern: str, string: str) -> int:
    patternLength = len(pattern)
    substring = string[:patternLength]
    patternHash = 0
    for i in range(len(pattern)):
        patternHash += ord(pattern[i]) * 26 ** (len(pattern) - i - 1)

    substringHash = 0
    for i in range(len(substring)):
        substringHash += ord(substring[i]) * 26 ** (len(substring) - i - 1)
    
    occurrences = int(substringHash == patternHash)
    for ch in string[patternLength:]:
        substring = substring[1:] + ch
        substringHash = (substringHash - ord(substring[0]) * 26 ** ((len(substring) - 1))) * 26 + ord(ch)
        occurrences += int(substringHash == patternHash)

    return occurrences

if __name__ == '__main__':
    string = 'A' * 1000000
    pattern = 'A' * 1000

    start = perf_counter()
    print(f'Naive {naivePatternSearch(pattern, string)}: {perf_counter() - start}')
    start = perf_counter()
    print(f'Rabin-Karp {rabinKarp(pattern, string)}: {perf_counter() - start}')