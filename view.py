from flask import Flask, render_template
from prometheus_client import Counter, generate_latest
from pymongo import MongoClient
import os

app = Flask(__name__)
view_metric = Counter('view', 'Book view', ['book'])

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/view/<id>')
def view_books(id):
    view_metric.labels(book=id).inc()
    return "View book %s" % id

@app.route('/buy/<id>')
def buy_books(id):
    return "Buy book %s" % id

@app.route('/metrics')
def metrics():
    return generate_latest()

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    client = MongoClient(os.environ['MONGO_HOST']);
    print("Connection to database Successful")
    client.close();
    app.run(debug=True, host='0.0.0.0', port=port)
