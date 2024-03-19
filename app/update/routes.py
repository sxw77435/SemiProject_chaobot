from flask import request, jsonify, Blueprint
from app import db  
from sqlalchemy import text


update_bp = Blueprint('update',__name__)

def find_update_detail(update_no):
    try:
        # 假设您的表格名称为 tbl_suspend，sus_no 是主键
        query_result = db.session.execute(
            text(f"SELECT update_detail FROM tbl_update WHERE update_no = {update_no}")
        )
        result = query_result.fetchone()
        
        if result:
            update_detail = result[0]
            update_detail = update_detail.replace("\\n", "\n")
            return update_detail
        else:
            return "Details not available"
    except Exception as e:
        print(f"Error querying database: {e}")
        return "Error querying database"
    
    # 1종 75세미만
@update_bp.route('/update/1/down75',methods=['GET', 'POST'])
def handel_update_1_down75():
    update_no=1
    update_detail = find_update_detail(update_no)
    
    if request.method == 'POST':
        # Handle POST request logic here
        return {"version": "2.0", "template": {"outputs": [{"simpleText": {"text": update_detail}}]}}
    else:
        # Handle GET request logic here
        return {"version": "2.0", "template": {"outputs": [{"simpleText": {"text": update_detail}}]}}
    
    #1종 75세 이상
@update_bp.route('/update/1/up75',methods=['GET', 'POST'])
def handel_update_1_up75():
    update_no=2
    update_detail = find_update_detail(update_no)
    
    if request.method == 'POST':
        # Handle POST request logic here
        return {"version": "2.0", "template": {"outputs": [{"simpleText": {"text": update_detail}}]}}
    else:
        # Handle GET request logic here
        return {"version": "2.0", "template": {"outputs": [{"simpleText": {"text": update_detail}}]}}

#  2종 70세 미만
@update_bp.route('/update/2/down70',methods=['GET', 'POST'])
def handel_update_2_down70():
    update_no=3
    update_detail = find_update_detail(update_no)
    
    if request.method == 'POST':
        # Handle POST request logic here
        return {"version": "2.0", "template": {"outputs": [{"simpleText": {"text": update_detail}}]}}
    else:
        # Handle GET request logic here
        return {"version": "2.0", "template": {"outputs": [{"simpleText": {"text": update_detail}}]}}

# 2종 70세 이상
@update_bp.route('/update/2/up70',methods=['GET', 'POST'])
def handel_update_2_up70():
    update_no=4
    update_detail = find_update_detail(update_no)
    
    if request.method == 'POST':
        # Handle POST request logic here
        return {"version": "2.0", "template": {"outputs": [{"simpleText": {"text": update_detail}}]}}
    else:
        # Handle GET request logic here
        return {"version": "2.0", "template": {"outputs": [{"simpleText": {"text": update_detail}}]}}

# 2종 75세 이상

@update_bp.route('/update/2/up75',methods=['GET', 'POST'])
def handel_update_2_up75():
    update_no=5
    update_detail = find_update_detail(update_no)
    
    if request.method == 'POST':
        # Handle POST request logic here
        return {"version": "2.0", "template": {"outputs": [{"simpleText": {"text": update_detail}}]}}
    else:
        # Handle GET request logic here
        return {"version": "2.0", "template": {"outputs": [{"simpleText": {"text": update_detail}}]}}