from tkinter import *
import tkinter.ttk as tk
from datetime import date
import urllib.request
import xml.dom.minidom
import pandas as pd
from pandas import DataFrame
import openpyxl
import time

import matplotlib
import matplotlib.pyplot as plt

# ЗАПРОС И ЧТЕНИЕ ВАЛЮТ
url = "http://www.cbr.ru/scripts/XML_daily.asp?date_req=22/04/2022"
response = urllib.request.urlopen(url)
dataset = response.read()
print(response)

#Парсинг , НЕ ТРОГАТЬ !!!
valute = list()
dom = xml.dom.minidom.parseString(dataset)
dom.normalize()
nodeArray = dom.getElementsByTagName("Valute")
for node in nodeArray:
    name = node.getElementsByTagName("Name")[0].firstChild.data
    count = node.getElementsByTagName("Nominal")[0].firstChild.data
    cost = node.getElementsByTagName("Value")[0].firstChild.data
    valute.append([name,count,cost])


#Редактируем значения для работы с валютами
for i in range(len(valute)):
    valute[i][2] = valute[i][2].replace(",",".",1)
    if int(valute[i][1]) > 1:
        valute[i][2] = str(float(float(valute[i][2]) / float(valute[i][1])))
        valute[i][1] = '1'
print(valute)

#Функция расчёта для 1 вкладки
def rasch(cmb1,cmb2):
    from_v = cmb1.get()
    to_v = cmb2.get()
    amount = float(window.get())

    cost1 = None
    cost2 = None

    for i in range(len(valute)):
        if(valute[i][0]==from_v):
            cost1 = float(valute[i][2])
        if(valute[i][0] == to_v):
            cost2 = float(valute[i][2])
    print(cost1)
    print(cost2)

    if cost1 is not None and cost2 is not None:
        res_amount = float((amount * cost1)/cost2)
        result.config(text = str(res_amount))
    else:
        result.config(text = "Error!")


def choose_file():
    data = None
    file_name = combobox3.get()
    if(file_name == "Австралийский доллар"):
        data = pd.read_excel("Australia.xlsx",engine="openpyxl")
    elif(file_name == "Азербайджанский манат"):
        data = pd.read_excel("Azerbaidjan.xlsx",engine="openpyxl")
    elif (file_name == "Фунт стерлингов Соединенного королевства"):
        data = pd.read_excel("United kingdom.xlsx",engine="openpyxl")
    elif (file_name == "Армянских драмов"):
        data = pd.read_excel("Armenia.xlsx",engine="openpyxl")
    elif (file_name == "Белорусский рубль"):
        data = pd.read_excel("Belarus.xlsx",engine="openpyxl")
    elif (file_name == "Болгарский лев"):
        data = pd.read_excel("Bolgaria.xlsx",engine="openpyxl")
    elif (file_name == "Бразильский реал"):
        data = pd.read_excel("Brazil.xlsx",engine="openpyxl")
    elif (file_name == "Канадский доллар"):
        data = pd.read_excel("Canada.xlsx",engine="openpyxl")
    elif (file_name == "Китайский юань"):
        data = pd.read_excel("China.xlsx",engine="openpyxl")
    elif (file_name == "Чешских крон"):
        data = pd.read_excel("Czech.xlsx",engine="openpyxl")
    elif (file_name == "Датская крона"):
        data = pd.read_excel("Dania.xlsx",engine="openpyxl")
    elif (file_name == "Евро"):
        data = pd.read_excel("Euro.xlsx",engine="openpyxl")
    elif (file_name == "Гонконгских долларов"):
        data = pd.read_excel("Honkong.xlsx",engine="openpyxl")
    elif (file_name == "Индийских рупий"):
        data = pd.read_excel("India.xlsx",engine="openpyxl")
    elif (file_name == "Японских иен"):
        data = pd.read_excel("Japan.xlsx",engine="openpyxl")
    elif (file_name == "Казахстанских тенге"):
        data = pd.read_excel("Kazahstan.xlsx",engine="openpyxl")
    elif (file_name == "Киргизских сомов"):
        data = pd.read_excel("Kirgizia.xlsx",engine="openpyxl")
    elif (file_name == "Вон Республики Корея"):
        data = pd.read_excel("Korea.xlsx",engine="openpyxl")
    elif (file_name == "Молдавских леев"):
        data = pd.read_excel("Moldavia.xlsx",engine="openpyxl")
    elif (file_name == "Норвежских крон"):
        data = pd.read_excel("Norway.xlsx",engine="openpyxl")
    elif (file_name == "Польский злотый"):
        data = pd.read_excel("Poland.xlsx",engine="openpyxl")
    elif (file_name == "Румынский лей"):
        data = pd.read_excel("Romania.xlsx",engine="openpyxl")
    elif (file_name == "СДР (специальные права заимствования)"):
        data = pd.read_excel("SDR.xlsx",engine="openpyxl")
    elif (file_name == "Сингапурский доллар"):
        data = pd.read_excel("Singapur.xlsx",engine="openpyxl")
    elif (file_name == "Шведских крон"):
        data = pd.read_excel("Sweden.xlsx",engine="openpyxl")
    elif (file_name == "Швейцарский франк"):
        data = pd.read_excel("Switzerland.xlsx",engine="openpyxl")
    elif (file_name == "Таджикских сомони"):
        data = pd.read_excel("Tajikiston.xlsx",engine="openpyxl")
    elif (file_name == "Турецкая лир"):
        data = pd.read_excel("Turkey.xlsx",engine="openpyxl")
    elif (file_name == "Украинских гривен"):
        data = pd.read_excel("Ukrain.xlsx",engine="openpyxl")
    elif (file_name == "Фунт стерлинг Соединенного королевства"):
        data = pd.read_excel("United kingdom.xlsx",engine="openpyxl")
    elif (file_name == "Доллар США"):
        data = pd.read_excel("USA.xlsx",engine="openpyxl")
    elif (file_name == "Узбекская сумов"):
        data = pd.read_excel("Uzbekiston.xlsx",engine="openpyxl")
    elif (file_name == "Венгерских форинтов"):
        data = pd.read_excel("Vengria.xlsx",engine="openpyxl")
    elif (file_name == "Южноафриканских рэндов"):
        data = pd.read_excel("Youth Afrika.xlsx",engine="openpyxl")
    else:
        print("Error!")
        exit(1)
    return data


