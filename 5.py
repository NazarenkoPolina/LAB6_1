def zdh1():
 coun = {"Австрия": "Вена", "Бельгия": "Брюссель", "Великобритания": "Лондон", "Германия": "Берлин", "Ирландия": "Дублин", "Лихтенштейн": "Вадуц", "Нидерладны": "Амстердам",
                 "Франция": "Париж", "Белоруссия": "Минск", "Болгария": "София", "Польша": "Варшава", "Чехия": "Прага", "Албания": "Тирана", "Босния и Герцеговина": "Сараево",
                 "Северная Македония": "Скопье", "Сербия": "Белград"}
 print(coun)
 print(coun["Франция"])
 for key in sorted(coun):
    print(key, "-", coun[key])
def zdh2():
    alp =  {
        "авеинорст" : 1,
        "дклмпу" : 2,
        "бгёья" : 3,
        "йы" : 4,
        "жзхцч" : 5,
        "шэю" : 8,
        "фщъ" : 10
     }
    sum = 0
    word = input('Введите слово')
    for i in word:
        sum += alp[i.lower()]
    print('Сумма:',sum)

def zdh3():
 le = ['рус', 'англ', 'китай']
 sp = {'рус': ['финкельберг', 'телятникова','шамбурова','рахимов','назаренко'],
      'англ': ['финкельберг','телятникова','рахимов','шамбурова','гумерова'],
      'китай': ['финкельберг', 'гумерова','рахимов','назаренко']}
 le.sort()
 s = len(le)
 print('Количество языков' ,s)
 print('Список по алфавиту',le)
 print('Введите любой язык из списка')
 a = str(input())
 print(sp[a])

 zdh1()
 zdh2()
 zdh3()