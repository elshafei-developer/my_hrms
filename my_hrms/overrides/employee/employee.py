import frappe
from frappe import _
from erpnext.setup.doctype.employee.employee import Employee

class CustomEmployee(Employee):
   def validate(self):
      pass
   def on_update(self):
      attendance_device_id = self.attendance_device_id
      
   
   
def receive_finger_template(data):
   return "Finger template received"