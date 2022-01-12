

import math
import re
input = "Stats\nAmore, Roma\nNo 'x' in Nixon\nWas it a cat I saw?"

input = "Stars\nO, a kak Uwakov lil vo kawu kakao!\nSome men interpret nine memos"
data = input.split("\n")

output = ""

for x in data :
  x =x.lower()
  x = re.sub('[^a-z]+', '', x)
  # x =x.replace("\'","")
  # x =x.replace(",","")
  # x =x.replace(" ","")
  # x =x.replace("?","")
  # x =x.replace("!","")

  # print(math.floor(len(x)))
  # print('..................')
  # print(math.floor(len(x)/2))
  # print('>>>>>>>>')
  prefix = x[:math.floor(len(x)/2):]
  postfix = x[math.floor(len(x)/2)+1:]
  postfix = postfix[::-1]

  if prefix == postfix:
    # print(f"refix: {prefix} postfix: {postfix} answer: {prefix==postfix}")
    output+='Y'
  else: output+='N'


  print(output)