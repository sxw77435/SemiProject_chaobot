from flask import request, jsonify, Blueprint
from app import db  
from sqlalchemy import text


test_bp = Blueprint('test',__name__)


def update_data():
    urls_to_update = [
        {
            "test_no": 1,
            "url": "https://www.safedriving.or.kr/rersafetyed/rerSafetyedAltrCnclUView.do?menuCode=MN-PO-1123"
        },
        {
            "test_no": 2,
            "url": "https://www.safedriving.or.kr/guide/rerGuide07View.do?menuCode=MN-PO-1117"
        },
        {
            "test_no": 3,
            "url": "https://www.safedriving.or.kr/guide/rerGuide04View.do?menuCode=MN-PO-1114"
        },
        {
            "test_no": 4,
            "url": "https://youtu.be/NQBPjmEivlE"
        },
        {
            "test_no": 5,
            "url": "https://youtu.be/wjcdWb-wHtc"
        }
    ]

    for data in urls_to_update:
        # 使用 UPDATE 语句更新数据
        update_query = "UPDATE tbl_TEST SET TEST_URL = :url WHERE TEST_NO = :test_no;"
        db.session.execute(text(update_query), {'url': data['url'], 'test_no': data['test_no']})
        db.session.commit()

@test_bp.route('/test/update', methods=['POST'])
def update_test_data():
    update_data()
    return jsonify({"message": "Data updated successfully!"})

def find_test_url(test_no):
    try:
       
        query_result = db.session.execute(
            text(f"SELECT test_url FROM tbl_test WHERE test_no = {test_no}")
        )
        result = query_result.fetchone()
        
        if result:
            test_url = result[0]
            return test_url
        else:
            return "Details not available"
    except Exception as e:
        print(f"Error querying database: {e}")
        return "Error querying database"
    
@test_bp.route('/test/1',methods=['GET', 'POST'])
def handel_test_1():
    test_no=1
    test_url = find_test_url(test_no)
    if request.method == 'POST':
        return {
                "version": "2.0",
                "template": {
                    "outputs": [
                        
                        {
                            "simpleText": {
                                "link": {
                                    "web": test_url
                                }
                            }
                        }
                    ]
                }
            }
    
    
@test_bp.route('/test/2',methods=['GET', 'POST'])
def handel_test_2():
    test_no=2
    test_url = find_test_url(test_no)
    if request.method == 'POST':  
        return {
                "version": "2.0",
                "template": {
                    "outputs": [
                        
                        {
                            "simpleText": {
                                "link": {
                                    "web": test_url
                                }
                            }
                        }
                    ]
                }
            }
    
@test_bp.route('/test/3',methods=['GET', 'POST'])
def handel_test_3():
    test_no=3
    test_url = find_test_url(test_no)
    if request.method == 'POST':
    
        return {
                "version": "2.0",
                "template": {
                    "outputs": [
                        
                        {
                            "simpleText": {
                                "link": {
                                    "web": test_url
                                }
                            }
                        }
                    ]
                }
            }
    
@test_bp.route('/test/4',methods=['GET', 'POST'])
def handel_test_4():
    test_no=4
    test_url = find_test_url(test_no)
    if request.method == 'POST':
        return {
                "version": "2.0",
                "template": {
                    "outputs": [
                        
                        {
                            "simpleText": {
                                "link": {
                                    "web": test_url
                                }
                            }
                        }
                    ]
                }
            }
    
@test_bp.route('/test/5',methods=['GET', 'POST'])
def handel_test_5():
    test_no=5
    test_url = find_test_url(test_no)
    if request.method == 'POST':
        return {
                "version": "2.0",
                "template": {
                    "outputs": [
                        
                        {
                            "simpleText": {
                                "link": {
                                    "web": test_url
                                }
                            }
                        }
                    ]
                }
            }
def find_test_details(test_no):
    try:
        # 假设您的表格名称为 tbl_suspend，sus_no 是主键
        query_result = db.session.execute(
            text(f"SELECT test_details FROM tbl_test WHERE test_no = {test_no}")
        )
        result = query_result.fetchone()
        
        if result:
            test_details = result[0]
            test_details = test_details.replace("\\n", "\n")
            return test_details
        else:
            return "Details not available"
    except Exception as e:
        print(f"Error querying database: {e}")
        return "Error querying database"

@test_bp.route('/test/6',methods =['GET','POST'])
def test_6():
    test_no =6
    test_details=find_test_details(test_no)
    
    if request.method == 'POST':
        # Handle POST request logic here
        return {"version": "2.0", "template": {"outputs": [{"simpleText": {"text": test_details}}]}}
    else:
        # Handle GET request logic here
        return {"version": "2.0", "template": {"outputs": [{"simpleText": {"text": test_details}}]}}
        
    
