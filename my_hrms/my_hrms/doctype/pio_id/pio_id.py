# Copyright (c) 2024, hassan hussein mohammed and contributors
# For license information, please see license.txt

import frappe
from frappe import _
from frappe.model.document import Document
from zk import ZK
from  zk.finger import Finger

class PIOID(Document):
	def validate(self):
     
		ZK_devices = frappe.db.get_list("ZK Device", pluck = "id_device")
		id_employee = self.id_employee_in_device

		if self.fingerprints == None:
			for device in ZK_devices:
				print("-"*40)
				finger = connect_zk(id_employee,device)
				print(finger["fingerprint"])
				if finger["fingerprint"] == False:
					pass
				else:
					self.fingerprints = finger["fingerprint"]
					# self.id_device = device
					break
				print("-"*40)
	def before_insert(self):
		employees = frappe.db.get_list("PIO ID", pluck="employee")
		exists_employee = frappe.db.exists({"doctype": "PIO ID", "id_employee_in_device": self.id_employee_in_device})
  
		if self.employee in employees:
			frappe.throw(f"Employee {self.full_name} already exists")
		if exists_employee:
			frappe.throw(f"The Employee {exists_employee} has ID {self.id_employee_in_device} already")
			
def connect_zk(employee_id,id_device):
	conn = None
	print(id_device)
	zk = ZK(id_device)
	try:
		print("connecting to device")
		conn = zk.connect()
		conn.disable_device()

		template = conn.get_user_template(uid=int(employee_id), temp_id=6)

		if template.template == b'':
			print(f"ID {employee_id} has no fingerprint")
			conn.test_voice()
			conn.enable_device()
			return {"fingerprint": False, "message": f"ID {employee_id} has no fingerprint"}
		else:
			print(f"ID {employee_id} has fingerprint")
			finger = Finger(uid=template.uid, fid=template.fid,valid=template.valid, template=template.template)
			finger_json = finger.json_pack()
			conn.test_voice()
			conn.enable_device()
			return {"fingerprint": finger_json, "message": f"ID {employee_id} has fingerprint"}

	except Exception as e:
		return {"fingerprint": False, "message": f"Error: {e}"}