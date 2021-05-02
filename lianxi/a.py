total=0;
def sum(arg1,arg2):
    total=arg1+arg2;
    print("函数内是局部变量：",total)
    return total;
sum(10,20);
print("函数外是全局变量：",total)
