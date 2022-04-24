import random
import sqlite3

con = sqlite3.connect('frog_db.db', check_same_thread=False)
cur = con.cursor()

frogs_win = 0
frogs_defeat = 0


def id_of_frog(profile):
    ids = list(cur.execute(f'''SELECT user_frog_id 
    FROM accounts
    WHERE telegram_user = "{profile}"
    ''').fetchone())[0]
    return ids


def add_new_profile(profile):
    ids = cur.execute(f'''SELECT id FROM accounts WHERE telegram_user = {profile}''').fetchone()
    if ids:
        return False
    cur.execute(f'''INSERT INTO frogs (heals, frog_satiety, frog_condition, bugs, frog_class, 
    frog_mood, attack_power, frog_wins, frog_defeats)
    VALUES (500, 100, "Живая", 10, "Новичок", "Хорошее", 500, 0, 0)''')
    con.commit()
    ids = list(cur.execute('''SELECT last_insert_rowid() FROM frogs''').fetchone())[0]
    cur.execute(f'''INSERT INTO accounts (telegram_user, user_frog_id)
    VALUES ({profile}, {ids})''')
    con.commit()
    return True


def result_of_game(profile, win=0, defeat=0):
    ids = id_of_frog(profile)
    cur.execute(f'''UPDATE frogs
        SET frog_wins = (frog_wins + {win})
        WHERE id = {ids}''')
    cur.execute(f'''UPDATE frogs
            SET frog_defeats = (frog_defeats + {defeat})
            WHERE id = {ids}''')
    con.commit()


def take_frog(profile):
    ids = id_of_frog(profile)
    return cur.execute(f'''SELECT heals, frog_satiety, frog_condition, bugs, frog_class, 
    frog_mood, attack_power, frog_wins, frog_defeats FROM frogs WHERE id = {ids}''').fetchone()


def add_bugs(profile, bugs_count):
    ids = id_of_frog(profile)
    invent_bugs = cur.execute(f'''SELECT bugs FROM frogs WHERE id = {ids}''').fetchone()[0] + bugs_count
    if invent_bugs < 0:
        invent_bugs = 0
    cur.execute(f'''UPDATE frogs
        SET bugs = ({invent_bugs})
        WHERE id = {ids}''')
    con.commit()


def take_away_bugs(profile, bugs_count):
    ids = id_of_frog(profile)
    invent_bugs = cur.execute(f'''SELECT bugs FROM frogs WHERE id = {ids}''').fetchone()[0] - bugs_count
    if invent_bugs < 0:
        invent_bugs = 0
    cur.execute(f'''UPDATE frogs SET bugs = ({invent_bugs})
    WHERE id = {ids}''')
    con.commit()


def show_bugs(profile):
    ids = id_of_frog(profile)
    return cur.execute(f'''SELECT bugs FROM frogs
        WHERE id = {ids}''').fetchone()[0]


def feed_frog(profile, price):
    ids = id_of_frog(profile)
    return cur.execute(f'''SELECT bugs FROM frogs
            WHERE id = {ids}''').fetchone()[0] >= price


def upclass(profile, price, frog_class):
    classes = {"Новичок": [0, 500, 500], "Боец": [1000, 1000, 1000], "Маг": [5000, 2000, 2000],
               "Эльф": [15000, 5000, 4500]}
    ids = id_of_frog(profile)
    count_bugs = cur.execute(f'''SELECT bugs FROM frogs
            WHERE id = {ids}''').fetchone()[0]
    if count_bugs >= price:
        take_away_bugs(profile, price)
        cur.execute(f'''UPDATE frogs 
            SET attack_power = {classes[frog_class][1]}
            WHERE id = {ids}''')
        cur.execute(f'''UPDATE frogs SET frog_class = "{frog_class}" 
        WHERE id = {ids}''')
        cur.execute(f'''UPDATE frogs SET heals = "{classes[frog_class][2]}" 
        WHERE id = {ids}''')
        con.commit()
    else:
        return False


def satiety(profile, count_satiety):
    ids = id_of_frog(profile)
    cur.execute(f'''UPDATE frogs 
    SET frog_satiety = (frog_satiety + {count_satiety})
    WHERE id = {ids}''')
    con.commit()


def condition(profile):
    ids = id_of_frog(profile)
    cur.execute(f'''UPDATE frogs 
    SET frog_condition = ("живая")
    WHERE id = {ids}''')
    con.commit()


def mood(profile, ind):
    indx = 3
    moods = ["Не покормишь - я тебя съем", "Ужасное", "Ей пуфик", "Хорошее", "Отличное"]
    indx += ind
    if indx > 4:
        indx = 4
    md_in = moods[indx]
    ids = id_of_frog(profile)
    cur.execute(f'''UPDATE frogs 
       SET frog_mood = '{md_in}'
       WHERE id = {ids}''')
    con.commit()


def fight(profile):
    ids = id_of_frog(profile)
    enemy = list(cur.execute(f'''SELECT telegram_user FROM accounts WHERE telegram_user != "{profile}"'''))
    enemy = random.choice(enemy[0])  # list index out of range

    my_attack = cur.execute(f'''SELECT attack_power FROM frogs WHERE id = {ids}''').fetchone()[0]
    my_heal = cur.execute(f'''SELECT heals FROM frogs WHERE id = {ids}''').fetchone()[0]
    enemy_attack = cur.execute(f'''SELECT attack_power FROM frogs WHERE id = {id_of_frog(enemy)}''').fetchone()[0]
    enemy_heal = cur.execute(f'''SELECT heals FROM frogs WHERE id = {id_of_frog(enemy)}''').fetchone()[0]

    while my_heal > 0 and enemy_heal > 0:
        my_heal -= enemy_attack
        enemy_heal -= my_attack
    if my_heal > 0 and enemy_heal <= 0:
        add_bugs(profile, 500)
        take_away_bugs(enemy, 250)
        return 'Ты победил!'
    elif my_heal == enemy_heal:
        add_bugs(profile, 100)
        add_bugs(enemy, 100)
        return 'Ничья'
    else:
        add_bugs(enemy, 500)
        take_away_bugs(profile, 250)
        return 'Ты проиграл!'


def enemy(enemy):
    heal = cur.execute(f'''SELECT heals FROM frogs WHERE id = {id_of_frog(enemy)}''').fetchone()[0]
    attack = cur.execute(f'''SELECT attack_power FROM frogs WHERE id = {id_of_frog(enemy)}''').fetchone()[0]
    class_enemy = cur.execute(f'''SELECT frog_class FROM frogs WHERE id = {id_of_frog(enemy)}''').fetchone()[0]
    return heal, attack, class_enemy
