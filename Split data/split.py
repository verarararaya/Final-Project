open_diff = open('dataset.txt', 'r')
diff_line = open_diff.readlines()

line_list = []
for line in diff_line:
    line_list.append(line)

lengthlist = []
for i in range(int(len(line_list)/2)):
    j=int(2*i)
#     if(len(line_list[j+1] ) < 50):
#         lengthlist.append(line_list[j])
#         lengthlist.append(line_list[j+1])
    if(j<int(len(line_list)/2)):
        line_list[j] = "positive-"+ str(i)+'\n' + str(len(line_list[j + 1]) - 1) + '\n'
        line_list[j+1] = line_list[j+1]+"2"+'\n'
    else:
        line_list[j] = "negative-" + str(i-310) + '\n' + str(len(line_list[j + 1]) - 1) + '\n'
        line_list[j + 1] = line_list[j + 1] + "1" + '\n'
# print(lengthlist)
diff_match_split = [line_list[i:i+124] for i in range(0,len(line_list),124)]
print(diff_match_split)

for i,j in zip(range(0,5),range(0,5)):
    with open('RACP%d.txt'% j,'w+') as temp:
        temp.write(str(124)+'\n')
        for line in diff_match_split [i]:
            temp.write(line)
        for line2 in diff_match_split[i+5]:
            temp.write(line2)
# with open('ACP4改.txt','w') as temp:
#     for line in lengthlist:
#         temp.write(line)
