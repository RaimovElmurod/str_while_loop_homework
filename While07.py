def main(s):
    m = 0
    n = 0
    while n < len(s):
        if s[n].isdigit() and int(s[n]) % 2 == 0:
            m += 1
        n += 1
    return m
print(main("56786543250"))
print(main("123456"))