W = 0
B = 0
for i in range(8):
  nu_i = [s for s in input()]
  for c in range(8):
      if nu_i[c] == "W":
        W += 1
      elif nu_i[c] == "B":
        B += 1

if W > B:
  print("YOU WIN")
elif W < B:
  print("YOU LOSE")
else:
  print("EVEN")
