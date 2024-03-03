import frappe
from frappe import _
from frappe.model.document import Document
from zk import ZK,const
from  zk.finger import Finger
from  zk.user import User
import json
from datetime import datetime

class BioID(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF
		from my_hrms.my_hrms.doctype.devices_table.devices_table import DevicesTable
		from my_hrms.my_hrms.doctype.templates_table.templates_table import Templatestable

		employee: DF.Link
		fingerprint_devices: DF.Table[DevicesTable]
		fingerprints: DF.Data | None
		fingerprints_template: DF.JSON | None
		full_name: DF.Data | None
		id_employee_in_device: DF.Data
		image: DF.AttachImage | None
		photo: DF.Data | None
		templates_table: DF.Table[Templatestable]
	# end: auto-generated types
	def validate(self):
		pass

@frappe.whitelist()
def receive_finger_template(employee , zk_device, finger_index):
	employee = frappe.get_doc('Employee',employee)
	zk_device = frappe.get_doc('ZK Device', zk_device)
	bioid = frappe.get_doc("BioID" , employee.employee_name)
	
	# information Employee
	employee_id = employee.attendance_device_id
	employee_name = employee.employee_name
	# information Device ZK
	device_name = zk_device.device_name
	device_ip = zk_device.device_ip
	
 
	conn = None
	zk = ZK(device_ip)
	try:
		print("connecting to device")
		conn = zk.connect()
		conn.disable_device()

		time_today = datetime.today()
		conn.set_time(time_today)
		# conn.test_voice()

		conn.set_user(uid=int(employee_id), name=employee_name,user_id=str(employee_id))
		conn.delete_user_template(uid=int(employee_id),temp_id=int(finger_index))
		conn.enroll_user(uid=int(employee_id),temp_id=int(finger_index),user_id=str(employee_id))

		template = conn.get_user_template(uid=int(employee_id), temp_id=int(finger_index))
		enroll_finger = bool(template) == False or template.template == b''
		if enroll_finger:
			conn.enable_device()
			return {"status": False,"color":"red", "message": f"The fingerprint was not captured"}
		else:
			template = conn.get_user_template(uid=int(employee_id), temp_id=int(finger_index))
			finger_json = template.json_pack()
			is_finger_existing = False
			for finger in bioid.templates_table:
				if str(finger_json['fid']) == str(finger.fid):
					is_finger_existing = True
					finger.size = finger_json['size']
					finger.template = finger_json['template']
					bioid.save()
					break
			if is_finger_existing == False:
				bioid.append("templates_table",finger_json)
				bioid.save()
			conn.enable_device()
			return {"status": True,"color":"green", "fingerprints_template":finger_json ,"message": _(f"The fingerprint of employee {employee_name} was successfully registered")}
	except Exception as e:
			return {"status": False,"color": "red", "message" : _(f"Error in {device_name} the Error => {e}")}
