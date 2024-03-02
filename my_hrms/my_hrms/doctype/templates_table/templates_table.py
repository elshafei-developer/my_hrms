# Copyright (c) 2024, hassan hussein mohammed and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Templatestable(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		fid: DF.Data | None
		parent: DF.Data
		parentfield: DF.Data
		parenttype: DF.Data
		size: DF.Data | None
		template: DF.LongText | None
		uid: DF.Data | None
		valid: DF.Data | None
	# end: auto-generated types
	pass
