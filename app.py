from flask import Flask, request, render_template
import psycopg2

app = Flask(__name__)

# PostgreSQL connection details
DB_HOST = "localhost"
DB_NAME = "verification"
DB_USER = "nandakumarpn"
DB_PASS = "NandA12!@#"

@app.route('/')
def index():
    return render_template('index.html')  # your HTML form page

@app.route('/submit', methods=['POST'])
def submit():
    tran_id = request.form['transaction_id']
    password = request.form['unique_code']

    # connect to PostgreSQL
    conn = psycopg2.connect(
        host=DB_HOST,
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASS
    )
    cur = conn.cursor()

    # insert operation
    cur.execute("INSERT INTO verification (tran_id, password) VALUES (%s, %s)", (tran_id, password))
    conn.commit()

    cur.close()
    conn.close()

    return "✅ Data stored successfully in PostgreSQL!"

if __name__ == '__main__':
    app.run(debug=True)
