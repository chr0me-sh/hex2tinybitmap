from flask import Flask, request, render_template, Response, jsonify
import hex2bmp
import base64

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/gen')
def gen_img():
    img_hex = request.args.get('h', 0, type=str)
    img_fg = request.args.get('fg', 0, type=str)
    img_bg = request.args.get('bg', 0, type=str)
    tmp = hex2bmp.generate(img_hex, img_fg, img_bg)
    tmp_b64 = base64.b64encode(tmp)
    return jsonify(result=str(tmp_b64, 'utf-8'))
