
# print ('hello world')
# print ("navro'z")
# print (type (800))
# print (type (14.69))
# print(type("Notebook"))



# ism1="Umidjon"
# print(ism1)
# ism_familiya="Sotvoldiyev Umid"    snake case
# print(ism_familiya)
# IsmFamiliya="Sotvoldiyev Umid"       camel case
# print(IsmFamiliya)




# ism=input('iltimos ismingizni kiriting: ')
# print(ism)
# ism= "Umid"
# familiya= "Sotvoldiyev"
# print(f"Salom, mening ismim {familiya}. {ism} {familiya}!")




# ism=input("ismingizni kiriting:  ")
# print(f"assalomu alekum {ism}")



# meva= input ("sizning yoktirgan mevangiz:  ")
# print(f"mening yoktirgan mevam {meva}")



# ism="umidjon"
# print(ism.upper())



# familiya="SOTVOldiyev"
# print(familiya.lower())



# ism_familiya="sotvoldiyev umid navfalyevich"
# print(ism_familiya.title())



# ism_familiya="sotvoldiyev umid navfalyevich"
# print(ism_familiya.capitalize())



# ism_familiya=input("ism familiya kiriting:  ")
# print(f"assalomu alaykum {ism_familiya}")
# nomer=input("telefon nomeringiz:  ")
# print(f"mening nomerim {nomer}")



# ism=input("ismingiz:  ")
# familiya=input("familiyangiz:  ")
# nomer=input("tel nomeringiz:  ")
# print(f"assalomu alaykum {ism} {familiya}, sizning {nomer}")



# print("salom \ndunyo")
# print("salom \tdunyo")



# manzil=input("yashab turgan manzilingiz:   ")
# mashina=input("minib yurgan mashinez:  ")
# hayvon=input("uy xayvoningiz:  ")
# meva=input("yoktirgan mevangiz:  ")
# print(f" {manzil.title()} {mashina.upper()} {hayvon.title()} {meva.lower()}")



# matn="hello world"         # togri sanoq 0 dan boshlanadi
# print(matn[6])
# matn="hello world"           # teskari sanok -1 dan boshlanadi
# print(matn[-5])



# математические действия
#    + прибавить (plus)      10+10=20
#    - отнять (minus)        5-4=1
#    * умножить              5*5=25
#    / разделить             36/2=18
#    < Больше                a>b
#    > меньше                a<b
#    <= больше или равно     a>=b
#    >= меньше или равно     a<=b  
#    = присвоить             a=25
#    == если равно           8=8
#    != не равно             4!=1   5!=5
#    % взять остаток         8%3=2  12%5=2   7%6=1   6%3=0
#    // взять целую часть    10//3=3   5//2=2    6//3=2
#    ** степень              5**2=25   2**3=8 
# 
#   
#  
# часы=int(input("введите кол-во часов"))
# минуты=часы*60
# print(f"{часы} часов равно {минуты} минутам ")



# metr=int(input("metr kiriting:  ") )
# km=metr/1000
# print(f"{metr} metr {km} kilomertga teng")



# soat=int(input("soat kiriting:  "))
# minut=soat*60
# sekund=minut*60
# print(f"{soat} {minut} minutga {sekund} sekundga teng")



# yil=int(input("qachon tugilgansiz?  "))
# yosh=2022-yil
# print(f"siz {yosh} yoshdasiz")



# yosh=int(input("yoshingiz:  "))
# yil=2022-yosh
# print(f"siz {yil} yilda tugilgansiz")



# son=int(input("raqam kiriting:  "))
# print(son**2)



# raqam=int(input("raqam kiriting:  "))
# daraja=int(input("darajasini kiriting:  "))
# print(raqam**daraja)



#  Boolean ------- True, False
# print(4!=5) 
# print(8/2==5)



# a=int(input("raqam kiriting:  "))
# print(a>0)



# a=int(input("raqam kiriting:  "))      #juft sonlar ---- true     toq sonlar ------ false
# print(a%2==0)



# if else       #НОВАЯ ТЕМА
# a=5
# if a>10:
#     print("10 dan katta")
# else:
#     print("10 dan kichkina")



# a=20
# if a>10:
#     print("10 dan katta")
# else:
#     print("10 dan kichkina")



# raqam=int(input("raqam kiriting:  "))
# if raqam>0:
#     print("musbat")
# else:
#     print("manfiy")



# raqam=int(input("raqam kiriting:  "))
# if raqam%2==0:
#     print("juft")
# else:
#     print("toq")