def update_butn():
    if (radio_state.get() == 1):
        combobox4["values"] = ("Неделя2 - январь","Неделя3 - январь","Неделя4 - январь",
                               "Неделя1 - февраль","Неделя2 - февраль","Неделя3 - февраль","Неделя4 - февраль",
                               "Неделя1 - март","Неделя2 - март","Неделя3 - март","Неделя4 - март",
                               "Неделя1 - апрель","Неделя2 - апрель","Неделя3 - апрель","Неделя4 - апрель",
                               "Неделя1 - май","Неделя2 - май","Неделя3 - май","Неделя4 - май",
                               "Неделя1 - июнь","Неделя2 - июнь","Неделя3 - июнь","Неделя4 - июнь",
                               "Неделя1 - июль","Неделя2 - июль","Неделя3 - июль","Неделя4 - июль",
                               "Неделя1 - август","Неделя2 - август","Неделя3 - август","Неделя4 - август",
                               "Неделя1 - сентябрь","Неделя2 - сентябрь","Неделя3 - сентябрь","Неделя4 - сентябрь",
                               "Неделя1 - октябрь","Неделя2 - октябрь","Неделя3 - октябрь","Неделя4 - октябрь",
                               "Неделя1 - ноябрь","Неделя2 - ноябрь","Неделя3 - ноябрь","Неделя4 - ноябрь",
                               "Неделя1 - декабрь","Неделя2 - декабрь","Неделя3 - декабрь","Неделя4 - декабрь")
    elif (radio_state.get() == 2):
        combobox4["values"] = ("январь 2023", "февраль 2023", "март 2023", "апрель 2023",
                               "май 2023", "июнь 2023", "июль 2022", "август 2022", "сентябрь 2022",
                               "октябрь 2022", "ноябрь 2022", "декабрь 2022")
    elif (radio_state.get() == 3):
        combobox4["values"] = ("1 квартал", "2 квартал", "3 квартал")

    else:
        combobox4["values"] = ("2022", "2023")


