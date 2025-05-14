# Unit-IX String Processing: Finite Automata method, KMP

# ====================================
# 1. Finite Automata Method (DFA)
# ====================================

def compute_dfa(pattern, alphabet):
    """
    Returns the DFA table for the given pattern and alphabet.
    dfa[state][char] = next_state
    """
    m = len(pattern)
    dfa = [{} for _ in range(m + 1)]

    for state in range(m + 1):
        for a in alphabet:
            k = min(m, state + 1)
            while k > 0 and not pattern[:k] == (pattern[:state] + a)[-k:]:
                k -= 1
            dfa[state][a] = k
    return dfa

def finite_automata_matcher(text, pattern):
    alphabet = set(text + pattern)
    dfa = compute_dfa(pattern, alphabet)
    m = len(pattern)
    state = 0
    result = []

    for i, char in enumerate(text):
        state = dfa[state].get(char, 0)
        if state == m:
            result.append(i - m + 1)
    return result

# ====================================
# 2. Knuth-Morris-Pratt (KMP)
# ====================================

def compute_lps(pattern):
    """
    Longest Prefix Suffix (LPS) array computation for KMP
    """
    lps = [0] * len(pattern)
    length = 0
    i = 1

    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length > 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    return lps

def kmp_search(text, pattern):
    """
    KMP search algorithm that returns starting indices of all matches
    """
    n, m = len(text), len(pattern)
    lps = compute_lps(pattern)
    result = []

    i = j = 0  # text and pattern index

    while i < n:
        if text[i] == pattern[j]:
            i += 1
            j += 1
        if j == m:
            result.append(i - j)
            j = lps[j - 1]
        elif i < n and text[i] != pattern[j]:
            if j > 0:
                j = lps[j - 1]
            else:
                i += 1
    return result

# ===========================
# Test All Algorithms
# ===========================

def test_all():
    print("=== Unit-IX: String Processing ===\n")

    text = "ababcabcabababd"
    pattern = "ababd"

    # DFA Matching
    dfa_matches = finite_automata_matcher(text, pattern)
    print(f"Finite Automata Matches at: {dfa_matches}")
    assert dfa_matches == [10]

    # KMP Matching
    kmp_matches = kmp_search(text, pattern)
    print(f"KMP Matches at: {kmp_matches}")
    assert kmp_matches == [10]

    # Additional KMP test
    print("\nMore KMP Examples:")
    print(kmp_search("AAAAABAAABA", "AAAA"))     # [0]
    print(kmp_search("ABABDABACDABABCABAB", "ABABCABAB"))  # [10]

if __name__ == "__main__":
    test_all()