# password=input("parol kiriting:  ")
# if password=="admin":
#     print("welcome admin")
# else:
#     print("welcome user")



# parol=str(input("mendan kattamisiz?  "))
# if parol=="ha" or parol=="xa":
#     print("akamsiz")
# else:
#     print("ukamsiz")



# javob=float(input("5x5 nechiga teng?  "))
# if javob!=25:
#     print("javob xato!")
# else:
#     print("togri")



# a=int(input("1-raqamni kiriting:  "))
# b=int(input("2-raqamni kiriting:  "))
# if a>b:
#     print(f"{a} katta {b} dan")
# else: 
#     print(f"{b} katta {a} dan")



# a=int(input("1-raqamni kiriting:  "))
# b=int(input("2-raqamni kiriting:  "))
# if a<b:
#     print(a)
#     print(b)
# else:
#     print(b)
#     print(a)



# yosh=int(input("yoshingizni kiriting:  "))
# if 6<=yosh<=18:
#     print("siz maktab oquvchisisiz")
# else:
#     print("maktabda oqimaysiz")



# a=int(input("1-raqamni kiriting:  "))
# b=int(input("2-raqamni kiriting:  "))
# if a==b:
#     print("ikkala son teng")
# else:
#     print("ikkala son teng emas")



#   НОВАЯ ТЕМA: list

# mevalar=["olma", "banan", "kivi"]     # matnli royxat
# narxlar=[500, 850, 4000]              # sonli royxat
# sonlar=["ikki", 450, "olti", 1000]    # aralash royxat
# ismlar=[]                             # bosh royxat



# mevalar=["olma", "banan", "kivi"]
# print(mevalar[2])


# mevalar=["olma", "banan", "kivi"]
# print(mevalar[-1].upper())


#        YANGI ELEMENTLAR QOSHISH

# ismlar=["ali", "doston", "jahongir"]
# ismlar.append("javohir")
# print(ismlar)



# mashinalar=[]
# a=input("1-mashinani yozing:  ")
# mashinalar.append(a)
# b=input("2-mashinani yozing:  ")
# mashinalar.append(b)
# c=input("3-mashinani yozing:  ")
# mashinalar.append(c)
# print(f"siz tanlagan mashinalar {mashinalar}")




# ismlar=["ali", "doston", "jahongir"]
# ismlar.insert(2, "javohir")
# print(ismlar)



# ismlar=["ali", "doston", "jahongir"]    # o'chirish
# ismlar.remove("doston")
# print(ismlar)



# ismlar=["ali", "doston", "jahongir"]   #index raqami bilan o'chirish
# del ismlar[2]
# print(ismlar)


# ismlar=["ali", "doston", "jahongir"]
# if "doston" in ismlar:
#     print("royxatda bor")
# else:
#     print("royhatda yoq")



# mashinalar=["spark", "aveo", "captiva", "damas"]
# mashina=input("mashina nomi:   ")
# if mashina in mashinalar:
#     print("mavjud")
# else:
#     print("tugab qolgan")



# mevalar=["gilos", "olma", "shaftoli"]
# meva=input("qaysi mevani qoshasiz:  ")
# son=int(input("qayerga qoshasiz:  "))
# mevalar.insert(son,meva)
# print(mevalar)



# mevalar=["gilos", "olma", "shaftoli"]
# meva=input("qaysi mevani qoshasiz:  ")
# if meva in mevalar:
#     print("ushbu meva mavjud")
# else:
#     son=int(input("qayerga qoshasiz?:  "))
#     mevalar.insert(son,meva)
#     print(mevalar)



# ismlar=["ali", "doston", "jahongir"]
# dost=input("dostingizni kiriting:  ")
# ismlar.append(dost)
# dushman=input("dushmaningiz:  ")
# ismlar.remove(dushman)
# print(ismlar)



# telefonlar=["iphone", "samsung", "redmi"]
# model=input("model kiriting:  ")
# if model in telefonlar:
#     telefonlar.remove(model)
#     print("ushbu model mavjud")
# else:
#     telefonlar.append(model)
# print(telefonlar)



# ismlar=["hasan", "husan", "olim"]
# a=input("ism kiriting:  ")
# if a in ismlar:
#     print("bu ism bor")
# else:
#     joy=int(input("qayerga:  "))
#     ismlar.insert(joy, a)
#     print(ismlar)



# ismlar=["hasan", "husan", "olim", "doston"]
# print(len(ismlar))



