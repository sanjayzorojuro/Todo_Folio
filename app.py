from flask import Flask,render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]='sqlite:///MyPro.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False
db=SQLAlchemy(app)

class todos(db.Model):
    sno=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(100),nullable=False)
    desc=db.Column(db.String(500),nullable=False)
    date_time=db.Column(db.DateTime,default=datetime.utcnow)

    def __repr__(self) ->str:
        return f"{self.sno}-{self.title}"




@app.route('/')
def base():
    return render_template('home.html')



@app.route('/about')
def about():
    return render_template('about.html')




@app.route('/todo',methods=['GET','POST'])
def todoe():
    if request.method == 'POST':
        title = request.form['title']
        desc = request.form['desc']
        todo = todos(title=title, desc=desc)
        db.session.add(todo)
        db.session.commit()

    alltodo=todos.query.all()
    return render_template('todo.html',alltodo=alltodo)

@app.route('/delete/<int:sno>')
def delete(sno):
    alltodo=todos.query.filter_by(sno=sno).first()
    db.session.delete(alltodo)
    db.session.commit()    
    return redirect('/todo')


@app.route('/update/<int:sno>', methods=['GET', 'POST'])
def update(sno):
    todo = todos.query.get_or_404(sno)

    if request.method == 'POST':
        todo.title = request.form['title']
        todo.desc = request.form['desc']
        db.session.commit()
        return redirect('/todo')

    return render_template('update.html', todo=todo)







@app.route('/github')
def github():
    return render_template('github.html')

if __name__ == '__main__':
    app.run(debug=True)
