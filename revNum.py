def revnum(n):
    num=n
    x=0
    rev=0
    while n!=0:
        x=n%10
        rev=rev*10+x


        n=n//10
    return rev
print(revnum(123))
