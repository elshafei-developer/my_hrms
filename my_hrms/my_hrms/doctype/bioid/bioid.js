// Copyright (c) 2024, hassan hussein mohammed and contributors
// For license information, please see license.txt

let dialogOpened = false;
frappe.ui.form.on("BioID", {
  refresh: function (frm) {
    if (!frm.is_new()) {
      let fields = [
        {
          label: "Employee Name",
          fieldname: "employee_name",
          fieldtype: "Data",
          default: frm.doc.full_name,
          read_only: 1,
        },
        {
          label: "ZK Device",
          fieldname: "zk_device",
          fieldtype: "Link",
          options: "ZK Device",
          reqd: 1,
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
          fieldname: "employee_id",
          fieldtype: "Data",
          default: frm.doc.id_employee_in_device,
          read_only: 1,
          hidden: 1,
        },
        {
          label: "Fingerprints Template",
          fieldname: "fingerprints_template",
          fieldtype: "JSON",
          hidden: 1,
        },
        {
          label: "Test",
          fieldname: "test",
          fieldtype: "Data",
          hidden: 1,
        },
      ];
      frm.add_custom_button(
        __("Receive Finger Template"),
        function () {
          const dialog = new frappe.ui.Dialog({
            title: __("Enter Details"),
            fields: fields,
            primary_action_label: "get fingerprint",
            primary_action(data) {
              dialog.set_value("test", "test");
              frappe.call({
                method:
                  "my_hrms.my_hrms.doctype.bioid.bioid.receive_finger_template",
                args: {
                  data: data,
                },
                freeze_message: __("Receiving Finger Template..."),
                async: true,
                freeze: true,
                callback: function (r) {
                  frappe.show_alert(
                    {
                      message: __("get  fingerprint template successfully"),
                      indicator: "red",
                    },
                    5
                  );
                },
                always: function () {
                  dialog.get_field("test").df.hidden = 0;
                  dialog.fields_dict.test.refresh();
                },

                error: function (e) {
                  console.log(e);
                },
              });
            },
          });

          dialog.show();
        },
        __("Action")
      );
    }
  },
});