# a="kompyuter"
# print(len(a))



# ismlar=["hasan", "husan", "olim", "doston"]
# print(ismlar[0])
# print(ismlar[1:3])
# print(ismlar[1:])
# print(ismlar[:3])



# ismlar=["hasan", "husan", "olim", "doston"]
# del ismlar
# print(ismlar)



# ismlar=["hasan", "husan", "olim", "doston"]
# ismlar.clear()
# print(ismlar)



# ismlar=["hasan", "husan", "olim", "doston", "ali", "john"]
# ismlar.sort()         #можно добавить команду reverce=true в скобки после sort, чтобы сделать противоположность
# print(ismlar)


# raqamlar=[25, 85, 12, 96, 100, 56, 1, 3]
# raqamlar.sort()         #можно добавить команду reverce=true в скобки после sort, чтобы сделать противоположность
# print(raqamlar)        



# raqamlar=[25, 85, 12, 96, 100, 56, 1, 3]
# print(max(raqamlar))



# raqamlar=[25, 85, 12, 96, 100, 56, 1, 3]
# print(min(raqamlar))



# raqamlar=[25, 85, 12, 96, 100, 56, 1, 3]
# print(sum(raqamlar))



# parol=str(input("parolni kiriting:  "))
# if len(parol)==8:                #можно поменять знак перед 8 на необходимый, если хотим меньше 8 ставим <8 если больше >8
#     print("xush kelibsiz")
# else:
#     print("8 xonali kiriting")



# a=(input("raqam kiriting:  "))
# b=(input("raqam kiriting:  "))
# c=(input("raqam kiriting:  "))
# list=[a,b,c]
# print(max(list))



# a=(input("raqam kiriting:  "))
# b=(input("raqam kiriting:  "))
# c=(input("raqam kiriting:  "))
# d=(input("raqam kiriting:  "))
# list=[a, b, c, d]
# list.sort()
# print(list)
# print(list[-2])



# list=["dushanba", "seshanba", "chorshanba","payshanba", "juma",]
# kun=str(input("hafta kunini kiriting:  "))
# if kun in list:
#     print("ish kuni")
# else:
#     print("dam olish kuni")

# НОВАЯ ТЕМА   "elif"



# a=int(input('raqam kiriting:  '))
# if 10<a<99:
#     print('raqam 2 xonali')
# elif 99<a<999:
#     print('3 xonali')
# elif 999<a<9999:
#     print('4 xonali')
# else:
#     print('iltimos 4 xonadan katta raqam yozmeng')




# olma=int(input('nechta olma bor:  '))
# hajm=int(input('nechtadan solamiz:  '))
# a=olma//hajm    #tola yashik
# b=olma%hajm     #ortgan olma
# print(f'{a} yashik toldi, {b} ta olma ortib qoldi')



# yosh=int(input("Yoshingiz nechida?  "))
# if 0<yosh<7:
#     print("Bepul")
# elif 7<yosh<15:
#     print("1000 sum")
# elif 15<yosh<45:
#     print("2000 sum")
# elif 45<yosh<60:
#     print("1000 sum")
# elif 60<yosh<80:
#     print("Bepul")
# else:
#     print("error")



# a=int(input("1-sonni kiriting:  "))
# b=input("qanday amal bajaramiz:  ")
# c=int(input("2-sonni kiriting:  "))
# if b=="+":
#     print(f'{a} + {c} = {a+c} ')
# elif b=="-":
#     print(f"{a} - {c} = {a-c} ")
# elif b=="*":
#     print(f"{a} * {c} = {a*c} ")
# elif b=="/":
#     print(f"{a} / {c} = {a/c} ")



# x=float(input("x nuqtani kiriting:  "))
# y=float(input("y nuqtani kiriting:  "))
# if x>0 and y>0:
#     print("1-chorakda")
# elif x<0 and y>0:
#     print("2-chorakda")
# elif x<0 and y<0:
#     print("3-chorakda")
# elif x>0 and y<0:
#     print("4-chorakda")




# matn=input("faqat matn kiriting:  ")
# if matn.isalpha():                       # isalpha используется только тогда, когда пишите буквы, не используя цифры.
#     print("True")
# else:
#     print("raqam aralashdi")



# raqam=input("faqat raqam kiriting:  ")
# if raqam.isdigit():                      # isdigit используется только тогда, когда пишите цифры, не используя буквы.
#     print("True")
# else:
#     print("harf aralashdi")



