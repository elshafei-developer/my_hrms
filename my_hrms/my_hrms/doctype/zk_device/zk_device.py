# Copyright (c) 2024, hassan hussein mohammed and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class ZKDevice(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		bioid: DF.Link | None
		data: DF.Data | None
		device_ip: DF.Data
		device_location: DF.Link
		device_name: DF.Data
		time: DF.Data | None
	# end: auto-generated types
	pass
