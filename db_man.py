import sqlite3
from plant import Plant
from datetime import date


def add_item(pt: Plant):
    # get max id and set it as the next id to insert
    get_max_str = """SELECT MAX(id) FROM Plant"""
    with sqlite3.connect("db/db.db") as conn:
        cursor = conn.cursor()
        cursor.execute(get_max_str)
        max_raw = cursor.fetchone()[0]
        curr_max_id = int(max_raw) if max_raw else 0
        pt.set_id(curr_max_id+1)
        cursor.execute(f"""INSERT INTO Plant(id, species, schedule) VALUES
                    ({pt.id}, '{pt.species}', {pt.schedule});""")
        conn.commit()


def read_items():
    # sort by id?
    sel_str = f"""SELECT * FROM Plant;"""
    with sqlite3.connect("db/db.db") as conn:
        cursor = conn.cursor()
        cursor.execute(sel_str)
        res = cursor.fetchall()
        return res


def read_log(id: int) -> date:
    sel_str = f"""SELECT MAX(day) FROM Log WHERE id={id}"""
    with sqlite3.connect("db/db.db") as conn:
        cursor = conn.cursor()
        cursor.execute(sel_str)
        res = cursor.fetchone()
        print(res)
        return res if res != (None,) else 0


def update_log(p: Plant):
    ins_str = f"""INSERT INTO Log VALUES ({p.id}, {p.last_watered}"""
    with sqlite3.connect("db/db.db") as conn:
        cursor = conn.cursor()
        cursor.execute(ins_str)
        conn.commit()


if __name__ == "__main__":
    add_item(Plant("testing", 100, 10))