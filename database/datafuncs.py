from flask import g

MAX_MSG = 50

table_name = "log"    

def query_db(query, args=(), one=False):
    cursor = g.db_conn.cursor()
    cursor.execute(query, args)
    rv = cursor.fetchall()
    cursor.close()
    return (rv[0] if rv else None) if one else rv


def insert_db(query, args=()):
    cursor = g.db_conn.cursor()
    cursor.execute(query, args)
    g.db_conn.commit()
    cursor.close()

def get_user_conversation_session_data(app, user, session):
    query_results = query_db(f"SELECT * FROM {table_name} WHERE app = %s AND enduser = %s AND sess = %s AND speaker IN ('user', 'assistant') ORDER BY ts ASC;", (app, user, session))
    return query_results[-MAX_MSG:]

def get_user_conversation_history(app, user):
    query_results = query_db(f"SELECT * FROM {table_name} WHERE app = %s AND enduser = %s AND speaker IN ('user', 'assistant') ORDER BY ts ASC;", (app, user))
    return query_results[-25:]

def insert_user_data(app, utilisateur, sess, msg, speaker):
    insert_db(f"INSERT INTO {table_name} (app,enduser,sess,msg,speaker) VALUES(%s,%s,%s,%s,%s);", (app, utilisateur, sess, msg, speaker))

def select_log_table():
    return query_db(f"SELECT app, enduser, msg, sess, speaker, ts FROM {table_name};")

def get_last_summary_context(user,app):
    return query_db(f"SELECT distinct msg, ts FROM {table_name} WHERE enduser = %s AND speaker = 'summary' AND app = %s  ORDER BY ts DESC LIMIT 1;", (user,app))