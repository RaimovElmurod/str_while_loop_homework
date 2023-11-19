def main(s):
    m = 0
    n = 0
    while n < len(s):
        if s[n].isdigit() and int(s[n]) % 2 == 1:
            m += 1
        n += 1
    return m
print(main("1567534"))
print(main("3489769"))