def create_graph():
    x = []
    y = []
    amount_c = combobox3.get()
    period_c = combobox4.get()
    print(amount_c)
    print(period_c)
    data = choose_file()

    if (period_c == "2022"):
        x = pd.to_datetime(data["data"].values[124:],format="%Y-%m-%d")
        y = data["curs"].values[124:]
    elif(period_c == "2023"):
        x = pd.to_datetime(data["data"].values[2:123],format="%Y-%m-%d")
        y = data["curs"].values[2:123]

    elif (period_c == "декабрь 2022"):
        x = pd.to_datetime(data["data"].values[124:146],format="%Y-%m-%d")
        y = data["curs"].values[124:146]

    elif (period_c == "ноябрь 2022"):
        x = pd.to_datetime(data["data"].values[147:167],format="%Y-%m-%d")
        y = data["curs"].values[147:167]

    elif (period_c == "октябрь 2022"):
        x = pd.to_datetime(data["data"].values[168:188],format="%Y-%m-%d")
        y = data["curs"].values[168:188]

    elif (period_c == "сентябрь 2022"):
        x = pd.to_datetime(data["data"].values[189:210],format="%Y-%m-%d")
        y = data["curs"].values[189:210]

    elif (period_c == "август 2022"):
        x = pd.to_datetime(data["data"].values[211:231],format="%Y-%m-%d")
        y = data["curs"].values[211:231]

    elif (period_c == "июль 2022"):
        x = pd.to_datetime(data["data"].values[232:254],format="%Y-%m-%d")
        y = data["curs"].values[124:146]

    elif (period_c == "июнь 2023"):
        x = pd.to_datetime(data["data"].values[2:27],format="%Y-%m-%d")
        y = data["curs"].values[124:146]

    elif (period_c == "май 2023"):
        x = pd.to_datetime(data["data"].values[28:46],format="%Y-%m-%d")
        y = data["curs"].values[28:46]

    elif (period_c == "апрель 2023"):
        x = pd.to_datetime(data["data"].values[47:67],format="%Y-%m-%d")
        y = data["curs"].values[47:67]

    elif (period_c == "март 2023"):
        x = pd.to_datetime(data["data"].values[68:89],format="%Y-%m-%d")
        y = data["curs"].values[68:89]

    elif (period_c == "февраль 2023"):
        x = pd.to_datetime(data["data"].values[90:107],format="%Y-%m-%d")
        y = data["curs"].values[90:107]

    elif (period_c == "яенварь 2023"):
        x = pd.to_datetime(data["data"].values[108:123],format="%Y-%m-%d")
        y = data["curs"].values[108:123]

    elif (period_c == "1 квартал"):
        x = pd.to_datetime(data["data"].values[2:89],format="%Y-%m-%d")
        y = data["curs"].values[2:89]

    elif (period_c == "2 квартал"):
        x = pd.to_datetime(data["data"].values[90:167],format="%Y-%m-%d")
        y = data["curs"].values[90:167]

    elif (period_c == "3 квартал"):
        x = pd.to_datetime(data["data"].values[168:254],format="%Y-%m-%d")
        y = data["curs"].values[168:254]

    elif (period_c == "Неделя2 - январь"):
        x = pd.to_datetime(data["data"].values[118:123],format="%Y-%m-%d")
        y = data["curs"].values[118:123]
    elif (period_c == "Неделя3 - январь"):
        x = pd.to_datetime(data["data"].values[112:117],format="%Y-%m-%d")
        y = data["curs"].values[112:117]
    elif (period_c == "Неделя4 - январь"):
        x = pd.to_datetime(data["data"].values[108:111],format="%Y-%m-%d")
        y = data["curs"].values[108:111]
    elif (period_c == "Неделя1 - декабрь"):
        x = pd.to_datetime(data["data"].values[142:146],format="%Y-%m-%d")
        y = data["curs"].values[142:146]
    elif (period_c == "Неделя2 - декабрь"):
        x = pd.to_datetime(data["data"].values[136:141],format="%Y-%m-%d")
        y = data["curs"].values[136:141]
    elif (period_c == "Неделя3 - декабрь"):
        x = pd.to_datetime(data["data"].values[130:135],format="%Y-%m-%d")
        y = data["curs"].values[130:135]
    elif (period_c == "Неделя4 - декабрь"):
        x = pd.to_datetime(data["data"].values[124:129],format="%Y-%m-%d")
        y = data["curs"].values[124:129]
    elif (period_c == "Неделя1 - ноябрь"):
        x = pd.to_datetime(data["data"].values[164:167],format="%Y-%m-%d")
        y = data["curs"].values[164:167]
    elif (period_c == "Неделя2 - ноябрь"):
        x = pd.to_datetime(data["data"].values[158:163],format="%Y-%m-%d")
        y = data["curs"].values[158:163]
    elif (period_c == "Неделя3 - ноябрь"):
        x = pd.to_datetime(data["data"].values[152:157],format="%Y-%m-%d")
        y = data["curs"].values[152:157]
    elif (period_c == "Неделя4 - ноябрь"):
        x = pd.to_datetime(data["data"].values[147:151],format="%Y-%m-%d")
        y = data["curs"].values[147:151]
    elif (period_c == "Неделя1 - октябрь"):
        x = pd.to_datetime(data["data"].values[184:188],format="%Y-%m-%d")
        y = data["curs"].values[184:188]
    elif (period_c == "Неделя2 - октябрь"):
        x = pd.to_datetime(data["data"].values[178:183],format="%Y-%m-%d")
        y = data["curs"].values[178:183]
    elif (period_c == "Неделя3 - октябрь"):
        x = pd.to_datetime(data["data"].values[172:177],format="%Y-%m-%d")
        y = data["curs"].values[172:177]
    elif (period_c == "Неделя4 - октябрь"):
        x = pd.to_datetime(data["data"].values[168:171],format="%Y-%m-%d")
        y = data["curs"].values[168:171]
    elif (period_c == "Неделя1 - сентябрь"):
        x = pd.to_datetime(data["data"].values[206:210],format="%Y-%m-%d")
        y = data["curs"].values[206:210]
    elif (period_c == "Неделя2 - сентябрь"):
        x = pd.to_datetime(data["data"].values[200:205],format="%Y-%m-%d")
        y = data["curs"].values[200:205]
    elif (period_c == "Неделя3 - сентябрь"):
        x = pd.to_datetime(data["data"].values[194:199],format="%Y-%m-%d")
        y = data["curs"].values[194:199]
    elif (period_c == "Неделя4 - сентябрь"):
        x = pd.to_datetime(data["data"].values[189:193],format="%Y-%m-%d")
        y = data["curs"].values[189:193]
    elif (period_c == "Неделя1 - август"):
        x = pd.to_datetime(data["data"].values[227:232],format="%Y-%m-%d")
        y = data["curs"].values[227:232]
    elif (period_c == "Неделя2 - август"):
        x = pd.to_datetime(data["data"].values[221:226],format="%Y-%m-%d")
        y = data["curs"].values[221:226]
    elif (period_c == "Неделя3 - август"):
        x = pd.to_datetime(data["data"].values[215:220],format="%Y-%m-%d")
        y = data["curs"].values[215:220]
    elif (period_c == "Неделя4 - август"):
        x = pd.to_datetime(data["data"].values[211:214],format="%Y-%m-%d")
        y = data["curs"].values[211:214]
    elif (period_c == "Неделя1 - июль"):
        x = pd.to_datetime(data["data"].values[250:254],format="%Y-%m-%d")
        y = data["curs"].values[250:254]
    elif (period_c == "Неделя2 - июль"):
        x = pd.to_datetime(data["data"].values[245:249],format="%Y-%m-%d")
        y = data["curs"].values[245:249]
    elif (period_c == "Неделя3 - июль"):
        x = pd.to_datetime(data["data"].values[240:244],format="%Y-%m-%d")
        y = data["curs"].values[240:244]
    elif (period_c == "Неделя4 - июль"):
        x = pd.to_datetime(data["data"].values[233:239],format="%Y-%m-%d")
        y = data["curs"].values[233:239]
    elif (period_c == "Неделя1 - июнь"):
        x = pd.to_datetime(data["data"].values[23:27],format="%Y-%m-%d")
        y = data["curs"].values[23:27]
    elif (period_c == "Неделя2 - июнь"):
        x = pd.to_datetime(data["data"].values[18:22],format="%Y-%m-%d")
        y = data["curs"].values[18:22]
    elif (period_c == "Неделя3 - июнь"):
        x = pd.to_datetime(data["data"].values[12:17],format="%Y-%m-%d")
        y = data["curs"].values[12:17]
    elif (period_c == "Неделя4 - июнь"):
        x = pd.to_datetime(data["data"].values[7:11],format="%Y-%m-%d")
        y = data["curs"].values[7:11]
    elif (period_c == "Неделя1 - май"):
        x = pd.to_datetime(data["data"].values[43:46],format="%Y-%m-%d")
        y = data["curs"].values[43:46]
    elif (period_c == "Неделя2 - май"):
        x = pd.to_datetime(data["data"].values[39:42],format="%Y-%m-%d")
        y = data["curs"].values[39:42]
    elif (period_c == "Неделя3 - май"):
        x = pd.to_datetime(data["data"].values[34:38],format="%Y-%m-%d")
        y = data["curs"].values[34:38]
    elif (period_c == "Неделя4 - май"):
        x = pd.to_datetime(data["data"].values[28:33],format="%Y-%m-%d")
        y = data["curs"].values[28:33]
    elif (period_c == "Неделя1 - апрель"):
        x = pd.to_datetime(data["data"].values[63:67],format="%Y-%m-%d")
        y = data["curs"].values[63:67]
    elif (period_c == "Неделя2 - апрель"):
        x = pd.to_datetime(data["data"].values[57:62],format="%Y-%m-%d")
        y = data["curs"].values[57:62]
    elif (period_c == "Неделя3 - апрель"):
        x = pd.to_datetime(data["data"].values[51:56],format="%Y-%m-%d")
        y = data["curs"].values[51:56]
    elif (period_c == "Неделя4 - апрель"):
        x = pd.to_datetime(data["data"].values[47:50],format="%Y-%m-%d")
        y = data["curs"].values[47:50]
    elif (period_c == "Неделя1 - март"):
        x = pd.to_datetime(data["data"].values[85:89],format="%Y-%m-%d")
        y = data["curs"].values[85:89]
    elif (period_c == "Неделя2 - март"):
        x = pd.to_datetime(data["data"].values[79:84],format="%Y-%m-%d")
        y = data["curs"].values[79:84]
    elif (period_c == "Неделя3 - март"):
        x = pd.to_datetime(data["data"].values[78:83],format="%Y-%m-%d")
        y = data["curs"].values[78:83]
    elif (period_c == "Неделя4 - март"):
        x = pd.to_datetime(data["data"].values[68:72],format="%Y-%m-%d")
        y = data["curs"].values[68:72]
    elif (period_c == "Неделя1 - февраль"):
        x = pd.to_datetime(data["data"].values[103:107],format="%Y-%m-%d")
        y = data["curs"].values[103:107]
    elif (period_c == "Неделя2 - февраль"):
        x = pd.to_datetime(data["data"].values[97:102],format="%Y-%m-%d")
        y = data["curs"].values[97:102]
    elif (period_c == "Неделя3 - февраль"):
        x = pd.to_datetime(data["data"].values[92:96],format="%Y-%m-%d")
        y = data["curs"].values[92:96]
    elif (period_c == "Неделя4 - февраль"):
        x = pd.to_datetime(data["data"].values[90:91],format="%Y-%m-%d")
        y = data["curs"].values[90:91]


    return x,y

