s = [int(raw_input()), int(raw_input()), int(raw_input())]
print max( (s[0] + s[1]) * s[2], s[0] + s[1] * s[2], s[0] * s[1] * s[2], s[0] * (s[1] + s[2]), s[0] * s[1] + s[2], s[0] + s[1] + s[2] )