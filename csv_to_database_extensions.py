
import sqlite3
db_con = sqlite3.connect("website/db.sqlite3")
db_cur = db_con.cursor()

first=True

db_res = db_cur.execute("SELECT DISTINCT extension_name FROM board_games_extensions")
extension_name_list = []
for i in db_res.fetchall():
    extension_name_list.append(i[0])

with open("Jeu_csv-Extentions.csv", "r") as file:
    for line in file:
        if not first:
            L = line.split(";")
            extension_name = L[0]
            game_name = L[1]
            time_add = L[2]
            game_name_normalised = game_name
            game_name_normalised = game_name_normalised.replace("'", "''")

            game_id = db_cur.execute("SELECT game_id from board_games_games where game_name='{}'".format(game_name_normalised)).fetchall()[0][0]

            if extension_name not in extension_name_list: # If the game is not yet in the database
                # Then add it to the database
                db_cur.execute("""INSERT INTO board_games_extensions VALUES (NULL,?, ?, ?)""",(time_add, game_id, extension_name))
                db_con.commit()
        else:
            first=False