def plot_graph():
    x,y = create_graph()
    plt.plot(x,y)
    plt.grid(True)
    canvas.draw()
    time.sleep(1)
    fig.clear()



#НАСТРОЙКА ИНТЕРФЕЙСА
root = Tk()
root.geometry("1000x700")
root.title("Binance")
root.resizable(width = False , height = False)

table = tk.Notebook(root)

tab1 = Frame(table)
table.add(tab1, text = "Конвертор")
combobox1 = tk.Combobox(tab1)
#Не изменять названия ! Парсер ломается.
combobox1["values"] = ("Австралийский доллар","Азербайджанский манат","Фунт стерлингов Соединенного королевства","Армянских драмов" ,
                       "Белорусский рубль","Болгарский лев","Бразильский реал","Венгерских форинтов","Гонконгских долларов",
                       "Датская крона","Доллар США","Евро","Индийских рупий","Казахстанских тенге","Канадский доллар",
                       "Киргизских сомов","Китайский юань","Молдавских леев","Норвежских крон","Польский злотый","СДР (специальные права заимствования)","Румынский лей",
                       "Сингапурский доллар","Таджикских сомони","Турецкая лир","Новый туркменский манат","Узбекская сумов","Украинских гривен","Чешских крон",
                       "Шведских крон","Швейцарский франк","Южноафриканских рэндов","Вон Республики Корея" ,"Японских иен")

