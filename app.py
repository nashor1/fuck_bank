from Tools.scripts.make_ctype import method
from flask import Flask, request

app = Flask(__name__)


@app.route('/', methods=['GET'])
def seacher_ID():
    import seach_ID
    idcard = request.args.get('idcard')
    finalStr = seach_ID.main(idcard)
    return finalStr


if __name__ == '__main__':
    app.run()
