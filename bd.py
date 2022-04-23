import sqlite3

con = sqlite3.connect('frog_db.db', check_same_thread=False)
cur = con.cursor()


def id_of_frog(profile):
    ids = list(cur.execute(f'''SELECT user_frog_id 
    FROM accounts
    WHERE telegram_user = {profile}
    ''').fetchone())[0]
    return ids


def add_new_profile(profile):
    ids = id_of_frog(profile)
    if ids:
        return False
    cur.execute(f'''INSERT INTO frogs (frog_satiety, frog_condition, bugs, frog_class, 
    frog_mood, frog_wins, frog_defeats)
    VALUES (100, "живая", 10, "начальный", "хорошее", 0, 0)''')
    con.commit()
    ids = list(cur.execute('''SELECT last_insert_rowid() FROM frogs''').fetchone())[0]
    cur.execute(f'''INSERT INTO accounts (telegram_user, user_frog_id)
    VALUES ({profile}, {ids})''')
    con.commit()
    return True


def result_of_game():
    pass


def take_frog(profile):
    ids = id_of_frog(profile)
    return cur.execute(f'''SELECT frog_satiety, frog_condition, bugs, frog_class, 
    frog_mood, frog_wins, frog_defeats FROM frogs WHERE id = {ids}''').fetchone()



def add_bugs(profile, bugs_count):
    ids = id_of_frog(profile)
    cur.execute(f'''UPDATE frogs
        SET bugs = (bugs + {bugs_count})
        WHERE id = {ids}''')
    con.commit()