combobox2 = tk.Combobox(tab1)
#Не изменять названия ! Парсер ломается.
combobox2["values"] = ("Австралийский доллар","Азербайджанский манат","Фунт стерлингов Соединенного королевства","Армянских драмов" ,
                       "Белорусский рубль","Болгарский лев","Бразильский реал","Венгерских форинтов","Гонконгских долларов",
                       "Датская крона","Доллар США","Евро","Индийских рупий","Казахстанских тенге","Канадский доллар",
                       "Киргизских сомов","Китайский юань","Молдавских леев","Норвежских крон","Польский злотый","СДР (специальные права заимствования)","Румынский лей",
                       "Сингапурский доллар","Таджикских сомони","Турецкая лир","Новый туркменский манат","Узбекская сумов","Украинских гривен","Чешских крон",
                       "Шведских крон","Швейцарский франк","Южноафриканских рэндов","Вон Республики Корея" ,"Японских иен")

window = Entry(tab1 , width = 20)
button = Button(tab1 , text = "Рассчитать",width=10,height=1,command = lambda: rasch(combobox1,combobox2))
result = Label(tab1 , text = "Nothng")

window.focus()
combobox1.current(0)
combobox2.current(1)

result.grid(row = 2, column = 1 , padx = 20)
button.grid(row = 1 , column = 2, padx = 20)
window.grid(row = 1, column = 1,padx = 20)
combobox1.grid(row = 1 , column = 0, pady = 10)
combobox2.grid(row = 2, column = 0, pady = 20)

