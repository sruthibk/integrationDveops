from flask import Flask, jsonify
import psycopg2

app = Flask(__name__)

# Connect to the PostgreSQL database
conn = psycopg2.connect(
    dbname="postgres",
    user="d72e0f9be7e2b11d55576a02",
    password="809bf67ccec54c3e35bce6e9",
host = "sruthi-roja-qa1.fyre.ibm.com",
    port="5432"
)

# Define a route to fetch data from the database
@app.route('/api/data')
def get_data():
    cur = conn.cursor()
    cur.execute("SELECT * FROM Entries")
    rows = cur.fetchall()
    cur.close()
    # Convert rows to a list of dictionaries
    data = [{'responsecode': row[0], 'responsemessage': row[1]} for row in rows]
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)