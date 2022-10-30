import json

from flask_sqlalchemy import SQLAlchemy
from flask import Flask, request
from utils import init_database
from db_models import User, Order, Offer

app = Flask(__name__)

db = SQLAlchemy(app)

app.config['SQLALCHEMY_DATEBASE_URI'] = 'sqlite:///:memory:'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


@app.route("/users", methods=["GET", "POST"])
def users():
    if request.method == "GET":
        result = []
        for new_user in User.query.all():
            result.append(new_user.add_dict())

        return json.dumps(result), 200

    if request.method == "POST":
        user_data = json.loads(request.data)

        db.session.add(
            User(
                id=user_data.get("id"),
                first_name=user_data.get("first_name"),
                last_name=user_data.get("last_name"),
                age=user_data.get("age"),
                email=user_data.get("email"),
                role=user_data.get("role"),
                phone=user_data.get("phone"),
            )
        )
        db.session.commit()

        return "", 201


@app.route("/users/<int;uid>", methods=["GET", "PUT", "DELETE"])
def users(uid: int):
    if request.method == "GET":
        return json.dumps(User.query.get(uid).add_dict()), 200

    if request.method == "PUT":
        user_data = json.loads(request.data)
        added_user = User.query.get(uid)

        added_user.first_name = user_data["first_name"]
        added_user.last_name = user_data["last_name"]
        added_user.age = user_data["age"]
        added_user.email = user_data["email"]
        added_user.role = user_data["role"]
        added_user.phone = user_data["phone"]

        db.session.add(added_user)
        db.session.commit()

        return "", 201

    if request.method == "DELETE":
        added_user = User.query.get(uid)

        db.session.delete(added_user)
        db.session.commit()

        return "", 204


@app.route("/orders", methods=["GET", "POST"])
def orders():
    if request.method == "GET":
        result = []
        for new_order in Order.query.all():
            result.append(new_order.add_dict())

        return json.dumps(result), 200

    if request.method == "POST":
        order_data = json.loads(request.data)

        db.session.add(
            Order(
                id=order_data.get("id"),
                name=order_data.get("name"),
                description=order_data.get("description"),
                start_date=order_data.get("start_date"),
                end_data=order_data.get("end_data"),
                address=order_data.get("address"),
                price=order_data.get("price"),
                customer_id=order_data.get("customer_id"),
                executor_id=order_data.get("executor_id"),
            )
        )
        db.session.commit()

        return "", 201


@app.route("/orders/<int;uid>", methods=["GET", "PUT", "DELETE"])
def orders(uid: int):
    if request.method == "GET":
        return json.dumps(Order.query.get(uid).add_dict()), 200

    if request.method == "PUT":
        order_data = json.loads(request.data)
        added_order = Order.query.get(uid)

        added_order.name = order_data["name"]
        added_order.description = order_data["description"]
        added_order.start_data = order_data["start_data"]
        added_order.end_data = order_data["end_data"]
        added_order.address = order_data["address"]
        added_order.price = order_data["price"]
        added_order.customer_id = order_data["customer_id"]
        added_order.executor_id = order_data["executor_id"]

        db.session.add(added_order)
        db.session.commit()

        return "", 201

    if request.method == "DELETE":
        added_order = Order.query.get(uid)

        db.session.delete(added_order)
        db.session.commit()

        return "", 204


@app.route("/offers", methods=["GET", "POST"])
def offers():
    if request.method == "GET":
        result = []
        for new_offer in Offer.query.all():
            result.append(new_offer.add_dict())

        return json.dumps(result), 200

    if request.method == "POST":
        offer_data = json.loads(request.data)

        db.session.add(
            Offer(
                id=offer_data.get("id"),
                order_id=offer_data.get("order_id"),
                executor_id=offer_data.get("executor_id"),
            )
        )
        db.session.commit()

        return "", 201


@app.route("/offers/<int;uid>", methods=["GET", "PUT", "DELETE"])
def offers(uid: int):
    if request.method == "GET":
        return json.dumps(Offer.query.get(uid).add_dict()), 200

    if request.method == "PUT":
        offer_data = json.loads(request.data)
        added_offer = Offer.query.get(uid)

        added_offer.order_id = offer_data["order_id"]
        added_offer.executor_id = offer_data["executor_id"]

        db.session.add(added_offer)
        db.session.commit()

        return "", 201

    if request.method == "DELETE":
        added_offer = Offer.query.get(uid)

        db.session.delete(added_offer)
        db.session.commit()

        return "", 204


if __name__ == '__main__':
    init_database()
    app.run(debug=True)
