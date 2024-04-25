# Copyright (c) 2024, samiksha mohekar and contributors
# For license information, please see license.txt

# import frappe


# def execute(filters=None):
# 	columns, data = [], []
# 	return columns, data

import frappe

def get_columns():
    return [
        {
            "label": "Airline",
            "fieldname": "airline",
            "fieldtype": "Link",
            "options":"Airline",
            "width": 200
        },
        {
            "label": "Revenue",
            "fieldname": "revenue",
            "fieldtype": "Currency",
            "width": 200
        }
    ]

def execute(filters=None):
    columns = get_columns()
    data = get_data(filters)
    total_revenue = sum(d[1] for d in data)
    data_list = [list(row) for row in data]
    total_row = ["Total", total_revenue]
    chart = get_chart(data_list, total_revenue)

    report_summary = [{
        "value": total_revenue,
        "indicator": "Green" if total_revenue > 0 else "Red",
        "label": "Total Revenue",
        "datatype": "Currency",
        "currency": "INR"
    }]
    # data_list.append(total_row)
    return columns, data_list, total_revenue, chart, report_summary

def get_data(filters):
    data = frappe.db.sql("""
        SELECT
            COALESCE(airline.name, 'Other') as airline,
            SUM(IFNULL(ticket.total_amount, 0)) as revenue
        FROM
            (SELECT name FROM `tabAirline`) as airline
        LEFT JOIN
            `tabAirplane Ticket` as ticket
        ON
            airline.name = SUBSTRING_INDEX(ticket.flight, '-', 1)
        GROUP BY
            airline
        ORDER BY
            revenue DESC;
        """)
    return data

def get_chart(data, total_revenue):
    chart = {
        "data": {
            "labels": [d[0] for d in data[:-1]], 
            "datasets": [
                {
                    "name": "Revenue",
                    "values": [d[1] for d in data[:-1]]  
                }
            ]
        },
        "type": "donut",
        "center": {
            "text": "Total Revenue",
            "subtext": frappe.format_value(total_revenue, dict(fieldtype='Currency')),
            "style": {
                "fill": "green",
                "font-size": "14px",
                "font-weight": "bold"
            }
        }
    }
    
    return chart
