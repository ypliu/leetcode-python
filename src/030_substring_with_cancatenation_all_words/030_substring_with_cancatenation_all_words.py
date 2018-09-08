class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """

        counts_words = len(words)
        if 0 == counts_words or not s:
            return []
        len_word = len(words[0])
        total_len_word = counts_words * len_word
        last = len(s) - total_len_word
        if 0 == total_len_word or last < 0:
            return []

        res = [ ]
        dict = { }
        for i in words:
            if i in dict:
                dict[i] += 1
            else:
                dict[i] = 1

        for i in range(len_word):
            seg_start = word_start = i
            temp_dict = { }
            while seg_start <= last:
                word = s[word_start:word_start+len_word]
                word_start += len_word
                if word not in dict:
                    seg_start = word_start
                    temp_dict = { }
                else:
                    if word not in temp_dict:
                        temp_dict[word] = 1
                    else:
                        temp_dict[word] += 1
                        while temp_dict[word] > dict[word]:
                            remove_word = s[seg_start:seg_start+len_word]
                            temp_dict[remove_word] -= 1
                            seg_start += len_word
                    if word_start - seg_start == total_len_word:
                        res.append(seg_start)

        return res

# debug
s = Solution()
print s.findSubstring("barfoothefoobarman", ["foo","bar"])
print s.findSubstring("wordgoodstudentgoodword", ["word","student"])
