def main(s):
    t=0
    i=0
    while i<len(s):
        if s[i].islower():
            t+=1
        i+=1
    return t
print(main("CodeschoolUz"))
