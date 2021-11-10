from flask import Flask, render_template
app = Flask(__name__)

@app.route('/results2')
def results():
    dict = {'phy':50,'che':60,'maths':70}
    return render_template('results2.html', result=dict)
