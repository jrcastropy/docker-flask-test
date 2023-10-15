from flask import render_template, Blueprint, request, flash
import json, os, uuid

main = Blueprint('main', __name__)

@main.route("/")
@main.route("/home")
def home():
    return render_template('home.html')