tab2 = Frame(table)
table.add(tab2, text = "Динамика курса")

combobox3 = tk.Combobox(tab2)
#Не изменять названия ! Парсер ломается.
combobox3["values"] = ("Австралийский доллар","Азербайджанский манат","Фунт стерлингов Соединенного королевства","Армянских драмов" ,
                       "Белорусский рубль","Болгарский лев","Бразильский реал","Венгерских форинтов","Гонконгских долларов",
                       "Датская крона","Доллар США","Евро","Индийских рупий","Казахстанских тенге","Канадский доллар",
                       "Киргизских сомов","Китайский юань","Молдавских леев","Норвежских крон","Польский злотый","СДР (специальные права заимствования)","Румынский лей",
                       "Сингапурский доллар","Таджикских сомони","Турецкая лир","Новый туркменский манат","Узбекская сумов","Украинских гривен","Чешских крон",
                       "Шведских крон","Швейцарский франк","Южноафриканских рэндов","Вон Республики Корея" ,"Японских иен")

title1 = Label(tab2 , text = "Валюта")
title2 = Label(tab2 , text = "Период")
title3 = Label(tab2 , text = "Выбор периода")


combobox4 = tk.Combobox(tab2)
radio_state = IntVar()
radio_state.set(4)
radio1 = Radiobutton(tab2 , text = "Неделя",value = 1,variable = radio_state,command = lambda : update_butn())
radio2 = Radiobutton(tab2 , text = "Месяц",value = 2,variable = radio_state,command=lambda : update_butn())
radio3 = Radiobutton(tab2 , text = "Квартал",value = 3,variable = radio_state,command=lambda : update_butn())
radio4 = Radiobutton(tab2 , text = "Год",value = 4,variable = radio_state,command=lambda : update_butn())

button2 = Button(tab2 , text = "Построить график",width=20,height=1 , command= lambda : plot_graph())


combobox3.current(0)
combobox4.current()

title1.grid(row = 1 , column = 0 , pady = 10, padx = 50)
combobox3.grid(row = 2 , column = 0 , pady = 10 , padx = 50)
title2.grid(row = 1 , column = 1 , pady = 10, padx = 50)
radio1.grid(row = 2 , column = 1 , pady = 3 , padx = 50)
radio2.grid(row = 3 , column = 1 , pady = 3 , padx = 50)
radio3.grid(row = 4 , column = 1 , pady = 3 , padx = 50)
radio4.grid(row = 5 , column = 1 , pady = 3 , padx = 50)
title3.grid(row = 1 , column = 2 , pady = 10 , padx = 50)
combobox4.grid(row = 2, column = 2 , pady = 10 , padx= 50 )
button2.grid(row = 3 , column = 0 ,pady = 10 ,padx=50)

table.grid(row = 0 , column = 0)

matplotlib.use("TkAgg")
fig = plt.figure(figsize=(6, 3))
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=tab2)
plot_widget = canvas.get_tk_widget()
plot_widget.grid(row=6, column=0, pady=40)

# ЗАПУСК ПРОГРАММЫ
if __name__ == "__main__":
     root.mainloop()
