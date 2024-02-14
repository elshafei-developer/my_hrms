// Copyright (c) 2024, hassan hussein mohammed and contributors
// For license information, please see license.txt

frappe.ui.form.on("PIO ID", {
  refresh(frm) {},
  before_save(frm) {},
});
frappe.realtime.on("my_custom_channel", function (data) {
  frappe.confirm(
    "The ID is already in use, do you want to update the information ?",
    () => {
      // action to perform if Yes is selected
    },
    () => {
      // action to perform if No is selected
    }
  );
});
