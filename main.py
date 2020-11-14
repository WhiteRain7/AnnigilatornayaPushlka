Stat =[]    # Заполняется в пункте 2 в виде:
            # ['специальность', число вакансий, число упоминаний в 2020, ч.у. в 2019]
            
LI = []     # Заполняется "сырым" текстом из файла (а файл - тз интернета)
            # и переводит в п.1 ['к', 'такому', 'виду,', 'по', 'одному', 'слову']

# Pr - это список специальностей, по которому программа ищет совпадения в п.2
Pr = ['Web-программист','SEO-специалист','SMM-специалист','Контент-менеджер',
      'копирайтер','линкбилдер','Link-менеджер','Web-аналитик','юзабилист',
      'вестальщик','модератор','таргетолог','контекстолог','IT-евангелист',
      'тимлид','front-end разработчик','back-end разработчик','embedded-программист',
      'QA-инженер','тестировщик','разработчик баз данных','системный аналитик','gamedev',
      'гейм-девелопер','android-разработчик','iOS-разработчик','IT-менеджер', 'системный администратор', 'программист 1C','дизайнер','гейм-дизайнер', '']

TmpP = []  # TmpP и TmpL используются в п.2, для посимвольного хранения
TmpL = []  # слов из Pr и LI соответственно, чтобы их сравнить и добавить в Stat,
           # если слова примерно одинаковые (меньше 3-х "ошибок")

Mnt = [0,0,0,0,0,0,0]
#----------------------------------------- 1

f = open ('WebInRes.txt','r')
for line in f:
    a = line
    i = 0
    for i in a:
        LI.append(i)
f.close()

a = b = 0

while (b!=len(LI)-1):
    b = b + 1
    while (LI[b]!=' ') and (b!=len(LI)-1) and (LI[b]!='\n') and (LI[b]!='.'):
        LI[a]=LI[a]+LI[b]
        b = b + 1
    a = a + 1
    LI[a] = ''
LI[a:len(LI)] = ''
#LI.append('end_file')
LI.append('')

#----------------------------------------- 2

a = b = c = d = ''
i = 0
vac = sp = 0
date = -1

for a in Pr:
    i = sp = 0
    TmpP[:] = ''
    for c in a:
        TmpP.append(c)
        if c == ' ':
            sp = sp + 1
    for b in LI:
        if b == 'finalendofthetext': break
        if b == 'eott2020': date = 0
        if b == 'eott2019': date = 1
        if b == 'eott2018': date = 2
        if b == 'eott2017': date = 3
        if b == 'eott2016': date = 4
        if b == 'eott2015': date = 5
        if b == 'eott2014': date = 6
        n = 0
        i = i + 1
        TmpL[:] = ''
        for c in b: TmpL.append(c)
        i2 = i
        sp2 = sp
        while (sp2 > 0) and (i2!=len(LI)):
            TmpL.append(' ')
            for c in LI[i2]: TmpL.append(c)
            i2 = i2 + 1
            if i2==len(LI): break
            sp2 = sp2 - 1
        sp2 = sp
        i2 = i
        if (len(TmpP) < len(TmpL)):
            while len(TmpP)<len(TmpL): TmpP.append(' ')
        elif (len(TmpP)>len(TmpL)):
            while len(TmpP)>len(TmpL): TmpL.append(' ')
        for c in range(len(TmpL)):
            if TmpP[c]!=TmpL[c]: n = n + 1
        if n > 3: continue
        elif n<4: Mnt[date] = Mnt[date] + 1
    if (Mnt[0]!=0)or(Mnt[1]!=0)or(Mnt[2]!=0)or(Mnt[3]!=0)or(Mnt[4]!=0)or(Mnt[5]!=0)or(Mnt[6]!=0):
        Stat.append([str(a),Mnt[6],Mnt[5],Mnt[4],Mnt[3],Mnt[2],Mnt[1],Mnt[0]])
        Mnt[0] = Mnt[1] = Mnt[2] = Mnt[3] = Mnt[4] = Mnt[5] = Mnt[6] = 0

#print(Stat)

# Здесь начинается Франкенштейн

new_massiv = []
for i in range(0,len(Stat)):
	#print(Stat[i][0])
	new_massiv.append([[Stat[i][0]], [], [0,0,0],0])
	count = len(Stat[i])-1
	for j in range(0,count-2):
		zn = (Stat[i][j+1] + Stat[i][j+2] + Stat[i][j+3]) // 3
		new_massiv[i][1].append(zn)
		#print(2016+j, ":" ,new_massiv[i][1][j])
		new_massiv[i][3] += Stat[i][j+1]
	new_massiv[i][3] += Stat[i][count-2]
	new_massiv[i][3] += Stat[i][count-1]
	new_count = len(new_massiv[i][1])
	X = (1 + new_count) / 2 # x среднее
	sumof = sum(new_massiv[i][1])
	Y = sumof / new_count # y среднее
	xxcp = 0
	xy = 0
	for x in range(0, new_count):
		y = new_massiv[i][1][x]
		xX = x - X
		xxcp = xxcp + xX
		xy = xy + xX * (y - Y)
		#for j in range(0, new_count):
		#  xy = xy + (j - X) * (y - Y)
	b = xy / (xxcp * xxcp)
	a = Y - b * X
	#print(a, b)
	#print("/// прогнозы")
	new_massiv[i][2][0] = (a + b * (new_count+1))
	new_massiv[i][2][1] = (a + b * (new_count+2))
	new_massiv[i][2][2] = (a + b * (new_count+3))
	#print("2021 :", int (a + b * (new_count+1)) //1)
	#print("2022 :", int (a + b * (new_count+2)) //1)
	#print("2023 :", int (a + b * (new_count+3)) //1)
	#print()
print("Десять самых приоритетных:")
new_massiv.sort(key=lambda item: -item[2][0] -item[2][1] -item[2][2] -item[3]) 
for i in range(1, len(new_massiv)):
	print(i,new_massiv[i][0][0])
	if (i==10):
		print("Остальные профессии:")
	if (i==len(new_massiv)-6):
		print("Пять самых не приоритетных:")