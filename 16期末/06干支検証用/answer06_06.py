Year = int(input())
Y = Year - 4

if Y%12 == 0 :
  print("亥")
elif Y%11 == 0:
  print("戌")
elif Y%10 == 0:
  print("酉")
elif Y%9 == 0:
  print("申")
elif Y%8 == 0:
  print("未")
elif Y%7 == 0:
  print("午")
elif Y%6 == 0:
  print("巳")
elif Y%5 == 0:
  print("辰")
elif Y%4 == 0:
  print("卯")
elif Y%3 == 0:
  print("寅")
elif Y%2 == 0:
  print("丑")
else:
  print("子")