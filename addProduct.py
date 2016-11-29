
name1 = []
product = []
name2 = []
feature1 = []
feature2 = []
feature3 = []
feature4 = []
feature5 = []
feature6 = []
txt1 = open("C:/Users/lenovo/Desktop/2.txt",'w')
for line in open("C:/Users/lenovo/Desktop/2.csv"):  
    name1.append(str(line.split(',')[8]).strip())
    product.append(str(line.split(',')[7]))
    
for line in open("C:/Users/lenovo/Desktop/1-123456-C2.csv"):
    name2.append(str(line.split(',')[0]))
    feature1.append(str(line.split(',')[1]))
    feature2.append(str(line.split(',')[2]))
    feature3.append(str(line.split(',')[3]))
    feature4.append(str(line.split(',')[4]))
    feature5.append(str(line.split(',')[5]))


for i in range(len(name2)):
    for j in range(len(name1)):
        if name2[i] == name1[j]:
            txt1.write(name2[i]+','+feature1[i]+','+feature2[i]+','+feature3[i]+','+feature4[i]+','+feature5[i]+','+product[j]+'\n')
    if name2[i] not in name1:
        txt1.write(name2[i]+','+feature1[i]+','+feature2[i]+','+feature3[i]+','+feature4[i]+','+feature5[i]+'\n')
txt1.close()
          