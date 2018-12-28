import sys
from subprocess import call
from flask import Flask, request, jsonify

app = Flask(__name__)

onCode = [
    1054003,
    1054147,
    1054467
]
offCode = [
    1054012,
    1054156,
    1054476
]

@app.route('/on')
def on():
    arg = request.args.get('n')
    if arg is None:
        return jsonify("Missing argument: n"), 400
    n = int(arg)
    call(["/root/rfoutlet/codesend", str(onCode[n])])
    return jsonify(" "), 200

@app.route('/off')
def off():
    arg = request.args.get('n')
    if arg is None:
        return jsonify("Missing argument: n"), 400
    n = int(arg)
    call(["/root/rfoutlet/codesend", str(offCode[n])])
    return jsonify(" "), 200

def main(argv):
    app.run(host='0.0.0.0', debug=True)

if __name__ == '__main__':
    main(sys.argv)
