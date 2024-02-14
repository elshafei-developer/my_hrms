# Copyright (c) 2024, hassan hussein mohammed and contributors
# For license information, please see license.txt

import frappe
from zk import ZK, const
from frappe.model.document import Document


class PIOID(Document):
	def validate(self):
     
		devices_ZK = frappe.db.get_list("ZK Device", fields=["location_device","id_device"])
		for device in devices_ZK:
			print("#"*40)
			print("-"*40)
			print(f"ID: {id}")
			if(connect_zk(self.id_employee_in_device,device)):
				frappe.throw(f"User ID found in device {device['location_device']} please choose another ID")
			# connect_zk(self.id_employee_in_device,device)
			print("-"*40)
			print("#"*40)
  
  
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
		# frappe.msgprint(f"Error:")
		pass