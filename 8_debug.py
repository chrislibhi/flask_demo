import logging
from flask import Flask
app = Flask(__name__)


file_handler = logging.FileHandler('app.log')
app.logger.addHandler(file_handler)
app.logger.setLevel(logging.INFO)


@app.route('/hello', methods=['GET'])
def api_hello():
    app.logger.info('informing')
    app.logger.warning('warning')
    app.logger.error('screaming bloody murder!')
    return "check your logs\n"


if __name__ == '__main__':
    app.run(debug=True)
