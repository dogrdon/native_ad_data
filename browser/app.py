from flask import Flask, request
from pymongo import MongoClient
import bson.json_util

app = Flask(__name__)

client = MongoClient()
db = client.native_ads

@app.route('/source/<provider>')
def source(provider):
	start = request.args.get('start') or 0
	start = max(int(start) - 1, 0)
	end = request.args.get('end') or 20
	end = int(end)
	width = end - start
	source = db.ads.find({"provider":provider}).skip(start).limit(width)
	return bson.json_util.dumps(list(source))

if __name__ == "__main__":
	app.run(debug=True)
