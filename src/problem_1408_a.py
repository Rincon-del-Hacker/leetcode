"""
# iterar toda la lista
    # por cada elemento de la lista
    # iterar toda la lista (de nuevo) y preguntar
    # si la logitud de la palabra actual es > a long de palabra evaluada
        # preguntar si palabra evaluada es substring de palabra actual
            # Agregar a lista de substrings

"""

from typing import List

class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        substrings = set()

        for word in words:
            for inner_word in words:
                if self.is_substring(word, inner_word):
                    substrings.add(word)

        return list(substrings)

    def is_substring(self, word, inner_word):
        if word != inner_word \
        and len(inner_word) > len(word) \
        and word in inner_word:
            return True
        return False

if __name__ == '__main__':
    s = Solution()
    assert "as" and "hero" in s.stringMatching(["mass","as","hero","superhero"])
    assert "code" and "et" in s.stringMatching(["leetcode","et","code"])
    assert s.stringMatching(["blue","green","bu"]) == []
