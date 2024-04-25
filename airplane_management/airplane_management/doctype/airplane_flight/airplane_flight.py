# Copyright (c) 2024, samiksha mohekar and contributors
# For license information, please see license.txt

import frappe
from frappe.website.website_generator import WebsiteGenerator
from frappe.model.document import Document
from frappe import _ 

class AirplaneFlight(WebsiteGenerator):
    def on_submit(self):
        self.db_set("status","Completed")
        
        airplane_flight = frappe.get_doc("Airplane Flight",self.name)
        
        if airplane_flight:
            airplane_flight.db_set("status","Completed")
        else:
            frappe.throw("Error: Airplane Flight document not found")