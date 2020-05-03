import re
#

def parse_connection_string(connection_string):
    d = {"dialect":"", "driver":"","username":"","password":"","host":"","port":"","database":""}
    if connection_string.startswith('sqlite3'):
        d['dialect']="sqlite3"
        d['database']=connection_string.split('///')[1]
    elif connection_string.startswith('postgresql'):
        d['dialect'] = "postgresql"
        d['username']=connection_string.split('://')[1].split(':')[0]
        d['password']=connection_string.split('@')[0].split('://')[1].split(':')[1]
        d['database']=connection_string.split('@')[1].split('/')[1]
        if connection_string.startswith('postgresql+'):
            d['driver'] = connection_string.replace('postgresql+', '').split('://')[0]
        if ":" in connection_string.split("@", 1)[1].split("/", 1)[0]:
            d["host"] = connection_string.split("@", 1)[1].split("/", 1)[0].split(":", 1)[0]
        else:
            d["host"] = connection_string.split("@", 1)[1].split("/", 1)[0]
        if ":" in connection_string.split("@", 1)[1].split("/", 1)[0]:
            d["port"] = connection_string.split("@", 1)[1].split("/", 1)[0].split(":", 1)[1]
    elif connection_string.startswith('m2sql'):
        d['dialect'] = "m2sql"
        d['username'] = connection_string.split('://')[1].split(':')[0]
        d['password'] = connection_string.split('://')[1].split(':')[1].split('/')[0]
        d['database'] = connection_string.split('://')[1].split('/')[1]
    return d

parse_connection_string('sqlite3:///b4_7.sqlite3')
parse_connection_string("postgresql+psycopg2://admin:1234@localhost/b4_7")
parse_connection_string("postgresql://admin:1234@localhost/b4_7")
parse_connection_string("m2sql://admin:1234/b4_7")

