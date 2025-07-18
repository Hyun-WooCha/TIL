l = []

def input1():
    l = list(map(int,input().split()))

def output(l):
    for i in range(len(l),-1,-1) :
        print(l[i],end='')

def main():
    input()
    output()

main()