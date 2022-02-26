from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb://test:test@localhost', 27017)
# client = MongoClient('localhost', 27017)
db = client.dbsparta

## HTML을 주는 부분
@app.route('/')
def home():
   return render_template('index.html')

@app.route('/shopping', methods=['GET'])
def listing():
    orders = list(db.orders.find({}, {'_id': False}))
    return jsonify({'all_orders': orders})

## API 역할을 하는 부분
@app.route('/shopping', methods=['POST'])
def saving():
    name_receive = request.form['name_give']
    amount_receive = request.form['amount_give']
    address_receive = request.form['address_give']
    phonenum_receive = request.form['phonenum_give']


    doc = {
        'name': name_receive,
        'amount': amount_receive,
        'address': address_receive,
        'phonenum': phonenum_receive,
    }
    db.orders.insert_one(doc)

    return jsonify({'msg':'주문이 완료되었습니다 !!'})

if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)