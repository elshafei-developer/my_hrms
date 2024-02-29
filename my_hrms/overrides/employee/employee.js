frappe.ui.form.on("Employee", {
  refresh(frm) {
    frm.add_custom_button(
      __("Receive Finger Template"),
      function () {
        const dialog = new frappe.ui.Dialog({
          title: "Enter Details",
          fields: [
            {
              label: "Employee Name",
              fieldname: "employee_name",
              fieldtype: "Data",
              default: frm.doc.employee_name,
              read_only: 1,
            },
            {
              label: "ZK Device",
              fieldname: "zk_device",
              fieldtype: "Link",
              options: "ZK Device",
            },
            {
              label: "Finger Index",
              fieldname: "finger_index",
              fieldtype: "Select",
              options: "0\n1\n2\n3\n4\n5\n6\n7\n8\n9",
              default: "6",
            },
            {
              label: "Attendance Device ID",
              fieldname: "attendance_device_id",
              fieldtype: "Data",
              default: frm.doc.attendance_device_id,
              read_only: 1,
              hidden: 1,
            },
          ],
          primary_action_label: "Submit",
          primary_action(values) {
            console.log("values", values);
            dialog.hide();
            frappe.call({
              method:
                "my_hrms.my_hrms.my_hrms.overrides.employee.employee.receive_finger_template",
              args: values,
              callback: function (response) {
                // Handle response
                frappe.msgprint(__("Response: " + response.message));
              },
            });
          },
        });

        dialog.show();
      },
      __("Action")
    );
  },
});
