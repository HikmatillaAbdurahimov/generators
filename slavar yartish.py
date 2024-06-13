import psycopg2
import os
from dotenv import load_dotenv
from typing import Optional
from googletrans import Translator

load_dotenv()
with psycopg2.connect(
    database=os.getenv('database'),password=os.getenv('password'),
    user=os.getenv('user'),host=os.getenv('host'),port=os.getenv('port')
) as conn:
    with conn.cursor() as cur:
        def create_table():
            create_table_query="""
            create table slavar(
            id              serial primary key,
            ozbek           varchar(1000),
            ingliz          varchar(1000),
            turkiya         varchar(1000),
            create_at       time default current_time
            );"""
            cur.execute(create_table_query)
            conn.commit()
            print("slavar jadvali yaratildi")

        def insert():
            tarjimon = Translator()  # Translator bu maxsus klass (tarjimon esa obyekt)
            matn_uz =input("matn yoki so'zni krting ==>:")
            tarjima_tr = tarjimon.translate(matn_uz,dest='tr')
            tarjima_eng=tarjimon.translate(matn_uz,dest='en')
            en=tarjima_eng.text
            tr=tarjima_tr.text
            insert_into_query="""
            insert into slavar(ozbek,ingliz,turkiya)
            values (%s,%s,%s);"""
            cur.execute(insert_into_query,(matn_uz,en,tr))
            conn.commit()
            runserver=input("""
                  shahsi slavaringizga so'z qo'shishni istaysizmi
                               1.ha
                               2.yo'q
                                 ==>""")
            if runserver=="1":
                return insert()
            else:
                return run()

        def select():
            select_query="""
            select * from slavar order by id asc ;"""
            cur.execute(select_query)
            data=cur.fetchall()
            for i in data:
                print(i)
            baza=input("""
                   bazaga qaytish
                       1. ha
                         ==> """)
            if baza=="1":
                return run()

        def run():
            runser=input("""
                 1.jadval yartish
                 2.malumot qo'shish
                 3.malumotlarni ko'rish
                     ==>:""")
            if runser=="1":
                return create_table()
            elif runser=="2":
                return insert()
            elif runser=="3":
                return select()
            else:
                print(f"{runser} bunday malumot topilmadi")
        if __name__=="__main__":
            run()



















