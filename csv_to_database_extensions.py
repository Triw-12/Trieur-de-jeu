# Import sqlite3 package and initialise the database cursor
import sqlite3
db_con = sqlite3.connect("website/db.sqlite3")
db_cur = db_con.cursor()

first=True # Boolean variable used to check if we're on the first line of the CSV

# Get all extension names
db_res = db_cur.execute("SELECT DISTINCT extension_name FROM board_games_extensions")
# Now make a proper array following the last request.
extension_name_list = []
for i in db_res.fetchall():
    extension_name_list.append(i[0])

# Open Jeu_csv-Extentions.csv in read-only mode.
with open("Jeu_csv-Extentions.csv", "r") as file:
    for line in file: # For each line
        if not first: # Allows to forget the first line (titles) of the csv
            words = line.split(";")
            extension_name = words[0]
            game_name = words[1]
            time_add = words[2]
            # Change game_name in order to escape the ' symbol in SQL.
            game_name_normalised = game_name.replace("'", "''")

            game_id = db_cur.execute("SELECT game_id from board_games_games where game_name='{}'".format(game_name_normalised)).fetchall()[0][0]

            if extension_name not in extension_name_list: # If the game is not yet in the database
                # Then add it to the database
                db_cur.execute("""INSERT INTO board_games_extensions VALUES (NULL,?, ?, ?)""",(time_add, game_id, extension_name))
                db_con.commit()
        else: # # Allows to forget the first line (titles) of the csv
            first=False