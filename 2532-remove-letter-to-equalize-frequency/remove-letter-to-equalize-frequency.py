class Solution:
    def equalFrequency(self, word: str) -> bool:
        frequencies = Counter(Counter(word).values())
        if len(frequencies) == 1:
            key, value = next(iter(frequencies.items()))
            if key == 1 or value == 1:
                return True

        if len(frequencies) == 2:
            if 1 in frequencies and frequencies[1] == 1:
                return True
            min_ = min(frequencies)
            max_ = max(frequencies)
            diff = max_ - min_
            if diff == 1 and frequencies[max_] == 1:
                return True


        return False

