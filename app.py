from flask import Flask, request, redirect, render_template
from Sweet import Sweet
from SweetShop import SweetShop

app = Flask(__name__)
shop = SweetShop()

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html", sweets=shop.get_sweets())

@app.route("/add", methods=["POST"])
def add():
    try:
        sweet = Sweet(
            request.form["id"],
            request.form["name"],
            request.form["category"],
            float(request.form["price"]),
            int(request.form["quantity"])
        )
        shop.add_sweet(sweet)
    except Exception as e:
        return f"Error adding sweet: {str(e)}"
    return redirect("/")

@app.route("/delete/<sweet_id>", methods=["POST"])
def delete(sweet_id):
    try:
        shop.delete_sweet(sweet_id)
    except Exception as e:
        return f"Error deleting sweet: {str(e)}"
    return redirect("/")

@app.route("/purchase/<sweet_id>", methods=["POST"])
def purchase(sweet_id):
    try:
        qty = int(request.form["qty"])
        shop.purchase_sweet(sweet_id, qty)
    except Exception as e:
        return f"Error purchasing sweet: {str(e)}"
    return redirect("/")

@app.route("/restock/<sweet_id>", methods=["POST"])
def restock(sweet_id):
    try:
        qty = int(request.form["qty"])
        shop.restock_sweet(sweet_id, qty)
    except Exception as e:
        return f"Error restocking sweet: {str(e)}"
    return redirect("/")

@app.route("/search", methods=["GET"])
def search():
    name = request.args.get("name", "")
    category = request.args.get("category", "")
    try:
        min_price = float(request.args.get("min_price", 0))
        max_price = float(request.args.get("max_price", float("inf")))
    except:
        min_price = 0
        max_price = float("inf")

    results = shop.search_sweets(name, category, min_price, max_price)
    return render_template("index.html", sweets=results)

if __name__ == "__main__":
    app.run(debug=True)
