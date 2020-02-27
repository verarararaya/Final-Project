# -*- coding: utf-8 -*-
'''
python读取文件，每两行为一组
'''

def branch(infile, outfile):
    infopen = open(infile, 'r')
    outopen = open(outfile, 'w')
    lines = infopen.readlines()
    #print(lines)
    # line1 = lines.remove('\n')
    i = 1
    for line in lines:
        line=line.strip('\n')
        # for a in line:
            # print(a)
        #print(line)
        if i % 2 == 0:
            outopen.write(line + '\n')
        else:
            #print(line[4:5])
            outopen.write(line + '\t')
        i += 1
    infopen.close()
    outopen.close()


branch("ACP164.txt", "test.txt")
branch("dataset.txt", "training.txt")

# # 读取excel数据表格，使用pandas,返回dataframe对象(一个抽象的二维表结构)，记为df
# # names = ['?','Y or N', 'name of peptide']
# # df = pd.read_csv('training.txt',sep="|\t|\|", header=None, names=names)
# # print(df)

df=open('training.txt',"r")
read=df.readlines()
df.close()
i=0
a=0
one=open('file0.txt',"w")
two=open('file1.txt','w')
three=open('file2.txt','w')
four=open('file3.txt','w')
five=open('file4.txt','w')
one.write("88"+"\n")
two.write("88"+"\n")
three.write("88"+"\n")
four.write("88"+"\n")
five.write("88"+"\n")
for line in read:
    line = line.strip('\n').split("\t")
    # print(line[1])
    # print(line[1])
    x=line[1]
    y=len(x)
    if(y<=62):
    # print(y)
        if(line[0][-1]=="1"):
            i=i+1
            # print(str(i)+"\t"+"1"+"\t"+line[1]+"\t"+str(y))
            if(i>=1 and i<=44):
                one.write(str(i)+"-positive"+"\n"+str(y)+"\n"+line[1]+"\n"+"2"+"\n")
            if(i>=45 and i<=88):
                two.write(str(i)+"-positive"+"\n"+str(y)+"\n"+line[1]+"\n"+"2"+"\n")
            if (i >= 89 and i <= 132):
                three.write(str(i)+"-positive"+"\n"+str(y)+"\n"+line[1]+"\n"+"2"+"\n")
            if (i >= 133 and i <= 176):
                four.write(str(i)+"-positive"+"\n"+str(y)+"\n"+line[1]+"\n"+"2"+"\n")
            if (i >= 177 and i <= 220):
                five.write(str(i)+"-positive"+"\n"+str(y)+"\n"+line[1]+"\n"+"2"+"\n")
        if (line[0][-1] == "0"):
            a = a + 1
            # print(str(i) + "\t" + "1" + "\t" + line[1])
            if (a >= 1 and a <= 44):
                one.write(str(a)+"-negative"+"\n"+str(y)+"\n"+line[1]+"\n"+"1"+"\n")
            if (a >= 45 and a <= 88):
                two.write(str(a)+"-negative"+"\n"+str(y)+"\n"+line[1]+"\n"+"1"+"\n")
            if (a >= 89 and a <= 132):
                three.write(str(a)+"-negative"+"\n"+str(y)+"\n"+line[1]+"\n"+"1"+"\n")
            if (a >= 133 and a <= 176):
                four.write(str(a)+"-negative"+"\n"+str(y)+"\n"+line[1]+"\n"+"1"+"\n")
            if (a >= 177 and a <= 220):
                five.write(str(a)+"-negative"+"\n"+str(y)+"\n"+line[1]+"\n"+"1"+"\n")
one.close()
two.close()
three.close()
four.close()
five.close()
test=open("test.txt","r")
readtest=test.readlines()
test.close()
b=250
c=250
test1=open("testfinal.txt","w")
test1.write("164"+"\n")
# test2=open("test2.txt","w")
# test3=open("test3.txt","w")
# test4=open("test4.txt","w")
# test5=open("test5.txt","w")
for line in readtest:
    line = line.strip('\n').split("\t")
    x = line[1]
    y = len(x)
    if (line[0][-1] == "1"):
        b = b + 1
        # print(str(b) + "\t" + "1" + "\t" + line[1] + "\t" + str(y))
        # test1.write(str(b) + "\t" + "1" + "\t" + line[1] + "\t" + str(y)+"\n")
        test1.write(str(b)+"-positive"+"\n"+str(y)+"\n"+line[1]+"\n"+"2"+"\n")
        # if(b>=17 and b<=32):
        #     test2.write("1"+"\t"+line[1]+"\t"+str(y)+"\n")
        # if (b >= 33 and b <= 48):
        #     test3.write("1" + "\t" + line[1] + "\n")
        # if (b >= 49 and b <= 64):
        #     test4.write("1" + "\t" + line[1] +"\t"+str(y)+"\n")
        # if (b >= 65 and b <= 80):
        #     test5.write("1" + "\t" + line[1] +"\t"+str(y)+ "\n")
    if(line[0][-1] == "0"):
        c = c + 1
        # print(str(c) + "\t" + "0" + "\t" + line[1] + "\t" + str(y))
        test1.write(str(c) + "-negative" + "\n" + str(y) + "\n" + line[1] + "\n" + "1" + "\n")
        # if (c >= 17 and c <= 32):
        #     test2.write("0" + "\t" + line[1] + "\t" + str(y) + "\n")
        # if (c >= 33 and c <= 48):
        #     test3.write("0" + "\t" + line[1] + "\n")
        # if (c >= 49 and c <= 64):
        #     test4.write("0" + "\t" + line[1] + "\t" + str(y) + "\n")
        # if (c >= 65 and c <= 80):
        #     test5.write("0" + "\t" + line[1] + "\t" + str(y) + "\n")

test1.close()
# test2.close()
# test3.close()
# test4.close()
# test5.close()
# ndf=open('negativeall.txt',"w")
# for line in read:
#     line = line.strip('\n').split("\t")
#     # print(line[0][-1])
#     if(line[0][-1]=="0"):
#         a=a+1
#         print(str(a)+"\t"+"0"+"\t"+line[1])
#         ndf.write(str(a)+"\t"+"0"+"\t"+line[1]+"\n")
# ndf.close()