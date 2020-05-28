from flask import Flask, render_template, url_for, redirect
from forms import RegistrationForm, Ludo, Slots, Dice, Roulette, CoinFlip, Search
from functions import data_entry, registration as register, coinflip_func, dice_func, slots_func, roulette_func, ludo_func
from db import search as searche, find, transactions

app = Flask(__name__)
app.config['SECRET_KEY']='93f7cce5d349ab7562fef0f08f788a99'

@app.route('/home')
@app.route('/')
def home():
    searches = searche()
    transaction=transactions()[0]
    return render_template('home.html', search=searches, transaction=transaction)

@app.route('/live')
def live():
    return render_template('live.html')

@app.route('/shop')
def shop():
    return render_template('shop.html')

@app.route('/search', methods=['GET', 'POST'])
def search():
    form = Search()
    name=form.name.data
    if form.validate_on_submit():
        rows = find(name)
        try:
            result=rows[0]
        except:
            return render_template('search.html', error="No match found", form=form)
        return render_template('search.html', result=result)
    return render_template('search.html', form=form)

@app.route('/registration', methods=['POST', 'GET'])
def registration():
    form = RegistrationForm()
    if form.validate_on_submit():
        name = form.name.data
        link = form.link.data
        promo = form.promo.data
        result = register(name, link, promo)
        hexa = result['hex']
        answer = data_entry(result)
        searches = searche()
        if answer=="SUCCESS!":
            return render_template('home.html', answer=answer, hexa=hexa, search=searches)
        else:
            return render_template('home.html', answer=answer, search=searches)
    return render_template('registration.html', form=form)

@app.route('/148839c49a7cd85bf77685f1f2929464')
def admin():
    return render_template('/admin.html')

@app.route('/a64e343c62182448d29112b2d38729b2',methods=['POST', 'GET'])
def coinflip():
    form = CoinFlip()
    if form.validate_on_submit():
        supply={'id_num':form.id_num.data, 'prediction':form.prediction.data, 'amount':form.bet_amount.data, 'answer':None}
        result=coinflip_func(supply)
        return render_template('coinflip.html', result=result)
    return render_template('coinflip.html', form=form)

@app.route('/1bf4b374d40f2497b75a24f0ea6db4ac',methods=['POST', 'GET'])
def dice():
    form=Dice()
    if form.validate_on_submit():
        supply={'id_num':form.id_num.data, 'amount':form.bet_amount.data, 'answer':None, 'user':None, 'cpu':None}
        result = dice_func(supply)
        return render_template('dice.html', result=result)
    return render_template('dice.html', form=form)

@app.route('/8fa2b6348e5494548f7e825ee637f3d1',methods=['POST', 'GET'])
def roulette():
    form = Roulette()
    if form.validate_on_submit():
        supply={'id_num':form.id_num.data, 'amount':form.bet_amount.data, 
                'color':form.color.data, 'result':None, 'answer':None,
                'prediction':form.prediction.data}
        result=roulette_func(supply)
        return render_template('roulette.html', result=result)
    return render_template('roulette.html',form=form)

@app.route('/7c81c45636a517644bece883b1c845ac',methods=['POST', 'GET'])
def slots():
    form = Slots()
    if form.validate_on_submit():
        supply={'id_num':form.id_num.data, 'amount':form.bet_amount.data, 'answer':None, 'display':None}
        result=slots_func(supply)
        return render_template('slots.html', result=result)
    return render_template('slots.html',form=form)

@app.route('/87a0cdbf8e78b4a1e55db09cd572c09e',methods=['POST', 'GET'])
def ludo():
    form=Ludo()
    if form.validate_on_submit():
        supply={'id1':form.id1.data,'id2':form.id2.data,'id3':form.id3.data,'id4':form.id4.data,'amount':form.bet_amount.data, 'answer':None}
        result=ludo_func(supply)
        return render_template('ludo.html', result=result)
    return render_template('ludo.html', form=form)


if __name__ == "__main__":
    app.run(debug=True)