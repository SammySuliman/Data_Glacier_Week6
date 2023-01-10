# virtual env: conda activate c:\Users\filto\Desktop\data_glacier\.conda
from flask import Flask
import pickle
app = Flask(__name__)
@app.route('/hello') #http://www.google.com/
def home():
    return 'Hello World'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
