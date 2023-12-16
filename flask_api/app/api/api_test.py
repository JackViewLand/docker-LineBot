from flask import Blueprint,request,jsonify
# BluePrint參數設定
api_test = Blueprint('api_test', __name__)
# ***********************************************
# Create GET http://IP:5000/
# ***********************************************
@api_test.route('/hi',methods=['GET'])
def index():  
  return "hi"
