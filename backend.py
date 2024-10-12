from flask import Flask
from flask import jsonify
import json
from . import app
from repository import *

rs = RepoService()

@app.route("/")
def init():
    rs.syncPlayersWithSpreadsheet()