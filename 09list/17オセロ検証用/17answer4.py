a1 = []
osero=[]
for i in range(8):
    i=input()
    a1.append(i)
for x in a1 :
  osero+=x
Wcount=osero.count("W")
Bcount=osero.count("B")
if Wcount>Bcount :
  print("YOU WIN")
elif Bcount>Wcount :
  print("YOU LOST")
else :
  print("EVEN")
