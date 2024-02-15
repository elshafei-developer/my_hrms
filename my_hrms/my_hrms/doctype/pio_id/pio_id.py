# Copyright (c) 2024, hassan hussein mohammed and contributors
# For license information, please see license.txt

import frappe
from frappe import _
from frappe.model.document import Document
from zk import ZK
from  zk.finger import Finger
import json
import time # Hypothetical function

class PIOID(Document):
	# def validate(self):
		# ZK_devices = frappe.db.get_list("ZK Device", pluck = "id_device")
		# if self.fingerprints == None:
		# 	employee_info = {'employee_name': self.full_name, 'id_employee': self.id_employee_in_device}
		# 	for device in ZK_devices:
		# 		print("-"*40)
		# 		finger = connect_zk(employee_info,device)
		# 		print(finger["fingerprint"])
		# 		if finger["fingerprint"] == False:
		# 			pass
		# 		else:
		# 			self.finger_template = finger["fingerprint"]['template']
		# 			self.finger_size = finger["fingerprint"]['size']
		# 			self.fingerprints = "Yes"
		# 			break
		# 		print("-"*40)


	def before_insert(self):
		employees = frappe.db.get_list("PIO ID", pluck="employee")

		if self.employee in employees:
			frappe.throw(f"Employee {self.full_name} already exists")

		exists_employee = frappe.db.exists({"doctype": "PIO ID", "id_employee_in_device": self.id_employee_in_device})
		if exists_employee:
			frappe.throw(f"The Employee {exists_employee} has ID {self.id_employee_in_device} already")
			
def connect_zk(employee_info,id_device):
	employee_id = employee_info['id_employee']
	employee_name = employee_info['employee_name']
	conn = None
	print(id_device)
	zk = ZK(id_device)
	try:
		print("connecting to device")
		conn = zk.connect()
		conn.disable_device()

		conn.set_user(uid=int(employee_id), name=employee_name)
		template = conn.get_user_template(uid=int(employee_id), temp_id=6)

		if template.template == b'':
			conn.test_voice()
			conn.enable_device()
			return {"fingerprint": False, "message": f"ID {employee_id} has no fingerprint in device ID {id_device}"}
		else:
			print(f"ID {employee_id} has fingerprint in device ID {id_device}")
   
			finger = Finger(uid=int(employee_id), fid=template.fid,valid=template.valid, template=template.template)
   
			finger_json = finger.json_pack()
			print(finger_json)
			conn.test_voice()
			conn.enable_device()
			return {"fingerprint": finger_json, "message": f"ID {employee_id} has fingerprint in device ID {id_device}"}

	except Exception as e:
		print(f'time to connect to device {id_device} has expired')
		return {"fingerprint": False, "message": f"Error: {e}"}



def connect_zk1(employee_info,id_device):
	employee_id = employee_info['id_employee']
	employee_name = employee_info['employee_name']
	employee = employee_info['employee']
	has_finger = employee_info['has_finger']
 
	# employees = frappe.db.get_list("PIO ID", pluck="employee")

	# if employee in employees:
	# 	return {"fingerprint": False, "message": f"Employee {employee_name} already exists"}

	exists_employee = frappe.db.exists({"doctype": "PIO ID", "id_employee_in_device": employee_id})
	if exists_employee:
		return {"fingerprint": False, "message": f"The Employee {exists_employee} has ID {employee_id} already"}
 
	conn = None
	print(id_device)
	zk = ZK(id_device)
	try:
		print("connecting to device")
		conn = zk.connect()
		conn.disable_device()
		if has_finger == "Yes":
			template = conn.get_user_template(uid=int(employee_id), temp_id=6)
			fingerprint_enrolled = bool(template)
			if fingerprint_enrolled == False or template.template == b'':
				conn.test_voice(20)
				conn.enable_device()
				return {"fingerprint": False, "message": f"ID {employee_id} no has fingerprint in device ID {id_device}"}
			else:
				conn.set_user(uid=int(employee_id), name=employee_name)
				finger = Finger(uid=int(employee_id), fid=template.fid,valid=template.valid, template=template.template)
				finger_json = finger.json_pack()
				conn.test_voice()
				conn.enable_device()
				return {"fingerprint": finger_json, "message": f"Add {employee} successful. and He has fingerprint in device ID {id_device}, his ID is {employee_id}"}
		elif has_finger == "No":
			conn.set_user(uid=int(employee_id), name=employee_name)
			conn.test_voice()
			finger = Finger(uid=int(employee_id), fid=6,valid=1, template=b'')
			finger_json = finger.json_pack()

			conn.enable_device()
			return {"fingerprint":finger_json, "message": _("The employee has been successfully added to the device. His ID is 55. Please now add the fingerprints to the device")}

	except Exception as e:
		print(f'time to connect to device {id_device} has expired')
		return {"fingerprint": False, "message": f"Error: Device that have ID {id_device} Is Not connection => {e}"}

@frappe.whitelist()
def get_fingerprint(data):

    data_json = json.loads(data)
    employee_info = {'employee_name': data_json['name_employee'], 'id_employee': data_json['id_employee'],'employee': data_json['employee'],'has_finger': data_json['has_finger']}
    id_device = data_json['id_device']
    
    status_finger = connect_zk1(employee_info,id_device)
    return status_finger
    