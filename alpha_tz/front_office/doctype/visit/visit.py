# Copyright (c) 2022, KodeIT and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Visit(Document):

	def before_submit(self):
		if self.state == "Check-In":
			frappe.throw("Checkout Visitor first then submit")

