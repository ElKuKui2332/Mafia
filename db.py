import sqlite3

def insert_player(player_id, username):
    con = sqlite3.connect("db.db")
    cur = con.cursor()
    sql = f"INSERT INTO players (player_id, username) VALUES('{player_id}', '{username}')"
    cur.execute(sql)
    con.commit()
    con.close()

#insert_player(112121, 'nick')

def player_amount():
    con = sqlite3.connect("db.db")
    cur = con.cursor()
    sql = f"SELECT * FROM players"
    cur.execute(sql)
    res = cur.fetchall()
    con.close()
    return len(res)

#print(player_amount())
 
def get_mafia_usernames():
    con = sqlite3.connect('db.db')
    cur = con.cursor()
    sql = f"SELECT username FROM players WHERE role = 'mafia' "
    cur.execute(sql)
    data = cur.fetchall()
   
    names = ''
    for row in data:
        name = row[0]
        names += name + '\n'
    con.close()
    return names

def get_players_role():
    con = sqlite3.connect('db.db')
    cur = con.cursor()
    sql = f"SELECT player_id, role FROM players"
    cur.execute(sql)
    data = cur.fetchall()
    con.close()
    return data

def get_all_alive():
    con = sqlite3.connect('db.db')
    cur = con.cursor()
    sql = f"SELECT username FROM players WHERE dead = 0"
    cur.execute(sql)
    data = cur.fetchall()
    data = [row[0] for row in data]
    con.close()
    return data 

def set_role(players):
    game_roles = ['citizen'] * players 
    mafias = int (players * 0.3)
    for i in range(mafias):
        game_roles[i] = 'mafia'
    random.shuffle(game_roles)

    con = sqlite3.connect('db.db')
    cur = con.cursor()

    sql =  f'SELECT player_id FROM players'
    cur.execute(sql)
    players_ids =  cur.fetchall()
    for role, row in zip(game_roles, players_id):
        sql = f"UPDATE players SET role = {role} WHERE player_id = {row[0]}"

def vote(type, user_name, player_id):
    con=sqlite3.connect('db1.db')
    cur = con.cursor()
    sql = f"SELECT username FROM players WHERE player_id = {player_id} AND dead = 0 AND voted = 0"
    cur.execute(sql)
    user = cur.fetchone()
    if user: 
        sql = f"UPDATE players SET {type} = {type}+1 WHERE username = '{user_name}'"
        cur.execute(sql)
        sql = f"UPDATE players SET voted = 1 WHERE player_id = '{player_id}'"
        cur.execute(sql)
        con.commit()
        con.close()
        return True
    else:
        con.close()
        return False
    
#print(vote(player_id = 643323,user_name ='El KuKui',type = 'mafia_vote'))
def mafia_kill():
    con=sqlite3.connect('db1.db')
    cur = con.cursor()
    sql = f"SELECT MAX(mafia_vote) FROM players"
    cur.execute(sql)
    mafia_vote = cur.fetchone()[0]
    print(mafia_vote)
    sql = f"SELECT COUNT (*) FROM players WHERE dead = 0 AND role = 'mafia'" 
    cur.execute(sql)
    mafia_alive = cur.fetchone()[0]
    killed_name = 'ничего'
    if mafia_alive == mafia_vote:
        sql = f"SELECT username FROM players WHERE mafia_vote = {mafia_vote} "
        cur.execute(sql)
        killed_name = cur.fetchone()[0]
        sql = f"UPDATE players SET dead = 1 WHERE username = '{killed_name}'"
        cur.execute(sql)
        con.commit()
    con.close()
    return killed_name

def citizen_kill():
    con=sqlite3.connect('db1.db')
    cur = con.cursor()
    sql = f"SELECT MAX(citizen_vote) FROM players"
    cur.execute(sql)
    citizen_vote = cur.fetchone()[0]
    print(citizen_vote)
    sql = f"SELECT COUNT (*) FROM players WHERE dead = 0 AND role = 'citizen'" 
    cur.execute(sql)
    citizen_alive = cur.fetchone()[0]
    kicked_name = 'ничего'
    if citizen_alive == citizen_vote:
        sql = f"SELECT username FROM players WHERE citizen_vote = {citizen_vote} "
        cur.execute(sql)
        kicked_name = cur.fetchone()[0]
        sql = f"UPDATE players SET dead = 1 WHERE username = '{kicked_name}'"
        cur.execute(sql)
        con.commit()
    con.close()
    return kicked_name

print(citizen_kill())
    

