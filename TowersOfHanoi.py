
def ToH(frm,to):
    print(f'move from {frm} to {to}')

def TowersOfHanoi(n,frm,to,spare):
    if n==1:
       return ToH(frm,to)
    else:
       TowersOfHanoi(n-1,frm,spare,to)
       TowersOfHanoi(1,frm,to,spare)
       TowersOfHanoi(n-1,spare,to,frm)

a=int(input("Enter a number: "))
TowersOfHanoi(a,'P1','P2','P3')
