# txt=open("a.txt","w",encoding="utf8")
# txt.write("nihao")
# txt.write("nibuhao")
# txt.close()

txt=open("a.txt","w",encoding="utf-8")
for i in range(1,10):
    for j in range(1,i+1):
       txt.write(f"{i}*{j}={i*j}\t")
    txt.write("\n")
txt.close()

# txt=open("a.txt","w",encoding="utf8")
# # txt.write("f {}")
# for i in range(1,101):
#     for j in range(1, 5):
#        txt.write(f"{i}*{j}={i*j}    \t")
#     txt.write("\n")
# txt.close()

# txt=open(r"C:\Users\tulili\Desktop\新建文本文档.txt","r",encoding="utf8")
# a=txt.read()
# print(a)
# txt.close()
#
# txt=open(r"C:\Users\tulili\Desktop\新建文本文档.txt","r",encoding="utf8")
# a=txt.read()
# b=[]
# c=" "
# for i in a:
#     c+=i
#     if i=="\n":
#         b.append(c)
#         c=" "
# print(a)
# txt.close()

# txt=open(r"C:\Users\tulili\Desktop\新建文本文档.txt","a",encoding="utf8")
# txt.write("\nndjwqf")
# txt.close()

# txt=open(r"C:\Users\tulili\Desktop\新建文本文档.txt","r")
# print(txt.read())
# txt.close()

# txt=open(r"c:\Users\tulili\Desktop\681ef6f50f20971ac5bddb07161fc6b5.mp3","rb")
# print(txt.read())
# txt.close()

#输入音频
# a=open(r"c:\Users\tulili\Desktop\681ef6f50f20971ac5bddb07161fc6b5.mp3","rb")
# b=a.read()
# a.close()
# print(b)
# c=open("txt.mp4","ab")
# c.write(b)
# c.close()

