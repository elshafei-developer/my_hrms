# Copyright (c) 2024, hassan hussein mohammed and contributors
# For license information, please see license.txt

import frappe
from frappe import _
from zk import ZK
from frappe.model.document import Document


class PIOID(Document):
	def validate(self):
		if self.id_employee_in_device:
			self.fingerprints = self.id_employee_in_device
	def before_insert(self):
		employees = frappe.db.get_list("PIO ID", pluck="employee")
		exists_employee = frappe.db.exists({"doctype": "PIO ID", "id_employee_in_device": self.id_employee_in_device})
  
		if self.employee in employees:
			frappe.throw(f"Employee {self.full_name} already exists")
		if exists_employee:
			frappe.throw(f"The Employee {exists_employee} has ID {self.id_employee_in_device} already")
			
def connect_zk(employee_id,device):
	conn = None
	zk = ZK(device['id_device'])
	try:
		conn = zk.connect()
		conn.disable_device()
		users = conn.get_users()
		for user in users:
			if(user.user_id == employee_id):
				return True
		conn.test_voice()
		conn.enable_device()
	except Exception as e:
		# return False
		pass

# def send_data_to_js(data):
# 	# Publish data to the specified channel
# 	frappe.publish_realtime('my_custom_channel', data)
 
# @frappe.whitelist()
# def move_to_custom_doctype(name,ID):
#     return {"message": f"The Employee {name} has ID {ID} Do you want update information this Employee ?"}