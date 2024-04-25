// Copyright (c) 2024, samiksha mohekar and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Airplane Ticket", {
// 	refresh(frm) {
//         frm.page.add_inner_button(__('Assign Seat'), function() {
//             frappe.prompt([
//                 {
//                     fieldname: 'seat_number',
//                     fieldtype: 'Data',
//                     label: __('Seat Number'),
//                     reqd: 1
//                 }
//             ], function(values){
//                 frm.set_value('seat', values.seat_number);
//             }, __('Select Seat'), __('Assign'));
//         }, __("Action"), "btn-primary");


// 	},
// });

frappe.ui.form.on("Airplane Ticket", {
    refresh(frm) {
        frm.add_custom_button(__('Assign Seat'), function() {
            frappe.prompt([
                {
                    fieldname: 'seat_number',
                    fieldtype: 'Data',
                    label: __('Seat Number'),
                    reqd: 1
                }
            ], function(values){
                frm.set_value('seat', values.seat_number);
            }, __('Select Seat'), __('Assign'));
        }, __("Action"));
    },
});

