import re
e={'tmg':'úng','rl':'n','rr':'n','êĩ':'ết','phãi':'phải', 'NGẦN':'NGÂN','ĐÓC':'ĐỐC'}
def post_process(a):
    b=''
    for word in a.split():
        c=0
        d=''
        for a in word:
            c=c+1
            if c>1:
                if not a.islower() :
                    d=d+a.lower()
                else :
                    d=d+a
            else :
                d=d+a
        b=b+d+' '
    for key, value in e.items():
        b=b.replace(key,value)
    b = re.sub(r"[@#&*$%_+]", "", b, flags=re.I)  
    return b.strip()

def process_text(str3):
    str1 =str3
    str1 =str1.strip()
    str1 =str1.replace(' ','')
    str1 = str1.replace('\n','')
    str1 = str1.replace('.','')
    str1 = str1.replace(',','')
    str1 = str1.replace(':','')
    str1 = str1.replace('-','')
    str1 = str1.replace(';','')
    str1 = str1.replace('”','')
    str1 = str1.replace('“','')
    str1 = str1.replace('(','')
    str1 = str1.replace(')','')
    return str1.strip()
def check_cta(text):
    mydict=dict()
    kq=dict()
    count=0
    with open("vi-DauMoi.dic", "r", encoding="utf8") as file: 
        for line in file: 
            a=line.strip()
            mydict[count]=a
            count=count+1
    count=0
    for word in text.split():
        wordd=process_text(word)
        if (wordd != '')and (wordd.lower() not in mydict.values()):
            kq.update({count:wordd})
        count+=1
    return(kq)