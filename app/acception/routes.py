from flask import request, Blueprint,jsonify
from app import db  
from sqlalchemy import text
from app.countries import countries_dict



acception_bp = Blueprint('acception',__name__)

def find_acc_nation(acc_no):
    try:
        
        query_result = db.session.execute(
            text(f"SELECT acc_nation FROM tbl_acception WHERE acc_no = {acc_no}")
        )
        result = query_result.fetchone()
        
        if result:
            acc_nation = result[0]
            acc_nation = acc_nation.replace("\\n", "\n")
            return acc_nation
        else:
            return "Details not available"
    except Exception as e:
        print(f"Error querying database: {e}")
        return "Error querying database"

@acception_bp.route('/acc_assia',methods =['GET','POST'])
def acc_assia():
    acc_no =1
    acc_nation=find_acc_nation(acc_no)
    
    if request.method == 'POST':
        # Handle POST request logic here
        return {"version": "2.0", "template": {"outputs": [{"simpleText": {"text": acc_nation}}]}}
    else:
        # Handle GET request logic here
        return {"version": "2.0", "template": {"outputs": [{"simpleText": {"text": acc_nation}}]}}
    
@acception_bp.route('/acc_america',methods =['GET','POST'])
def acc_america():
    acc_no =2
    acc_nation=find_acc_nation(acc_no)
    
    if request.method == 'POST':
        # Handle POST request logic here
        return {"version": "2.0", "template": {"outputs": [{"simpleText": {"text": acc_nation}}]}}
    else:
        # Handle GET request logic here
        return {"version": "2.0", "template": {"outputs": [{"simpleText": {"text": acc_nation}}]}}
    
@acception_bp.route('/acc_europe',methods =['GET','POST'])
def acc_europe():
    acc_no =3
    acc_nation=find_acc_nation(acc_no)
    
    if request.method == 'POST':
        # Handle POST request logic here
        return {"version": "2.0", "template": {"outputs": [{"simpleText": {"text": acc_nation}}]}}
    else:
        # Handle GET request logic here
        return {"version": "2.0", "template": {"outputs": [{"simpleText": {"text": acc_nation}}]}}
    
@acception_bp.route('/acc_middle',methods =['GET','POST'])
def acc_middle():
    acc_no =4
    acc_nation=find_acc_nation(acc_no)
    
    if request.method == 'POST':
        # Handle POST request logic here
        return {"version": "2.0", "template": {"outputs": [{"simpleText": {"text": acc_nation}}]}}
    else:
        # Handle GET request logic here
        return {"version": "2.0", "template": {"outputs": [{"simpleText": {"text": acc_nation}}]}}
    
@acception_bp.route('/acc_africa',methods =['GET','POST'])
def acc_africa():
    acc_no =5
    acc_nation=find_acc_nation(acc_no)
    
    if request.method == 'POST':
        # Handle POST request logic here
        return {"version": "2.0", "template": {"outputs": [{"simpleText": {"text": acc_nation}}]}}
    else:
        # Handle GET request logic here
        return {"version": "2.0", "template": {"outputs": [{"simpleText": {"text": acc_nation}}]}}


@acception_bp.route('/acc_ask', methods=['GET', 'POST'])
def acc_ask():
    if request.method == 'GET':
        return "나라를 말해보세요~~"

    if request.method == 'POST':
        data = request.get_json()
        country_name = data['userRequest']['utterance']

        if country_name in countries_dict:
            response_body = {
                "version": "2.0",
                "template": {
                    "outputs": [
                        {
                            "simpleText": {
                                "text": f"네, {country_name}에 한국운전면허를 쓸 수 있습니다"
                            }
                        }
                    ]
                }
            }
        else:
            response_body = {
                "version": "2.0",
                "template": {
                    "outputs": [
                        {
                            "simpleText": {
                                "text": f"{country_name}에 한국운전면허를 쓸 수 없습니다"
                            }
                        }
                    ]
                }
            }

        return jsonify(response_body)
    


