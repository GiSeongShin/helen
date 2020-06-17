Process
=======

* 목록 페이지 접속 시 캠페인의 리스트를 받는 요청을 보낸다.

def init_main_page():
    
    return campaign_list

* 등록 페이지에서 작성한 템플릿을 DB 에 적재하는 요청을 보낸다.

def add_campaign(template):
	
	return response

* 수정 페이지 접근 시 해당 campaign 에 대한 조회요청, 수정사항 반영 시 update 요청을 보낸다.

def get_modify_campaign(campaign_id):
	
	return template_value_dict

def update_modify_campaign(campaign_id, template):
	
	return response
