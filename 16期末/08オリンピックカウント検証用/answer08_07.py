Ys, Ye = map(int, input().split())

cancel_year = {1916, 1940, 1944, 2020}

olympics_count = 0

for year in range(max(Ys, 1896), Ye + 1, 4):

    if year in cancel_year:
        continue

    if 1937 <= year <= 1947:
        continue

    olympics_count += 1


if 2020 <= Ye <= 2024:
    olympics_count += 1

print(olympics_count)
