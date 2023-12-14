Si = [input() for i in range(8) ]
Si = ''.join(Si)
count_B = Si.count("B")
count_W = Si.count("W")
if count_W > count_B:
   print("YOU WIN")
elif count_B > count_W:
   print("YOU LOSE")
else:
   print("EVEN")
