from flask import Flask, render_template, request

app = Flask(__name__)

class RMS:
    def __init__(self):
        self.orders = []

    def AddOrder(self, id, name, quantity, table):
        order = {"id": id, "name": name, "quantity": quantity, "table": table}
        self.orders.append(order)
        return "Order added successfully."

    def UpdateOrder(self, id, name, quantity, table):
        for order in self.orders:
            if order["id"] == id:
                order["name"] = name
                order["quantity"] = quantity
                order["table"] = table
                return "Order updated successfully."
        return "Order not found"

    def DeleteOrder(self, id):
        for order in self.orders:
            if order["id"] == id:
                self.orders.remove(order)
                return "Order deleted successfully."
        return "Order not found"

    def SearchOrder(self, search):
        result = [order for order in self.orders if search.lower() in order["name"].lower()]
        if result:
            return result
        else:
            return "There is no order matching the search criteria."

@app.route('/', methods=["GET", "POST"])
def form_submit():
    if request.method == 'GET':
        return render_template("MAIN.html")

    id = request.form["idText"]
    name = request.form["NameText"]
    quantity = request.form["QuantityText"]
    table = request.form["TableText"]
    search = request.form["SearchText"]
    dbobj = RMS()

    if request.form["action_button"] == "Add an Order":
        ordersText = dbobj.AddOrder(int(id), name, int(quantity), int(table))
    elif request.form["action_button"] == "Update an Order":
        ordersText = dbobj.UpdateOrder(int(id), name, int(quantity), int(table))
    elif request.form["action_button"] == "Delete an Order":
        ordersText = dbobj.DeleteOrder(int(id))
    else:
        ret = dbobj.SearchOrder(search)
        if "There is no order" not in ret:
            ordersText = ">>>Number of orders retrieved is:" + str(len(ret)) + "\n"
            for order in ret:
                ordersText += str(order) + "\n"
        else:
            ordersText = ret

    return render_template("MAIN.html", i=id, n=name, q=quantity, t=table, sr=search, b=ordersText)

if __name__ == "__main__":
    app.run(port=9001)
