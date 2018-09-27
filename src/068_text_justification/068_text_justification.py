class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """

        if not words or 0 == len(words):
            return []

        res = []; cur_width = 0
        for i in xrange(len(words)):
            len_word = len(words[i])
            if len_word > maxWidth:
                print 'Error, there is more than maxWidth characters in ', words[i]
                return

            if 0 == cur_width:
                cur_width = len_word
                start = i
            else:
                temp_width = cur_width + 1 + len_word
                if temp_width < maxWidth:
                    cur_width = temp_width
                elif temp_width == maxWidth:
                    res.append(' '.join(words[start:i+1]))
                    cur_width = 0
                else:
                    if i - start == 1:
                        new_line = words[start] + ' '*(maxWidth - cur_width)
                    else:
                        num_space, remain_space = divmod((maxWidth - cur_width), (i - 1 - start))
                        new_line = words[start]
                        num_space += 2
                        for j in xrange(start+1, start+1+remain_space):
                            new_line += ' '*(num_space) + words[j]
                        num_space -= 1
                        for j in xrange(start+1+remain_space, i):
                            new_line += ' '*(num_space) + words[j]
                    res.append(new_line)
                    cur_width = len_word
                    start = i
        if cur_width > 0:
            new_line = ' '.join(words[start:i+1])
            new_line += ' ' * (maxWidth - len(new_line))
            res.append(new_line)
        return res

# debug
s = Solution()
print s.fullJustify(["This", "is", "an", "example", "of", "text", "justification."], 16)
print s.fullJustify(["What","must","be","acknowledgment","shall","be"], 16)
print s.fullJustify(["Science","is","what","we","understand","well","enough","to","explain", "to","a","computer.","Art","is","everything","else","we","do"], 20)
