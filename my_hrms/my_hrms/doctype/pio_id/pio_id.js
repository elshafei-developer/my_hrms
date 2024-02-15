// Copyright (c) 2024, hassan hussein mohammed and contributors
// For license information, please see license.txt
let dialogOpened = false;
frappe.ui.form.on("PIO ID", {
  taking_a_fingerprint: function (frm) {
    if (!dialogOpened) {
      frm.fields_dict.taking_a_fingerprint.$input.on("click", function () {
        let employee = frm.fields_dict.employee.get_value();
        let name_employee = frm.fields_dict.full_name.get_value();
        let id_employee = frm.fields_dict.id_employee_in_device.get_value();
        let zk_device = frm.fields_dict.zk_device.get_value();
        let has_finger = frm.fields_dict.has_fingerprint.get_value();
        let id_device = frm.fields_dict.id_device.get_value();

        if (employee && id_employee && name_employee && zk_device) {
          showLoadingIndicator(frm);
          dialogOpened = true;
          frappe.call({
            method: "my_hrms.my_hrms.doctype.pio_id.pio_id.get_fingerprint",
            args: {
              data: {
                employee,
                name_employee,
                id_employee,
                id_device,
                has_finger,
              },
            },
            callback: function (data) {
              hideLoadingIndicator();
              if (data) {
                if (data.message.fingerprint == false) {
                  frappe.msgprint(data.message.message);
                } else {
                  frm.set_value(
                    "finger_template",
                    data.message.fingerprint.template
                  );
                  frm.set_value("finger_size", data.message.fingerprint.size);
                  frappe.msgprint(data.message.message);
                }
                dialogOpened = false;
              }
            },
          });
        } else {
          frappe.throw(__("Please fill all the required fields"));
          dialogOpened = false;
        }

        console.log("clicked");
      });
    }
  },
  // refresh: function (frm) {},
});

function showLoadingIndicator() {
  let loadingIndicator = $('<div id="loading-indicator">Loading...</div>');

  loadingIndicator.css({
    position: "fixed",
    top: 0,
    left: 0,
    width: "100%",
    height: "100%",
    background: "rgba(255, 255, 255, 0.8)",
    zIndex: 9999,
    textAlign: "center",
    paddingTop: "20%",
    fontSize: "24px",
  });

  $(document.body).append(loadingIndicator);
}

function hideLoadingIndicator() {
  $("#loading-indicator").remove();
}
