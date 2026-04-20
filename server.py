import sqlite3, os, http.server, socketserver

# STEP 1: Connect to database
conn = sqlite3.connect("bank.db")
cursor = conn.cursor()

# STEP 2: Get totals from DB
cursor.execute("SELECT SUM(amount) FROM transactions WHERE amount > 0")
received = str(cursor.fetchone()[0] or 0)

cursor.execute("SELECT SUM(amount) FROM transactions WHERE amount < 0")
withdrawn = str(abs(cursor.fetchone()[0] or 0))

cursor.execute("SELECT SUM(amount) FROM transactions")
balance = str(cursor.fetchone()[0] or 0)

# STEP 3: Build table rows
table_rows = ""
cursor.execute("SELECT time, detail, amount, status FROM transactions ORDER BY time DESC LIMIT 10")
rows = cursor.fetchall()

for r in rows:
    table_rows += f"<tr><td>{r[0]}</td><td>{r[1]}</td><td>{r[2]}</td><td style='text-align:right'><span class='status-badge'>{r[3]}</span></td></tr>"

# STEP 4-6: Read index, Replace, and Save to output.html
with open("index.html", "r") as f:
    html = f.read()

html = html.replace("{balance}", balance).replace("{received}", received).replace("{withdrawn}", withdrawn).replace("{table_rows}", table_rows if table_rows else "<tr><td colspan='4'>No Data Found</td></tr>")

with open("output.html", "w") as f:
    f.write(html)
conn.close()

# STEP 7: Start Server (Keep this running)
print("ALIVE: Open http://localhost:8000/output.html in your browser")
socketserver.TCPServer(("", 8000), http.server.SimpleHTTPRequestHandler).serve_forever()