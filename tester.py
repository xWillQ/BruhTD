level = open("level1.txt", "r")
lines = level.read().splitlines()
level_theme = str(lines[1])
print(level_theme)
