from app import db

class acception(db.Model):
    acc_no = db.Column(db.Integer,primary_key=True,comment='인증코드')
    acc_region = db.Column(db.String(100),comment='인증지역')
    acc_nation = db.Column(db.String(2000),comment='인증나라')
    
class suspend(db.Model):
    sus_no = db.Column(db.Integer,primary_key=True,comment='정지코드')
    sus_reason = db.Column(db.String(50),comment='정지사유')
    sus_details = db.Column(db.String(1000),comment='사유상세')
    
class update(db.Model):
    update_no = db.Column(db.Integer,primary_key=True,comment='갱신코드')
    update_category = db.Column(db.String(50),comment='갱신종류')
    update_age = db.Column(db.String(20),comment='운전자 나이')
    update_detail= db.Column(db.String(2000),comment='준비몰')
    
    
class test(db.Model):
    test_no = db.Column(db.Integer,primary_key=True,comment='시험코드')
    test_content = db.Column(db.String(50),comment='시험내용')
    test_details = db.Column(db.String(1000),comment='시험상세')
    test_url= db.Column(db.String(1000),comment='시험링크')