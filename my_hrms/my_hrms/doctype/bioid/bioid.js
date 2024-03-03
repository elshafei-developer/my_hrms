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
      ];
      frm.add_custom_button(
        __("Receive Finger Template"),
        function () {
          const dialog = new frappe.ui.Dialog({
            title: __("Enter Details"),
            fields: fields,
            primary_action_label: "get fingerprint",
            primary_action(data) {
              frappe.call({
                method:
                  "my_hrms.my_hrms.doctype.bioid.bioid.receive_finger_template",
                args: {
                  employee: frm.doc.employee,
                  zk_device: data.zk_device,
                  finger_index: data.finger_index,
                },
                freeze_message: __("Receiving Finger Template..."),
                freeze: true,
                async: true,
                callback: function (r) {
                  console.log(r.message.message);
                  if (r.message.status == true) {
                    dialog.hide();
                  }
                  frappe.show_alert(
                    {
                      message: __(`${r.message.message}`),
                      indicator: r.message.color,
                    },
                    7
                  );
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
