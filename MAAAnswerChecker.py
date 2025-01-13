import requests
import json
import re

while True:
  print("\n")

  inp = input("Enter 's' if you want to stop. What AIME question do you want to see? \nExample1: 2005IIq7 \nExample2: 1990q5\n")
  if inp == 's':
    break
  urans = int(input("Your Answer? "))
  
  yr = inp[0:4]
  tp = None
  qnum = None
  if inp[4] == "q":
    tp = "X"
    qnum = inp[5:]
  else:
    if inp[5] == "q":
      tp = "I"
      qnum = inp[6:]
    else:
      tp = "II"
      qnum = inp[7:]
  
  url = 'https://artofproblemsolving.com/wiki/index.php/'+yr+'_AIME_'+tp+'_Answer_Key'
  
  if tp == 'X':
    url = 'https://artofproblemsolving.com/wiki/index.php/'+yr+'_AIME_Answer_Key'
    
  req = requests.get(url)
  longtxt = req.text
  ans = re.findall("<li>(\d+)</li>", longtxt)
  if int(ans[int(qnum)-1]) == urans:
    print("\n\nCongrats, you're right!")
  else:
    print("\n\nWrong Answer...")