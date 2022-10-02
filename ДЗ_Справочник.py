import pymysql
from auxiliary import host, user, password, db

connection = pymysql.connect(host = host,
                            user = user,
                            password = password,
                            db = db)
###############################
def select():
    with connection.cursor() as cursor:
        cursor = connection.cursor()
        cursor.execute("select * from individuals")
        rows = cursor.fetchall()

    return rows
def search():
    d = input("Для поиска абонента ведите фамилию: \n")
    with connection.cursor() as cursor:
        sel_query = "select * from individuals where lastname LIKE '%s'"%(d+'%')
        cursor.execute(sel_query)
        rows = cursor.fetchall()
        if len(rows) == 0:
            return "Не найден в справочнике"
        else:
            return rows

#print(search())

def insert(lastname,firstname,middlename,company,work_phone,cellular_phone,email):
    params = (lastname,firstname,middlename,company,work_phone,cellular_phone,email)
    with connection.cursor() as cursor:
        cursor = connection.cursor()
        cursor.execute("""INSERT ignore INTO individuals (lastname, firstname, middlename, company, work_phone, cellular_phone, email) VALUES(%s,%s,%s,%s,%s,%s,%s)""", params)
        connection.commit()
        return "Вставили"

def delete(id):
    with connection.cursor() as cursor:
        del_query = "delete from individuals where id='%s'"%(id+'%')
        cursor.execute(del_query)
        connection.commit()
    return "Удаление выполнено"
#####################################################

print("Телефонный справочник")
prompt = "Выберите одну из команд: 1 - если хотите вывести записи ввиде строки \n                         " \
             "2 - если хотите получить записи ввиде списка \n"
q = int(input(prompt))
for i in select():
    if q == 1:
        print (*i, end = '\n')
    else:
        print(i[0], i[1], i[2], i[3])
        print(i[4])
        print(i[5], i[6], sep = ', ')
        print(i[7])
        print()

if type(search())==str:
    h=input("Добавить запись в справочник? да/нет: \n")
    if h == 'да':
        lastname = input("Введите фамилию: ")
        firstname = input("Введите имя: ")
        middlename = input("Введите отчество: ")
        company = input("Введите название компании: ")
        work_phone = input("Введите номер рабочего телефона: ")
        cellular_phone = input("Введите номер сотового телефона: ")
        email = input("Введите электронный адрес: ")
        insert(lastname,firstname,middlename,company,work_phone,cellular_phone,email)

    input("Нажмите Enter для выхода!")
else:
    print(search())


