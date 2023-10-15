from flask import render_template, Blueprint, request, flash
import json, os, uuid
import requests

main = Blueprint('main', __name__)

@main.route("/")
@main.route("/home")
def home():
    return render_template('home.html')

@main.route("/test_api")
def test_api():
    try:
        res = requests.get("http://api:3001/test")
        print(res.json())
    except Exception as e:
        print(e)
    return render_template('home.html')