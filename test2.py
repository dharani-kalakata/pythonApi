from flask import Flask, jsonify
import random
import datetime

app = Flask(__name__)

def generate_random_data():
    change_number = random.randint(1000, 9999)
    start_date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    end_date = (datetime.datetime.now() + datetime.timedelta(days=random.randint(1, 30))).strftime('%Y-%m-%d %H:%M:%S')
    coordinator_name = "Eswar"
    
    data = {
        "change_number": change_number,
        "start_date": start_date,
        "end_date": end_date,
        "coordinator_name": coordinator_name
    }
    return data

@app.route('/api/random_change', methods=['GET'])
def get_random_change():
    random_data = generate_random_data()
    return jsonify(random_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
