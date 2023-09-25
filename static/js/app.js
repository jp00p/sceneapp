const slider_values = ["Not interested", "Curious", "Would like to try", "Would enjoy", "Please do this"]


function update_slider_value(elem, key) {
  console.log(elem, key)
  elem.innerHTML = slider_values[key];
}

function toggle_notes(parent) {
  if (parent.classList.contains("active")) {
    parent.classList.remove("active");
  } else {
    parent.classList.add("active");
  }
}

document.addEventListener("DOMContentLoaded", function () {

  document.querySelectorAll(".range-slider").forEach(function (e) {
    let parent = e.parentElement;
    parent.classList.add("slider-wrapper")
    let label = document.createElement("div")
    label.classList.add("slider-label")
    label.innerHTML = slider_values[e.value];
    if (e.value == 0) {
      parent.classList.add("disabled");
    } else {
      parent.classList.remove("disabled");
    }

    e.addEventListener("input", function () {
      console.log(e.value)
      label.innerHTML = slider_values[e.value];
      if (e.value == 0) {
        parent.classList.add("disabled");
      } else {
        parent.classList.remove("disabled");
      }
      if (e.value == 4) {
        parent.classList.add("enthusiastic");
      } else {
        parent.classList.remove("enthusiastic");
      }
    });

    parent.appendChild(label);
  });


  document.querySelectorAll(".kink-notes").forEach(function (e) {
    let parent = e.parentElement;
    parent.classList.add("kink-notes-wrap")
    let note_icon = document.createElement('i')
    note_icon.classList.add("fa-solid", "fa-note-sticky", "note-icon")
    let close_icon = document.createElement('i')
    close_icon.classList.add("fa-solid", "fa-times", "close-icon")
    parent.appendChild(note_icon)
    parent.appendChild(close_icon)
    note_icon.addEventListener("click", function () {
      toggle_notes(parent);
    });
    close_icon.addEventListener("click", function () {
      toggle_notes(parent);
    });
  });

});
