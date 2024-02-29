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

		employee: DF.Link
		fingerprint_devices: DF.Table[DevicesTable]
		fingerprints: DF.Data | None
		fingerprints_template: DF.JSON | None
		full_name: DF.Data | None
		id_employee_in_device: DF.Data
		image: DF.AttachImage | None
		photo: DF.Data | None
	# end: auto-generated types
	def validate(self):
		pass

@frappe.whitelist()
def receive_finger_template(data):
	data_json = json.loads(data)
	employee_id = data_json['employee_id']
	employee_name = data_json['employee_name']
	zk_name = data_json['zk_device']
	finger_index = data_json['finger_index']
	zk_devices_ip = frappe.db.get_value("ZK Device", zk_name ,"device_ip")

	conn = None
	zk = ZK(zk_devices_ip)
	try:
		print("connecting to device")
		conn = zk.connect()
		conn.disable_device()
		time_today = datetime.today()
		conn.set_time(time_today)
		conn.test_voice()
		conn.set_user(uid=int(employee_id), name=employee_name,user_id=str(employee_id))
		conn.delete_user_template(uid=int(employee_id),temp_id=int(finger_index))
		conn.enroll_user(uid=int(employee_id),temp_id=int(finger_index),user_id=str(employee_id))	
		template = conn.get_user_template(uid=int(employee_id), temp_id=int(finger_index))
		enroll_finger = bool(template) == False or template.template == b''
		if enroll_finger:
			conn.enable_device()
			return {"status": False, "message": f"The fingerprint was not captured"}
		else:
			template = conn.get_user_template(uid=int(employee_id), temp_id=int(finger_index))
			finger_json = template.json_pack()
			conn.enable_device()
			return {"status": True, "fingerprints_template":finger_json ,"message": f"Add {employee_name} successful, With Finger Index {finger_index}"}
	except Exception as e:
			return {"status": False, "message": f"Error => {zk_name} Device {e}"}
