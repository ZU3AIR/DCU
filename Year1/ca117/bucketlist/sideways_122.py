#!/usr/bin/env python3
import sys

def c_lines(s):
   number = 0
   for i in s:
      number += 1
   return number

def word_length(s):
   return len(s[0].strip())

def main():
   s_list = []
   l = sys.stdin.readlines()
   number = c_lines(l)
   currlen = word_length(l)
   i = 0
   while i < currlen:
      s_list.append("")
      i += 1
   k = 0

   while k < currlen:
      for line in l:
         line = line.strip()
         s_list[k] += line[k]
      k += 1
   s_list.sort(key=str.lower)
   p = 0
   while p < number:
      rid = ''
      for i in s_list:
         rid += i[p]
      print(rid)
      p += 1

if __name__ == "__main__":
   main()
