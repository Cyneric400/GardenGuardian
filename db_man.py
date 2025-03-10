import sqlite3
from plant import Plant

def add_item(pt: Plant):
    # get max id and set it as the next id to insert
    get_max_str = """SELECT MAX(id) FROM Plant"""
    with sqlite3.connect("db/db.db") as conn:
        cursor = conn.cursor()
        cursor.execute(get_max_str)
        curr_max_id = int(cursor.fetchone()[0])
        pt.set_id(curr_max_id+1)
        cursor.execute(f"""INSERT INTO Plant(id, species, schedule) VALUES
                    ({pt.id}, '{pt.species}', {pt.schedule});""")
        conn.commit()
        
def read_items() -> list[Plant]:
    # sort by id?
    sel_str = f"""SELECT * FROM Plant;"""
    with sqlite3.connect("db/db.db") as conn:
        cursor = conn.cursor()
        res = cursor.execute(sel_str)
        return res
    
if __name__ == "__main__":
    add_item(Plant("testing", 100, 10))