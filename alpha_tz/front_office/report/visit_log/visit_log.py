# Copyright (c) 2022, KodeIT and contributors
# For license information, please see license.txt

import frappe
from frappe import _


def execute(filters=None):
	if not filters:
		filters = {}

	columns = get_column()
	data=[]

	report_items = get_data(filters)
	for d in report_items:
		row = {}
		
		row['visit_date'] = d.visit_date		
		row['visitor_name'] = d.visitor_name
		row["employee_name"] = d.employee_name
		row['purpose'] = d.purpose
		row['branch'] = d.branch

		
		row['time_in'] = d.time_in
		row['time_out'] = d.time_out
		
		#row['balance'] = d.balance	


		data.append(row)

	return columns, data


def get_column():
	return [
		{
			"fieldname":"visit_date",
			"label": "Tarehe",
			"fieldtype": "Date",
			'width': 150
		},
		{
			"fieldname":"visitor_name",
			"label": "visitor  ",
			"fieldtype": "Data",
			'width': 150
		},
		{
			"fieldname":"purpose",
			"label": "Purpose",
			"fieldtype": "Data",
			"width": 120,
		},
		{
			"fieldname":"employee_name",
			"label": "Meeting With  ",
			"fieldtype": "Data",
			'width': 150
		},
		{
			"fieldname":"branch",
			"label": "Branch",
			"fieldtype": "Data",
			'width': 150
		},		
		{
			"fieldname":"time_in",
			"label": "Time In",
			"fieldtype": "Time",
			'width': 150
		},
		{
			"fieldname":"time_out",
			"label": "Time Out",
			"fieldtype": "Time",
			'width': 150
		},

	
	]


def get_data(filters):
	where_filter = {"from_date": filters.from_date, "to_date": filters.to_date}
	where = ""

	data = frappe.db.sql("""select tv.visit_date, tv.visitor_name,
		tv.purpose, tv.employee_name, tv.time_in, tv.time_out, tv.branch
		
		from `tabVisit` tv
		where tv.docstatus !=2
		order by tv.visit_date ASC
		"""+ where, where_filter, as_dict=1)
	return data
