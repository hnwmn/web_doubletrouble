from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('store.html')

@app.route("/checkout")
def checkout():
    # get all 'price' parameters submitted
    prices = request.args.getlist("price")
    price = None
    flag = False
    success = False
    payment_attempted = False

    if prices:
        payment_attempted = True
        try:
            price = float(prices[-1])  # vuln takes the last price param
            
            # if multiple price parameters are detected show flag
            if len(prices) > 1:
                flag = True
                success = True
            elif price >= 199:
                success = True
        except ValueError:
            pass

    return render_template("store.html", flag=flag, price=price, success=success, payment_attempted=payment_attempted)
        
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)