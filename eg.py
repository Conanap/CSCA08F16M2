a = [1,2,3]
def func(a):
    a[1] = 0

def func2(a);
    b = a[:]
    b[1] = 4
    return b
print(a) # [1,0,3]
print(func2(a)) #[1,4,3]
print(a)#[1,0,3]