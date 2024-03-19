from flask import request, Blueprint
from app import db  
from sqlalchemy import text


suspend_bp = Blueprint('suspend',__name__)


def find_sus_details(sus_no):
    try:
        
        query_result = db.session.execute(
            text(f"SELECT sus_details FROM tbl_suspend WHERE sus_no = {sus_no}")
        )
        result = query_result.fetchone()
        
        if result:
            sus_details = result[0]
            sus_details = sus_details.replace("\\n", "\n")
            return sus_details
        else:
            return "Details not available"
    except Exception as e:
        print(f"Error querying database: {e}")
        return "Error querying database"

# 별점누적
@suspend_bp.route('/suspend/1', methods=['GET', 'POST'])
def handle_sus_no_1():
    sus_no = 1  # 对应数据库中的 sus_no
    sus_details = find_sus_details(sus_no)
    
    if request.method == 'POST':
        # Handle POST request logic here
        return {"version": "2.0", "template": {"outputs": [{"simpleText": {"text": sus_details}}]}}
    else:
        # Handle GET request logic here
        return {"version": "2.0", "template": {"outputs": [{"simpleText": {"text": sus_details}}]}}

# 回 "음주운전적발"
@suspend_bp.route('/suspend/2', methods=['GET', 'POST'])
def handle_sus_no_2():
    sus_no = 2  #
    sus_details = find_sus_details(sus_no)
    
    if request.method == 'POST':
        
        return {"version": "2.0", "template": {"outputs": [{"simpleText": {"text": sus_details}}]}}
    else:
        
        return {"version": "2.0", "template": {"outputs": [{"simpleText": {"text": sus_details}}]}}

# "교통사고"
@suspend_bp.route('/suspend/3', methods=['GET', 'POST'])
def handle_sus_no_3():
    sus_no = 3  
    sus_details = find_sus_details(sus_no)
    
    if request.method == 'POST':
       
        return {"version": "2.0", "template": {"outputs": [{"simpleText": {"text": sus_details}}]}}
    else:
        
        return {"version": "2.0", "template": {"outputs": [{"simpleText": {"text": sus_details}}]}}

# "부정취득"
@suspend_bp.route('/suspend/4', methods=['GET', 'POST'])
def handle_sus_no_4():
    sus_no = 4  
    sus_details = find_sus_details(sus_no)
    
    if request.method == 'POST':
        
        return {"version": "2.0", "template": {"outputs": [{"simpleText": {"text": sus_details}}]}}
    else:
        
        return {"version": "2.0", "template": {"outputs": [{"simpleText": {"text": sus_details}}]}}
 
#보복운전 
@suspend_bp.route('/suspend/5', methods=['GET', 'POST'])
def handle_sus_no_5():
    sus_no = 5  
    sus_details = find_sus_details(sus_no)
    
    if request.method == 'POST':
       
        return {"version": "2.0", "template": {"outputs": [{"simpleText": {"text": sus_details}}]}}
    else:
        
        return {"version": "2.0", "template": {"outputs": [{"simpleText": {"text": sus_details}}]}}
  
# 불복절차
@suspend_bp.route('/suspend/6', methods=['GET', 'POST'])
def handle_sus_no_6():
    sus_no = 6  
    sus_details = find_sus_details(sus_no)
    
    if request.method == 'POST':
        
        return {"version": "2.0", "template": {"outputs": [{"simpleText": {"text": sus_details}}]}}
    else:
       
        return {"version": "2.0", "template": {"outputs": [{"simpleText": {"text": sus_details}}]}}