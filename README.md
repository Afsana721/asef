🛠️ Simple Bank: How the Backend Works

This project uses Raw Python to create a bridge between a Database (SQL) and a User Interface (HTML). Since we aren't using a framework (like Flask or Django), we are building the "plumbing" ourselves.

1. The Core Imports (The Tools)

sqlite3: Our "Librarian." It talks to the bank.db file to save and retrieve data.

os: Our "Handyman." It helps Python understand the file paths on your computer.

http.server & socketserver: Our "Broadcaster." They create the local web server so your browser can "see" the files.

2. The Logic Flow

A. Data Retrieval (The Brain)

Instead of just showing a static page, the script queries the database.

cursor.execute("SELECT SUM(amount) FROM transactions")
balance = str(cursor.fetchone()[0] or 0)


Python asks the SQL file for a math calculation (SUM), converts the result into a string, and stores it in a variable.

B. Dynamic HTML Building

Since HTML can't "talk" to a database, Python builds the table rows for it. It loops through the SQL results and wraps them in <tr> and <td> tags. This is called Dynamic Generation.

C. The "Template Injection" Strategy

This is the most important part. We use a template file (index.html) with "blank spots" like {balance}.

Read: Python opens the file as a giant string.

Replace: The .replace() command swaps the "blank spot" for the real data from the database.

Save: It writes a new file called output.html.

D. The Request/Response Handshake

The Server: socketserver stays "awake" on Port 8000.

The Request: When you type localhost:8000/output.html in Chrome, the browser sends a "Request" to Python.

The Response: Python's server finds the output.html file on your hard drive and sends the text back to the browser.

3. Why This Matters

By doing this without a framework, you are learning how Internet plumbing actually works. You are manually handling:

Persistence (Database)

State Management (Variables)

Templating (String replacement)

Networking (HTTP Hosting)

Tip for the Developer: Every time you change data in the SQL database, you must stop the server (Ctrl+C) and restart it so the script can re-run the "Replace" logic and update the numbers in output.html.