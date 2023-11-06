n=int(input('搜索范围：2到n，n：'))
q0=input('是否保存？(y/n)')
if q0=='y':
    q0=True
else:
    q0=False
if q0:
    q1=input('保存路径：')
q2=input('是否显示数表创建进度条？(y/n)')
if q2=='y':
    q2=True
else:
    q2=False
q3=input('是否显示排除进度条？(y/n)')
if q3=='y':
    q3=True
else:
    q3=False
if q0:
    q4=input('是否显示保存进度条？(y/n)')
    if q4=='y':
        q4=True
    else:
        q4=False
number=[]
if q2:
    a=100/(n-1)
for i in range(2,n+1):
    number.append(i)
    if q2:
        b=int((i-1)*a)
        if b==0:
            print('数表创建中……已创建：'+(3-len(str(b)))*' '+str(b)+'%['+100*'.'+']')
        elif b==1:
            print('数表创建中……已创建：'+(3-len(str(b)))*' '+str(b)+'%['+'>'+99*'.'+']')
        else:
            print('数表创建中……已创建：'+(3-len(str(b)))*' '+str(b)+'%['+(b-2)*'*'+'->'+(100-b)*'.'+']')
zhishu=[]
for num in number:
    print(num)
    zhishu.append(num)
    c=n//num
    if q3:
        if c>1:
            a=100/(c-1)
        else:
            print(num,'的倍数排除中……已排除： '+'100%['+98*'*'+'->'+']')
    for i in range(2,c+1):
        if num*i in number:
            number.remove(num*i)
        if q3:
            b=int((i-1)*a)
            if b==0:
                print(str(num)+'的倍数排除中……已排除：'+(3-len(str(b)))*' '+str(b)+'%['+100*'.'+']')
            elif b==1:
                print(str(num)+'的倍数排除中……已排除：'+(3-len(str(b)))*' '+str(b)+'%['+'>'+99*'.'+']')
            else:
                print(str(num)+'的倍数排除中……已排除：'+(3-len(str(b)))*' '+str(b)+'%['+(b-2)*'*'+'->'+(100-b)*'.'+']')
if q0:
    if q4:
        a=100/len(zhishu)
    c=''
    for i in range(len(zhishu)):
        if i==len(zhishu)-1:
            c+=str(zhishu[i])
        else:
            c+=str(zhishu[i])+' '
        if q4:
            b=int((i+1)*a)
            if b==0:
                print('保存中……已保存：'+(3-len(str(b)))*' '+str(b)+'%['+100*'.'+']')
            elif b==1:
                print('保存中……已保存：'+(3-len(str(b)))*' '+str(b)+'%['+'>'+99*'.'+']')
            else:
                print('保存中……已保存：'+(3-len(str(b)))*' '+str(b)+'%['+(b-2)*'*'+'->'+(100-b)*'.'+']')
    f=open(q1+str(n)+'以内的质数.txt','w',encoding='utf-8')
    f.write(c)
    f.close()
    print('保存成功')
else:
    print(zhishu)
