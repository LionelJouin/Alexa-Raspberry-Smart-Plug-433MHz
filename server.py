from flask import Flask, request

onCode = [
    1,
    2
]
offCode = [
    3,
    4
]

@app.route('/on')
def on():
    arg = request.args.get('n')
    if arg is None:
        return jsonify("missing args"), 400
    print("turn on: " + arg)
    call(["codesend", onCode[arg]])
    return jsonify(" "), 200

@app.route('/off')
def off():
    arg = request.args.get('n')
    if arg is None:
        return jsonify("missing args"), 400
    print("turn off: " + arg)
    call(["codesend", offCode[arg]])
    return jsonify(" "), 200

def main(argv):
    app.run(host='0.0.0.0', debug=True)
    
if __name__ == '__main__':
    main(sys.argv)
