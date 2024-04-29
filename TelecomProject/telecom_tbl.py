import pymysql as sql

db = sql.connect(
    user='vicjnr',
    password='kevjnr7890',
    host='localhost',
    database='Telecom_db'
)

my_cur = db.cursor()

cre_tbl = '''
        create table Telecom_tbl(
        id int primary key auto_increment,
        First_name varchar(40) not null,
        Last_name varchar(40) not null,
        Phone_number varchar(11) not null unique,
        Airtime_balance decimal(15,2) not null,
        Data_balance decimal(15,2) not null,
        Airtime_borrowed_balance decimal(15,2) not null,
        Data_borrowed_balance decimal(15,2) not null
        )
'''

my_cur.execute(cre_tbl)
my_cur.close()
