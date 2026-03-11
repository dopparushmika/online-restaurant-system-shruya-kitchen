from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

menu_items = {
    "biryani": 100,
    "Pizza": 120,
    "Pasta": 150,
    "mutton curry": 200,
    "Soda": 30
}

orders = []
reviews = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/menu')
def menu():
    return render_template('menu.html', menu=menu_items)

@app.route('/order', methods=['GET', 'POST'])
def order():
    order_placed = False
    selected_items = []
    order_total = 0

    if request.method == 'POST':
        selected_items = request.form.getlist('items')
        order_total = sum(menu_items[item] for item in selected_items)
        orders.append({"items": selected_items, "total": order_total})
        order_placed = True

    return render_template(
        'order.html',
        menu=menu_items,
        order_placed=order_placed,
        selected_items=selected_items,
        order_total=order_total
    )
@app.route('/bill/<int:order_id>')
def bill(order_id):
    order = orders[order_id]
    return render_template('bill.html', order=order)

@app.route('/review', methods=['GET', 'POST'])
def review():
    if request.method == 'POST':
        name = request.form['name']
        comment = request.form['comment']
        reviews.append({"name": name, "comment": comment})
        return redirect(url_for('review'))
    return render_template('review.html', reviews=reviews)

if __name__ == '__main__':
    app.run(debug=True)
