import netcon as nc
import sqlite3
import os

global db_name
global dir
base_dir = os.getcwd()
dir = base_dir+"/PYCON"
db_name = "True_colors.db"

def create_new_database():
    os.chdir(dir)
    conn = sqlite3.connect(r'True_colors.db')
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE fabric_entry(fabric_id INTEGER PRIMARY KEY, client_name text TEXT NOT NULL,work_role TEXT NOT NULL,fabric_type TEXT NOT NULL,fabric_amount INTEGER NOT NULL)")
    cursor.execute("CREATE TABLE design(fabric_id INTEGER,pic blob,PRIMARY KEY (fabric_id),FOREIGN KEY (fabric_id) REFERENCES fabric_entry (fabric_id))")
    cursor.execute("CREATE TABLE print_queue(fabric_id INTEGER,pic BLOB,work_status TEXT NOT NULL,PRIMARY KEY (fabric_id),FOREIGN KEY(fabric_id) REFERENCES fabric_entry(fabric_id),FOREIGN KEY (pic) REFERENCES design (pic),constraint chk_work check(work_status in('Y','N')))")
    cursor.execute("CREATE TABLE finish_phase(fabric_id INTEGER,work TEXT,client_name TEXT)")


def readpic(filename):
    with open(filename,'rb') as file:
        blob = file.read()
    return blob

def design_write(f_id,client_name,role):
    try:
        conn = sqlite3.connect('True_colors.db')
        cursor = conn.cursor()
        data_sets = (f_id,client_name,role)
        sqlquery = """ INSERT INTO fabric_entry (id,client_name,role) VALUES (?,?,?) """
        cursor.execute(sqlquery,data_sets)
        print("[SERVER] Database Connected")
    except sqlite3.Error as error:
        print("[SERVER] Database Error ",error)
    finally:
        if conn:
            conn.close()
            print("[SERVER] Database Connection Closed")

data_out_FE = "select * from fabric_entry;"
data_out_D = "select * from design;"
data_in_FE = "insert into fabric_entry values("

def base_read():
    os.chdir(dir)
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    for row in cursor.execute(data_out_FE):
        print(row)

    conn.close()

def base_write(selc,data):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    data_in_FE = "insert into fabric_entry values("
    data_in_D = "insert into design values("
    data_in_FP = "insert into finish_phase values("
    data_in_PQ = "insert into print_queue values("
    end_write = ");"
    if selc == 1:
        cursor.execute(data_in_FE+data+end_write)
    elif selc == 2:
        cursor.execute(data_in_D+data+end_write)
    elif selc == 3:
        cursor.execute(data_in_FP+data+end_write)
    elif selc == 4:
        cursor.execute(data_in_PQ+data+end_write)

    conn.commit()
    conn.close()

base_read()
# SO FOR DATABASE INPUT ALWAYS USE COMMIT TO SAVE THE VALUES TO THE DATABASE