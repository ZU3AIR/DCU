1 #!/usr/bin/env python
2 
3 s = raw_input()
4 
5 i = 0
6 while i < len(s) and not (s[i] >= "A" and s[i] <= "Z"):
7     i = i + 1
8 
9 j = i
10 while j < len(s) and (s[j] >= "A" and s[j] <= "Z"):
11     j = j + 1
12 
13 if i < len(s):
14     print s[i:j], i