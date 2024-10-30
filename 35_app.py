from flask import Flask, request, render_template, redirect, url_for
from models import db, Cars

app = Flask(__name__)

host = 'localhost'
port = 5432
database = 'flask_db'
user = 'postgres'
password = 'irakli24'

app.secret_key = 'secret'

app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db.init_app(app)

@app.route('/')
def Index():
    all_data = Cars.query.all()
    print(all_data)
    return render_template('index.html', cars=all_data)



@app.route('/insert', methods=['GET', 'POST'])
def insert():

    if request.methods == 'POST':

        manufacturer = request.form['manufacturer']
        model = request.form['model']
        instock = request.form['instock']
        price = request.form['price']

        car = Cars(manufacturer, model, instock, price)
        db.session.add(car)
        db.session.commit()

        return redirect(url_for('Index'))


@app.route('/delete/<id>', methods=['GET', 'POST'])
def delete(id):
    car = Cars.query.get(id)
    db.session.delete(car)
    db.session.commit()
    return redirect(url_for('Index'))


@app.route('/update/<id>', methods=['GET', 'POST'])
def update(id):
    if request.method == 'POST':
        car = Cars.query.get(id)
        
        car.manufacturer = request.form['manufacturer']
        car.model = request.form['model']
        car.instock = request.instock['instock']
        car.price = request.price['price']
        
        db.session.commit()
        return redirect(url_for('Index'))


if __name__ == '__main__':

    with app.app_context():
        db.create_all()

    app.run(debug=True)







# from flask import Flask, request, render_template, redirect, url_for
# from models import db, Cars

# app = Flask(__name__)

# host = 'localhost'
# port = 5432
# database = 'flask_db'
# user = 'postgres'
# password = 'Tika2018'
# app.secret_key = 'secret'
# app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db.init_app(app)

# @app.route('/')
# def Index():
#     all_data = Cars.query.all()
#     print(all_data)
#     return render_template('index.html', cars=all_data)


# @app.route('/insert', methods=['GET', 'POST'])
# def insert():

#     if request.methods == 'POST':
#         manufacturer = request.form['manufacturer']
#         model = request.form['model']
#         instock = request.form['instock']
#         price = request.form['price']
#         car = Cars(manufacturer, model, instock, price)
#         db.session.add(car)
#         db.session.commit()
#         return redirect(url_for('Index'))


# @app.route('/delete/<id>/', methods=['GET', 'POST'])
# def delete(id):
#     car = Cars.query.get(id)
#     db.session.delete(car)
#     db.session.commit()
#     return redirect(url_for('Index'))


# @app.route('/update/<id>', methods=['GET', 'POST'])
# def update(id):
#     if request.methods == 'POST':
#         car = Cars.query.get(id)
#         car.manufacturer = request.form['manufacturer']
#         car.model = request.form['model']
#         car.instock = request.form['instock']
#         car.price = request.form['price']
#         db.session.commit()
#         return redirect(url_for('Index'))


# if __name__ == '__main__':

#     with app.app_context():
#         db.create_all()
#     app.run(debug=True)