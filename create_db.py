import psycopg2
import db_settings

dbname = db_settings.DBNAME
dbhost = db_settings.DBHOST
dbuser = db_settings.DBUSER
dbpass = db_settings.DBPASS
conn = psycopg2.connect("dbname='" + dbname +
                        "' user='" + dbuser +
                        "' host='" + dbhost +
                        "' password='" + dbpass + "'")
cur = conn.cursor()
cur.execute("""
CREATE TABLE news(
    id SERIAL PRIMARY KEY,
    global_id INTEGER,
    title VARCHAR(500),
    subtitle VARCHAR(500),
    date_time TIMESTAMP WITHOUT TIME ZONE,
    text TEXT,
    authors VARCHAR(300),
    tags TEXT,
    subject VARCHAR(100),
    portal VARCHAR(100),
    link VARCHAR(500)
)
""")
conn.commit()
conn.close()
