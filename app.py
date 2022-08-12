from flask import Flask,jsonify
from flask_cors import CORS
from data import Nums


app = Flask(__name__)

CORS(app)




@app.route("/<int:nbr>")
def hello_world(nbr):
	print(len(Nums))
	print(type(nbr))
	if (nbr > len(Nums)):
		return jsonify({"message":'done'})
	maxnbr = min(nbr+15, len(Nums))
	return jsonify(Nums[nbr:maxnbr])





if __name__ == '__main__':
	app.run(debug=True)