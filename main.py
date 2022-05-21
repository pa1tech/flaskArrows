from flask import Flask, flash,render_template, request, send_from_directory,session
import win32com.client as comclt

wsh= comclt.Dispatch("WScript.Shell")
wsh.AppActivate("Notepad")

app = Flask(__name__)
app.secret_key = 'the random string'

@app.route('/',methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if request.form.get('left') == 'True':
            wsh.SendKeys("{LEFT}")
        if request.form.get('right') == 'True':
            wsh.SendKeys("{RIGHT}")
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8080,debug=True)