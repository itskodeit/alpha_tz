# Copyright (c) 2022, KodeIT and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Visitor(Document):
	def before_save(self):
		set_visitor_name(self)


@frappe.whitelist(allow_guest=True)	
def set_visitor_name(self):
	self.visitor_name = " ".join(
		filter(lambda x: x, [self.visitor_first_name, self.visitor_middle_name, self.visitor_last_name])
	)

