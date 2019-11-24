# def yinshu():   #def  函数名()    定义一个新的函数
#     for i in range(2,101):
#         b=[j for j in range(1,i) if i%j==0]
#         if sum(b)==i:
#             print(i)
# yinshu()   #调用函数：函数名()

# def sum1(x,y):
#     a=0
#     for i in range(x,y+1):
#         b=[j for j in range(2,i) if i%j==0]
#         if len(b)==0:
#             a+=i
#     print(a)
# sum1

'''
显示 a 列表中两个数相加，等于b的
'''
# def he(a,b):
#     for i in a:
#         for j in a:
#             if i + j == b:
#                 print(i,j)
#                 a.remove(i)
# he(a=[12,1,10,3,25,45],b=13)



# def hanshu():
#     a=111
#     print(a)
#     def wrapper():
#         b=222
#         print(b)
#     return wrapper
# hanshu()()

'''
共有 m 块钱,每天花 k 块钱,可以得到一块钱, 可以花几天
'''
# m=int(input("请输入您现有的金额（单位：元）："))
# k=int(input("请输入花多少钱可以得到1元钱："))
# i=0
# b=0
# while 0<m:
#      m=m-3
#      i=i+1
#      b = b + 1
#      if i%k==0:
#          m=m+1
# print(b)

'''二进制转十进制'''
# a=input("请输入一组二进制数：")
# a=a[::-1]
# b=0
# for i in a:
#     for j in range(0,2):
#         if i==str(j):
#             c=j*2**(a.index(i))
#         b = b + c
# # print(b)


# def hanshu(**kwargs):
#     print(kwargs)
# hanshu(name=1,route=[1,2],day="adgy")


'''打印空行有多少行，#开头的有多少行，共有多少行'''
# a=open("a.txt","r",encoding="utf8")
# e=0
# b=0
# i=0
# while 1:
#     c=a.readline()
#     if c==("\n"):
#         e=e+1
#     elif c.startswith("#"):
#         b=b+1
#     elif c=="":
#         break
#     i = i + 1
# print("空行共有%d行" %e)
# print("#号共有%d行" %b)
# print(i)
# a.close()

#系统函数
#1.enumerate():将有序列的数据中的值与其下标显示
#2.sum（）:求和函数（括号中只能填元组，列表，集合）
a=sum((1,2,3,4))
print(a)
#3.max():求最大，按照ascii码表排序，但必须是同种类型
a=max("a","b","c")
print(a)
#4.min():求最小，按照ascii排序，但必须是同种类型
a=min(1,2,3,1)
print(a)
#5.divmod():返回商和余数
a,b=divmod(60,7)   #a为商，b为余数
print(a,b)
#6.chr()求括号内的码在ascii码中的值
code=chr(65)
print(code)
a=[chr(i) for i in range(97,123)]
print(a)
#7.ord():将值转换为ascii码中的码
a=ord("a")
print(a)
#8.bin():将十进制转换为二进制
a=bin(6)
print(a)
#9.oct():将十进制转换为八进制
a=oct(8)
print(a)
#10.hex():将十进制转换为16进制
a=hex(16)
print(a)
#11.都可以转换为十进制
a=int(0b10)
print(a)