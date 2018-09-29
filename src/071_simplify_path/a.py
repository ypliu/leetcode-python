class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """

        if not path or 0 == len(path):
            print "The path is empty."
            return ""

        path += '/'
        stack = []; curr_file_name = ""
        for ch in path:
            if '/' != ch:
                curr_file_name += ch
            elif curr_file_name:
                if ".." == curr_file_name:
                    if stack:
                        stack.pop()
                elif "." != curr_file_name:
                    stack.append(curr_file_name)
                curr_file_name = ""
        return ('/' + '/'.join(stack))

# debug
s = Solution()
paths = [ "/home/", "/a/./b/../../c/", "/a/../../b/../c//.//", "/a//b////c/d//././/.." ]
for path in paths:
    print path, "=>", s.simplifyPath(path)