# raqam=input("raqam kiriting:  ")   # 60A255DB
# if raqam[0:2].isdigit() and raqam[2].isalpha() and raqam[3:6].isdigit() and raqam[6:8].isalpha():
#     if raqam[0:2]=="01" or "10":
#         print("Tashkent")
#     elif raqam[0:2]=="60":
#         print("Andijon")
#     elif raqam[0:2]=="30":
#         print("Samarkand")
#     else:
#         print("Natogri raqam kiritingiz")
# else:
#     print("Xato")



# import random
# a=random.randint(1,100)
# print(a)



# import random
# a=random.randint(0, 10)
# b=int(input("1-urinish:  "))
# print(a)
# b=int(input("2-urinish:  "))
# print(a)
# if b==a:
#     print("tabriklaymiz")
# else:
#     print("topolmadiz")



# nomer=input("tel nomer kiriting:  ")
# if nomer[0:4]=="+998":
#     if len(nomer)==13:
#         if nomer[4:6]=="99" or nomer[4:6]=="95":
#             print("Uzmobile")
#         elif nomer[4:6]=="91" or nomer[4:6]=="90":
#             print("Beeline")
#         elif nomer[4:6]=="93" or nomer[4:6]=="94":
#             print("Ucell")
#         else:
#             print("nomalum operator")
#     else:
#         print("faqat 13 xonali nomer kiriting")
# else:
#     print("faqat UZB raqam kiriting")



#  НОВАЯ ТЕМА     "FOR"


# matn="kompyuter"
# for i in matn:
#     print(i)



# mevalar=["olma", "banan", "kiwi"]
# for meva in mevalar:
#     print(f"men yoqtirgan meva {meva}")



# for i in range(10):
#     print(i)


# for i in range(2,6):
#     print(i)


# for i in range(0,15,2):     #где значения в скобках: 1)старт, 2)стоп, 3)шаги
#     print(i)


# matn=input("matn yozing:  ")
# son=int(input("raqam kiriting:  "))
# for i in range(son):
#     print(matn)



# for i in range(1,20,2):
#     print(i)



# start=int(input("boshlangich:  "))
# stop=int(input("tugashi:  "))
# for i in range(start, stop):
#     if i%2!=0:
#         print(i)




# kg=int(input("necha kg olma olasiz:?  "))
# narx=int(input("necha puldan olasiz:?  "))
# for i in range(1,kg+1):
#     print(f"{i}kg olma {i*narx} sum")



# son=int(input("raqam kiriting:  "))
# for i in range(son+1):
#     print(i*str(i))



# a=int(input("1-raqam:  "))
# b=int(input("2-raqam:  "))
# c=1
# for i in range(a, b+1):
#     c=c*i
# print(c)


# matn=input("soz kiriting:  ")
# harf=input("harf kiriting:  ")
# c=0
# for i in matn:
#     if i==harf:
#         c=c+1
# print(c)




# unli=["a", "i", "e", "u", "o"]
# matn=input("kiriting:  ")
# sanovchi=0
# for i in matn:
#     if i in unli:
#         sanovchi=sanovchi+1
# print(sanovchi)



# unli=["a", "i", "e", "u", "o"]
# matn=input("kiriting:  ")
# sanovchi=0
# umumiy=len(matn)
# probel=0

# for i in matn:
#     if i in unli:
#         sanovchi=sanovchi+1
#         if i==" ":
#             probel=probel+1

# print(f"{sanovchi} ta unli, {umumiy-sanovchi-probel}ta undosh harf {probel} ta bosh joy bor")




# matn=input("matn kiriting:  ")
# yangi=input("qanday soz:  ")




# birinchi=input("birinchi sonni kiriting:  ")
# ikkinchi=input("ikkinchi sonni kiriting:  ")
# a=[]
# b=[]
# for i in birinchi:
#     a.append(i)
# for j in ikkinchi:
#     b.append(j)
# a.sort()
# b.sort()
# if a==b:
#     print("True")
# else:
#     print("False")


# 1-вариант

# word1 = input()
# word2 = input()
# flag = True
# dct1 = {}
# dct2 = {}

# for i in word1:
#     if dct1.get(i, False):
#         dct1[i] = dct1[i] + 1
#     else:
#         dct1[i] = 1

# for j in word2:
#     if dct2.get(j, False):
#         dct2[j] = dct2[j] + 1
#     else:
#         dct2[j] = 1

# for key in dct2.keys():
#     if dct1.get(key, False) != False:
#         if not dct1[key] >= dct2[key]:
#             flag = False
#     else:
#         flag = False
#     if not flag:
#         break
# print(flag)



