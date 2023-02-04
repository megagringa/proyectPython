from flask import Flask
from flask import render_template

app=Flask(__name__)

@app.route('/')
def inicio():
    return render_template('sitio/index.html')

@app.route('/libros')
def libros():
    return render_template('sitio/libros.html')

@app.route('/nosotros')
def nosotros():
    return render_template('sitio/nosotros.html')

@app.route('/admin')
def admin_index():
    return render_template('admin/index.html') 
@app.route('/admin/login')
def admin_login():
    return render_template('admin/login.html')       

if __name__=='__main__':
    app.run(debug=True)