class Solution:
    vowels = ['a', 'e', 'i', 'o', 'u']
    def reverseVowels(self, s: str) -> str:
        word_map = dict(enumerate(s))
        vow_map = {}
        consonant_map = {}

        for i,j in enumerate(word_map):
            if word_map[i] in self.vowels:
                vow_map[i] = word_map[i]
            else:
                consonant_map[i] = word_map[i]
        #print(vow_map)
        reversed_vow_map = dict(zip(vow_map.keys(), vow_map.values().__reversed__()))
        #print(reversed_vow_map)
        dict_res = dict(sorted({**consonant_map, **reversed_vow_map}.items()))
        #print(dict(sorted(dict_res.items())))


        #print("".join([str(i) for i in {**consonant_map, **reversed_vow_map}.values()]))
        return "".join([str(i) for i in dict_res.values()])

s = Solution()
print(s.reverseVowels("hello"))