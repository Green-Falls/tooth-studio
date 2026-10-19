// Appointment request form on contact.html.
// Validates name and phone (and email if given), then posts to the form service
// set as FORM_ENDPOINT in build.py (Formspree-style: JSON in, {ok:true} out).
// With no endpoint configured it says so instead of pretending to send.
(function () {
  var form = document.getElementById("request-form");
  if (!form) return;
  var status = document.getElementById("form-status");
  var sent = document.getElementById("sent");
  var button = form.querySelector(".submit");

  var RULES = {
    name: function (v) { return v.trim() ? "" : "Enter your name."; },
    phone: function (v) {
      var digits = v.replace(/\D/g, "");
      if (!digits) return "Enter a phone number so Rytel can reach you.";
      return digits.length >= 10 ? "" : "Enter the full number, including area code.";
    },
    email: function (v) {
      if (!v.trim()) return "";
      return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(v.trim()) ? "" : "Check the email address, or leave it blank.";
    }
  };

  function check(input) {
    var rule = RULES[input.name];
    if (!rule) return true;
    var message = rule(input.value);
    var error = document.getElementById("e-" + input.name);
    input.setAttribute("aria-invalid", message ? "true" : "false");
    input.closest(".field").classList.toggle("invalid", !!message);
    if (error) error.textContent = message;
    return !message;
  }

  Object.keys(RULES).forEach(function (name) {
    var input = form.elements[name];
    input.addEventListener("blur", function () { if (input.value) check(input); });
    input.addEventListener("input", function () { if (input.getAttribute("aria-invalid") === "true") check(input); });
  });

  // Email becomes required when someone asks for a reply by email.
  form.addEventListener("change", function (e) {
    if (e.target.name !== "reply_by") return;
    var email = form.elements.email;
    var label = form.querySelector('label[for="f-email"] .optional');
    var needEmail = e.target.value === "Email";
    RULES.email = needEmail
      ? function (v) { return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(v.trim()) ? "" : "Enter your email so Rytel can reply."; }
      : function (v) { return !v.trim() || /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(v.trim()) ? "" : "Check the email address, or leave it blank."; };
    if (label) label.hidden = needEmail;
    if (email.getAttribute("aria-invalid") === "true") check(email);
  });

  function setBusy(busy) {
    button.disabled = busy;
    button.textContent = busy ? "Sending…" : "Send request";
  }

  form.addEventListener("submit", function (e) {
    e.preventDefault();
    status.textContent = "";
    status.classList.remove("bad");
    var firstBad = null;
    ["name", "phone", "email"].forEach(function (name) {
      var input = form.elements[name];
      if (!check(input) && !firstBad) firstBad = input;
    });
    if (firstBad) { firstBad.focus(); return; }
    if (form.elements._gotcha.value) return;

    var endpoint = form.getAttribute("action");
    if (!endpoint) {
      status.classList.add("bad");
      status.textContent = "This form isn't connected yet, so nothing was sent. Please call or text (207) 599-6459.";
      return;
    }

    var data = {};
    new FormData(form).forEach(function (value, key) { data[key] = value; });
    data._subject = "Visit request: " + data.reason;
    setBusy(true);
    fetch(endpoint, {
      method: "POST",
      headers: { "Content-Type": "application/json", "Accept": "application/json" },
      body: JSON.stringify(data)
    }).then(function (res) {
      if (!res.ok) throw new Error(res.status);
      var first = data.name.trim().split(/\s+/)[0];
      sent.querySelector("[data-sent-name]").textContent = first ? ", " + first : "";
      sent.querySelector("[data-sent-reply]").textContent = data.reply_by === "Call" ? "phone" : data.reply_by.toLowerCase();
      sent.querySelector("[data-sent-phone]").textContent = data.reply_by === "Email" ? data.email : data.phone;
      form.hidden = true;
      sent.hidden = false;
      sent.focus();
    }).catch(function () {
      setBusy(false);
      status.classList.add("bad");
      status.textContent = "Your request didn't go through. Try again, or call or text (207) 599-6459.";
    });
  });
})();
