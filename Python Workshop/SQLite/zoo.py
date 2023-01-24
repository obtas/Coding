import sqlite3 as sqlite

conn = sqlite.connect("test-db")
cursor = conn.cursor()

sql_file = open("cats.sql")
sql_string = sql_file.read()
#cursor.executescript(sql_string)

#print(cursor.execute("SELECT * FROM cats").fetchall())

def runQuery(query):
    data = cursor.execute(query).fetchall()
    return data

def addCat(name_type, weight_kg, patterned):
    insert_str = f"INSERT INTO cats (name_type, weight_kg, patterned) VALUES ('{name_type', '{weight_kg}', '{patterned}');"
    runQuery(insert_str)
    return True

def updateCat(id, value):
    update_query = f"UPDATE cats SET weight_kg = '{value}' WHERE cat_id = {id}"
    runQuery(update_query)
    return True

def deleteCat(id):
    delete_query= f"DELETE FROM cats WHERE cat_id = {id}"
    runQuery(delete_query)
    return True

def userCat():
    cat_name = input("Enter the name of the cat: ")
    cat_weight = input("Enter weight of cat: ")
    cat_pattern = input("Is the cat patterned: ")
    update_usercat = f"INSERT INTO cats (name_type, weight_kg, patterned) VALUES ('{cat_name}', '{cat_weight}' , '{cat_pattern}');"
    runQuery(update_usercat)
    return True

def viewCat(id):
    view_cat = f"SELECT * FROM cats WHERE cat_id = {id}"
    return runQuery(view_cat)

def viewAllRecords():
    view_all = "SELECT * FROM cats;"
    return runQuery(view_all)
    
    


print(viewCat(3))
#cat_data = runQuery("SELECT * FROM cats")
#print(cat_data)

# Saving the data into the db created via cursor stuff
conn.commit

