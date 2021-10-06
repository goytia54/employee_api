from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///employees.db"
db = SQLAlchemy(app)


class EmployeeSchema(Schema):
    id = fields.Int()
    gender = fields.Str()


class Employees(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    gender = db.Column(db.String)


employee_schema = EmployeeSchema()


@app.route("/employees")
def get_employees():
    employees = Employees.query.all()
    result = employee_schema.dump(employees, many=True)
    return jsonify(result)
