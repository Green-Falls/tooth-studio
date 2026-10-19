// Writes the booking text from the form on book.html. Nothing leaves the page:
// the message only goes anywhere when the visitor sends it from Messages or email.
(function () {
  var form = document.getElementById("book-form");
  if (!form) return;

  var PHONE = "+12075996459";
  var EMAIL = "toothstudiomaine@gmail.com";
  var message = document.getElementById("message");
  var sms = document.getElementById("send-sms");
  var email = document.getElementById("send-email");
  var copy = document.getElementById("copy");
  var status = document.getElementById("status");
  var out = {};
  document.querySelectorAll("[data-out]").forEach(function (el) { out[el.dataset.out] = el; });

  var INSURANCE = {
    delta: "Delta Dental",
    martins: "Martin's Point through Delta Dental",
    mainecare: "MaineCare",
    medicare: "Medicare",
    other: "another plan",
    none: "no insurance"
  };
  var WHO_CARD = { me: "You", child: "Your child", family: "More than one of you", facility: "Someone in a care facility" };
  var WHO_TEXT = { me: "", child: " for my child", family: " for more than one person in my family", facility: " for a family member in a care facility" };

  function values(name) {
    return Array.prototype.map.call(form.querySelectorAll('[name="' + name + '"]:checked'), function (el) { return el.value; });
  }

  function list(items) {
    if (items.length < 2) return items.join("");
    return items.slice(0, -1).join(", ") + " or " + items[items.length - 1];
  }

  function update() {
    var f = form.elements;
    var name = f["name"].value.trim();
    var who = values("who")[0] || "me";
    var returning = values("returning")[0] === "yes";
    var what = values("what");
    var ins = f["insurance"].value;
    var days = values("day");
    var times = values("time");
    var note = f["note"].value.trim();
    var we = who === "me" ? "I" : "we";
    var We = who === "me" ? "I" : "We";

    var visit;
    if (what.indexOf("cleaning") > -1 && what.indexOf("whitening") > -1) visit = "a cleaning and whitening";
    else if (what.indexOf("whitening") > -1) visit = "whitening";
    else if (what.indexOf("cleaning") > -1) visit = "a cleaning";
    else visit = "an appointment";

    var parts = [];
    parts.push("Hi Rytel, " + (name ? "this is " + name + ". " : "") + "I'd like to book " + visit + WHO_TEXT[who] + ".");
    if (what.indexOf("unsure") > -1) parts.push((what.length > 1 ? "I'm also" : "I'm") + " not sure yet what " + we + " need.");
    if (who === "me") parts.push(returning ? "I've been to the studio before." : "I'm a new patient.");
    else parts.push(returning ? "We've been to the studio before." : "We're new patients.");

    if (ins === "none") parts.push(We + " don't have insurance and would pay " + (who === "me" ? "myself" : "ourselves") + ". Could you tell me about the membership plan?");
    else if (ins === "other" || ins === "medicare") parts.push(We + " have " + INSURANCE[ins] + ". Can you check if it's covered? I can send the plan name.");
    else parts.push(We + " have " + INSURANCE[ins] + ".");

    if (days.length) {
      var timeText = times.length === 1 ? ", in the " + times[0] : times.length === 2 ? ", morning or afternoon" : "";
      parts.push(list(days.map(function (d) { return d + "s"; })) + " work best" + timeText + ".");
    } else if (times.length) {
      parts.push(list(times.map(function (t) { return t.charAt(0).toUpperCase() + t.slice(1) + "s"; })).replace(" or A", " or a") + " work best.");
    }
    if (note) parts.push(note);
    parts.push("Thank you!");

    var text = parts.join(" ");
    message.textContent = text;

    out.who.textContent = name ? name + (who === "me" ? "" : ", " + WHO_CARD[who].toLowerCase()) : WHO_CARD[who];
    out.what.textContent = visit.replace(/^an? /, "").replace(/^./, function (c) { return c.toUpperCase(); }) + (returning ? ", returning" : ", new patient");
    out.insurance.textContent = ins === "other" ? "Another plan" : ins === "none" ? "Self-pay" : INSURANCE[ins];
    out.when.textContent = days.length || times.length
      ? (days.length ? days.map(function (d) { return d.slice(0, 3); }).join(", ") : "Any day") + (times.length ? ", " + times.join(" or ") : "")
      : "Any time";

    var body = encodeURIComponent(text);
    sms.href = "sms:" + PHONE + "?&body=" + body;
    email.href = "mailto:" + EMAIL + "?subject=" + encodeURIComponent("Appointment request") + "&body=" + body;
  }

  if (navigator.clipboard) {
    copy.hidden = false;
    copy.addEventListener("click", function () {
      navigator.clipboard.writeText(message.textContent).then(function () {
        status.textContent = "Copied. Paste it into a text to (207) 599-6459.";
      }, function () {
        status.textContent = "Couldn't copy. Select the message above and copy it.";
      });
    });
  }

  form.addEventListener("input", update);
  form.addEventListener("change", update);
  form.addEventListener("submit", function (e) { e.preventDefault(); });
  update();
})();
