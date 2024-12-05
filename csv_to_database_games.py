# Import sqlite3 package and initialise the database cursor
import sqlite3
db_con = sqlite3.connect("website/db.sqlite3")
db_cur = db_con.cursor()

first=True # Boolean variable used to check if we're on the first line of the CSV

# Get all game names
db_res = db_cur.execute("SELECT game_name FROM board_games_games")
# Now make a proper array following the last request.
game_list = []
for i in db_res.fetchall():
    game_list.append(i[0])

# Open Jeu_csv-Jeux.csv in read-only mode.
with open("Jeu_csv-Jeux.csv", "r") as file:
    for line in file: # For each line
        if not first: # Allows to forget the first line (titles) of the csv
            words = line.split(";")
            game_name = words[0]
            difficulty = words[1]
            min_age = words[2]
            game_length_min = words[3]
            game_length_max = words[4]
            min_players = words[5]
            max_players = words[6]
            types = words[7]
            caution = words[8]
            stock_nb = words[9]
            # Change game_name in order to escape the ' symbol in SQL.
            game_name_normalised = game_name.replace("'", "''")

            # If the game is not yet in the database
            if game_name not in game_list:
                # Then add it to the database
                db_cur.execute("""INSERT INTO board_games_games VALUES (NULL,?, ?, ?, ?, ?, ?, ?)""",
                               (stock_nb, game_length_min, game_length_max, min_players, max_players, min_age, game_name))
                db_con.commit()
                # To add its tag.s to the tags table I need the game_id, I'll get it with game_name in the games table :
                game_id = db_cur.execute("SELECT game_id from board_games_games where game_name='{}'".format(game_name_normalised)).fetchall()[0][0]
                # Split the tags column into the different tags
                tags = types.split("/")
                # For each tag
                for tag in tags:
                    # Add it to the corresponding table
                    db_cur.execute("""INSERT INTO board_games_tags VALUES (NULL, ?, ?)""",(tag, game_id))
                    db_con.commit()
        else: # Allows to forget the first line (titles) of the csv
            first=False