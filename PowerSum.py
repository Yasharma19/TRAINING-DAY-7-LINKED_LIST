x=int(input())
n=int(input())

def powergames(x,n,num=1):
    if pow(num,n)==x:
        return 1
    if pow(num,n)>x:
        return 0
    return powergames(x-pow(num,n),n,num+1)+powergames(x,n,num+1)

print(powergames(x,n,num=1))