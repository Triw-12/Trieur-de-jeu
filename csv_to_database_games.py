
import sqlite3
db_con = sqlite3.connect("website/db.sqlite3")
db_cur = db_con.cursor()

first=True

db_res = db_cur.execute("SELECT game_name FROM board_games_games")
game_list = []
for i in db_res.fetchall():
    game_list.append(i[0])

with open("Jeu_csv-Jeux.csv", "r") as file:
    for line in file:
        if not first:
            L = line.split(";")
            game_name = L[0]
            difficulty = L[1]
            min_age = L[2]
            game_length_min = L[3]
            game_length_max = L[4]
            min_players = L[5]
            max_players = L[6]
            types = L[7]
            caution = L[8]
            stock_nb = L[9]
            print(types)
            print(game_name)

            if game_name not in game_list: # If the game is not yet in the database
                # Then add it to the database
                db_cur.execute("""INSERT INTO board_games_games VALUES (NULL,?, ?, ?, ?, ?, ?, ?)""",
                               (stock_nb, game_length_min, game_length_max, min_players, max_players, min_age, game_name))
                db_con.commit()
                #print(db_con.commit())
                # Then add its tag.s to the 2nd table
                # For that I need the game_id, for that I'll ask the bdd :
                game_id = db_cur.execute("SELECT game_id from board_games_games where game_name='{}'".format(game_name.replace("'", "''"))).fetchall()[0][0]
                tags = types.split("/")
                for tag in tags:
                    db_cur.execute("""INSERT INTO board_games_tags VALUES (NULL, ?, ?)""",(tag, game_id))
                    db_con.commit()
        else:
            first=False