1 #!/usr/bin/env python
2 
3 s = raw_input()
4 
5 i = 0
6 while i < len(s) and not (s[i] >= "A" and s[i] <= "Z"):
7     i = i + 1
8 
9 if i < len(s):
10     print s[i], i