def main(s):

    i = 0
    consonat = 0
    while i<len(s):
        if s[i]=="a" or s[i]=="e" or s[i]=="i" or s[i]=="o" or s[i]=="u" or s[i]=="o'":
            consonat +=1
        i+=1
    return len(s)-consonat -1
print(main("CodeschoolUz"))