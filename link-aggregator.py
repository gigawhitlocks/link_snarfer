from bottle import route, run, error, Bottle
import sqlite3
app = Bottle()
db_cursor = None

@app.get('/')
def show_snarfed_links():
    db_cursor.execute('SELECT * FROM links ORDER BY timestamp DESC;')
    links = db_cursor.fetchall()
    return "".join(["{}: <a href='{}'>{}</a><br />{}<hr />".format(x[0], x[2], x[2], x[3]) for x in links])

if __name__ == "__main__":
    conn = sqlite3.connect('/home/giggles/links-engine/src/links.db')
    global db_cursor
    db_cursor = conn.cursor()
    app.run(host="0.0.0.0", port="9982", reload=True)
