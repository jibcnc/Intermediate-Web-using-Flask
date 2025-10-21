# main.py
from flask import Flask, render_template, request
import mylib

app = Flask(__name__)

@app.route('/')
def tourist_site():
    return render_template('tourist-site.html')

@app.route('/tech')
def tech():
    return render_template('tech.html')

@app.route('/myid')
def myid():
    return """
    <html lang="th">
    <head>
        <meta charset="UTF-8">
        <title>รหัสนักศึกษา</title>
        <style>
            body {
                font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif;
                background-color: #f0f8ff;
                color: #333;
                text-align: center;
                margin: 0;
                padding: 0;
            }
            h1 {
                background-color: #4cafef;
                color: white;
                padding: 20px 0;
                margin: 0 0 30px 0;
            }
            .id-box {
                background-color: #ffffff;
                display: inline-block;
                padding: 30px 50px;
                border-radius: 12px;
                box-shadow: 0 0 10px rgba(0,0,0,0.15);
            }
            .menu { margin-top: 40px; }
            .menu a {
                text-decoration: none;
                background-color: #4cafef;
                color: white;
                padding: 10px 20px;
                border-radius: 8px;
                margin: 0 5px;
                transition: 0.3s;
            }
            .menu a:hover { background-color: #007acc; }
        </style>
    </head>
    <body>
        <h1>รหัสนักศึกษา</h1>
        <div class="id-box">
            <h2>68130037</h2>
        </div>
        <div class="menu">
            <a href="/">หน้าแนะนำสถานที่ท่องเที่ยว</a>
            <a href="/tech">หน้าเทคโนโลยีที่สนใจ</a>
            <a href="/draw">หน้างาน Git ครั้งที่แล้ว</a>
        </div>
    </body>
    </html>
    """

@app.route('/draw')
def draw():
    return render_template('draw.html')

@app.route('/run', methods=['POST'])
def run():
    x = request.form['character']
    y = int(request.form['turn'])
    results = [mylib.myfunc(x, i) for i in range(1, y + 1)]
    return render_template('result.html', x=x, y=y, results=results)



#Assignment 19/10/25
@app.route('/sum/<xx>/<yy>') 
def sum_number(xx,yy):
    try:                           
        number_xx = int(xx)
        number_yy = int(yy)
        result_number = number_xx + number_yy
        return "The result of sum between " + str(number_xx) + " and " + str(number_yy) + " is " + str(result_number)
    except(ValueError,TypeError):     
        return "You are using miss data type for operation"

@app.route('/concat/<xx>/<yy>')
def concat(xx, yy):
    result_concat = xx + yy
    return "The result of concatenate between " + str(xx) + " and " + str(yy) + " is " + str(result_concat)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=80)