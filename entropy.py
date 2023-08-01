import sys
import math
from collections import Counter

def main() -> int:
    if len(sys.argv) < 2:
        print("No file provided", file=sys.stderr)
        return 1
    all_words = Counter()
    with open(sys.argv[1]) as f:
        for l in f.readlines():
            l = l.strip()
            if l == '':
                continue
            all_words.update([w.lower() for w in l.split()])
    N = len(all_words)
    H = 0
    for v in all_words.values():
        P = v/N
        H -= P*math.log2(P)
    nl = '\n'
    print(sys.argv[1])
    print(f"Total Words: {N}")
    # https://en.wikipedia.org/wiki/Entropy_(information_theory)
    print(f"Shannon Entropy: {H}")
    print(f"5 Most Common Words:\n{nl.join([f'{v}: {k}' for k,v in
                                   all_words.most_common(5)])}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
