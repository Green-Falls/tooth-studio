// Loads the Google map only when the visitor asks, so the contact page makes no
// request to Google on arrival.
(function () {
  var button = document.getElementById("load-map");
  if (!button) return;
  button.addEventListener("click", function () {
    var box = document.getElementById("map");
    var frame = document.createElement("iframe");
    frame.src = button.dataset.src;
    frame.title = "Map of 55 Main Street, Bridgton, Maine";
    frame.referrerPolicy = "no-referrer-when-downgrade";
    box.textContent = "";
    box.classList.add("loaded");
    box.appendChild(frame);
    frame.focus();
  });
})();
