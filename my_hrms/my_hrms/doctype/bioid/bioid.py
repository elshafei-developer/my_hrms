import frappe
from frappe import _
from frappe.model.document import Document
from zk import ZK,const
from  zk.finger import Finger
from  zk.user import User
import json

class BioID(Document):
    pass
			
def connect_zk(employee_info,id_device):
    
	employee_id = employee_info['id_employee']
	employee_name = employee_info['employee_name']
	employee = employee_info['employee']
	has_finger = employee_info['has_finger']
 
	conn = None
	print(id_device)
	zk = ZK(id_device)
	try:
		print("connecting to device")
		conn = zk.connect()
		conn.disable_device()
		if has_finger == "Yes":
			users = conn.get_users()
			for user in users:
				if user.uid == int(employee_id):
					template = conn.get_user_template(uid=int(employee_id), temp_id=6)
					fingerprint_enrolled = bool(template) == False or template.template == b''
					if fingerprint_enrolled:
						conn.test_voice(20)			
						conn.enable_device()
						return {"fingerprint": False, "message": f"ID -{employee_id}- No Has Fingerprint in Device"}
					else:
						conn.set_user(uid=int(employee_id), name=employee_name,user_id=str(employee_id))
						finger = Finger(uid=int(employee_id), fid=template.fid,valid=template.valid, template=template.template)
						finger_json = finger.json_pack()

						conn.test_voice()
						conn.enable_device()
						return {"fingerprint": finger_json, "message": f"Add {employee_name} successful, With ID {employee_id}"}
			else:
				conn.test_voice(20)
				conn.enable_device()
				return {"fingerprint": False, "message": f"User with ID {employee_id} not found in device"}

		elif has_finger == "No":
			conn.test_voice(24)
			conn.set_user(uid=int(employee_id), name=employee_name,user_id=str(employee_id))
			conn.enroll_user(uid=int(employee_id),temp_id=6,user_id=str(employee_id))
			template = conn.get_user_template(uid=int(employee_id), temp_id=6)
			finger = Finger(uid=int(employee_id), fid=template.fid,valid=template.valid, template=template.template)
			finger_json = finger.json_pack()
			conn.enable_device()
			return {"fingerprint":finger_json, "message": _(f"Add {employee_name} successfully. His ID is {employee_id}.")}

	except Exception as e:
		print(f'time to connect to device {id_device} has expired')
		return {"fingerprint": False, "message": f"Error => {e}"}

@frappe.whitelist()
def get_fingerprint(data):

    data_json = json.loads(data)
    employee_info = {'employee_name': data_json['name_employee'], 'id_employee': data_json['id_employee'],'employee': data_json['employee'],'has_finger': data_json['has_finger']}
    id_device = data_json['id_device']
    
    status_finger = connect_zk(employee_info,id_device)
    return status_finger
    