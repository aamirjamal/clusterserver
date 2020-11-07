from flask import Flask, request
import os
import subprocess


app = Flask(__name__)
CUR_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = CUR_DIR + "/data"
pkPath = DATA_DIR + "/my_public_key.txt"
skPath = DATA_DIR + "/my_secret_key.txt"
c1Path = DATA_DIR + "/inp1.txt"
c2Path = DATA_DIR + "/inp2.txt"


@app.route('/')
def hello_world():
    return 'Cluster server running!'


@app.route('/compute', methods=["POST"])
def compute():
    operand = request.args['operand']
    scheme = request.args['scheme']
    library = request.args['library']
    ctxt1 = request.files['ctxt1']
    ctxt1.save(c1Path)
    ctxt2 = request.files['ctxt2']
    ctxt2.save(c2Path)
    pk = request.files['pk']
    pk.save(pkPath)
    sk = request.files['sk']
    sk.save(skPath)

    arg1 = 0
    if operand == "Multiply":
        arg1 = 1

    # enter your command here and pass arguments as string interpolation
    cmd = f"./test.sh {arg1}"
    subprocess.run(cmd, cwd=".", shell=True)

    # bash hello.bash

    return operand + scheme + library


@app.route('/test', methods=["GET"])
def test():
    return {"response": "woorking!"}
