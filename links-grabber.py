import sqlite3
import time
import re

def follow(thefile):
    thefile.seek(0,2)
    while True:
        line = thefile.readline()
        if not line:
            time.sleep(0.1)
            continue
        yield line

def save_url(db_conn, quote):
    links = re.findall(r'http\S+',quote)
    for link in links:
        timestamp = quote.split("\t")[0]
        speaker = quote.split()[2]
        c = db_conn.cursor()
        c.execute("INSERT INTO links (speaker, timestamp, link, full) VALUES (?,?,?,?)", 
            (speaker, timestamp, link, quote))

    db_conn.commit()

if __name__ == '__main__':
    conn = sqlite3.connect('/home/giggles/links-engine/src/links.db')
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS links (speaker text, timestamp text, link text, full text)")
    logfile = open("/home/giggles/.weechat/logs/irc.#!.#!.weechatlog","r")
    loglines = follow(logfile)
    for line in loglines:
        save_url(conn, line)
