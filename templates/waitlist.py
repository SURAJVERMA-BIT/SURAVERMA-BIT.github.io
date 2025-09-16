from flask import Flask, request, jsonify
import sqlite3, re
from cryptography.fernet import Fernet

app = Flask(__name__)

# Secret key (store in .env later)
key = Fernet.generate_key()
cipher = Fernet(key)

# Initialize DB
def init_db():
    conn = sqlite3.connect("waitlist.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS waitlist (id INTEGER PRIMARY KEY, email BLOB UNIQUE)")
    conn.commit()
    conn.close()

@app.route("/subscribe", methods=["POST"])
def subscribe():
    email = request.form.get("email")
    if not email or not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return jsonify({"error": "Invalid email"}), 400
    
    encrypted_email = cipher.encrypt(email.encode())
    try:
        conn = sqlite3.connect("waitlist.db")
        cur = conn.cursor()
        cur.execute("INSERT INTO waitlist (email) VALUES (?)", (encrypted_email,))
        conn.commit()
        conn.close()
        return jsonify({"message": "You are added to the waitlist!"}), 200
    except sqlite3.IntegrityError:
        return jsonify({"error": "Email already exists"}), 409

if __name__ == "__main__":
    init_db()
    app.run(debug=True)