# 2-вариант

# str1 = input()
# str2 = input()

# for char2 in str2:
#  notFound = True
#  if str2.count(char2) <= str1.count(char2):
#   notFound = False
#  if notFound:
#   break
# print("Составить", "не выйдет" if notFound else "получится")


# 3-вариант

# a=input("1-word:  ")
# b=input("2-word:  ")
# c=0
# for i in b:
#     if i in a:
#         c=c+1
# if c==len(b):
#     print(True)
# else:
#     print(False)



# НОВАЯ ТЕМА ----- DICTIONARY (Словари)



# thisdict={
#     "brand": "Ford",
#     "model": "Mustang",
#     "year": 1964
# }
# print(thisdict)



# thisdict={
#     "brand": "Ford",
#     "model": "Mustang",
#     "year": 1964
# }
# print(thisdict["brand"])



# thisdict={
#     "brand": "Ford",
#     "model": "Mustang",
#     "year": 1964
#     "colors": ["red", "white", "blue"]
# }
# print(thisdict)



# thisdict={
#     "brand": "Ford",
#     "model": "Mustang",
#     "year": 1964
# }
# x=thisdict.keys()
# print(x)



# car={
#     "brand": "Ford",
#     "model": "Mustang",
#     "year": 1964
# }
# x=car.keys()
# print(x)
# car["color"] = "white"
# print(x)



# thisdict={
#     "brand": "Ford",
#     "model": "Mustang",
#     "year": 1964
# }
# thisdict.update({"year": 2020})
# print(thisdict)



# thisdict={
#     "brand": "Ford",
#     "model": "Mustang",
#     "year": 1964
# }
# for x in thisdict:
#     print(thisdict[x])



# thisdict={
#     "brand": "Ford",
#     "model": "Mustang",
#     "year": 1964
# }
# for x, y in thisdict.items():
#     print(x, y)



# car = {
#     "brand": "Ford",
#     "model": "Mustang",
#     "year": 1964
# }
# x = car.get("model")
# print(x)



# my_family = {
#     "child_1" : {
#         "name" : "Emil",
#         "year" : 2004
#     },
#     "child_2" : {
#         "name" : "Tobias",
#         "year" : 2007 
#     },
#     "child_3" : {
#         "name" : "Linus",
#         "year" : 2011
#     }
# }
# print(my_family)



# a=input("davlat kiriting:  ")
# davlatlar={
#     "Uzb": "Toshkent",
#     "USA": "Vashinkton",
#     "Russ": "Moskow"
# }
# x = davlatlar.get(a)
# print(x)



# soz_1 = input("Sozni kiriting: ")
# print(f"Natija: {soz_1[::-1]}")



# while True:
#  soz_1 = input("Sozni kiriting: ")
#  print("Natija: {}\n".format(soz_1[::-1]))
#  if soz_1 == "exit":
#   break



# word = input()
# i = len(word) - 1
# new_word = ''
# while i >= 0:
#     new_word += word[i]
#     i -= 1

# print(new_word)



# string = input()[::-1];
# print(string)



# print((int(input()) + int(input()) ) / 2)



# def season(month):
#     if (9 <= month <= 11):
#         print("осень")
#     if (6 <= month <= 8):
#         print("лето")
#     if (3 <= month <= 5):
#         print("весна")
#     else: 
#         print("зима")
# while True:
#   try:
#     num=int(input("Номер:  "))
#     season(num)
#   except:
#     print("Введите число")



# def season (num):
#     if num == 12 or 1 <= num <= 2:
#         return 'Зима'
#     elif 3 <= num <= 5:
#         return 'Весна'
#     elif 6 <= num <= 8:
#         return 'Лето'
#     elif 9 <= num <= 11:
#         return 'Осень'
    
# num = int(input('Введите номер ммесяца: '))
# print(season(num))



# from unittest import result


# def f ():
#     return "privet"
# result = f()
# print(result)



# def season(month : int) -> None:
#   if month == 12 or month < 3:
#    print("Зима\n")
#   elif month == 3 or month < 6:
#    print("Весна\n")
#   elif month == 6 or month < 9:
#    print("Лето\n")
#   elif month == 9 or month < 12:
#    print("Осень\n")
#   else:
#    print("Введите число от 1 до 12")
# while True:
#  try:
#   num = int(input("Введите:  "))
#   season(num)
#  except:
#   print("Введите число")


