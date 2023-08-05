from flask import Flask,render_template,request,session

app=Flask(__name__)
app.secret_key='deepu'

@app.route('/form')
def formPage():
    return render_template('index.html')

@app.route('/submitmsg',methods=['post'])
def formdata():
    msg=request.form['msg']
    session['msg']=msg
    print(session['msg'])
    return ('message stored')

if __name__=="__main__":
    app.run(debug=True)