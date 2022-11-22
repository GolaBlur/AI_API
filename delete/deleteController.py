from flask import Flask

app = Flask(__name__)


@app.route('/do')
def do_delete(file_and_object_list):
    
    return



if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8881)