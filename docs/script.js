// set folder name click callback
let elms = document.querySelectorAll(".d");
elms.forEach((elm) => {
  elm.addEventListener("click", () =>{
    let childclass;
    elm.classList.forEach((c) => {
      if (c.startsWith("p")) {
        childclass = ".c" + c.replace("p", "");
      };
    });
    let child = document.querySelectorAll(childclass);
    let oldmode, newmode;
    if (child[0].classList.contains("s")) {
      oldmode = "s";
      newmode = "h";
      child.forEach((c) => {
        c.classList.remove(oldmode);
        c.classList.add(newmode);
      });
    } else {
      oldmode = "h";
      newmode = "s";
      let level;
      child[0].classList.forEach((c) => {
        if (c.startsWith("l")) {
          level = c;
        };
      });
      child.forEach((c) => {
        if (c.classList.contains(level)) {
          c.classList.remove(oldmode);
          c.classList.add(newmode);
        };
      });
    }
  });
});

// set search callback
let search = document.querySelector("#search");
search.addEventListener("change", () => {
  collapseAll();
  let regex = new RegExp(search.value, "i");
  if (search.value.length == 0) {
    return;
  }

  let items = document.querySelectorAll("tr");
  items.forEach((tr) => {
    if (tr.classList.contains("h") || tr.classList.contains("s")) {
      if (regex.test(tr.innerText)) {
        tr.classList.remove("h");
        tr.classList.add("s");
      } else {
        tr.classList.remove("s");
        tr.classList.add("h");
      }
    }
  });
});

function collapseAll() {
  let items = document.querySelectorAll("tr");
  items.forEach((tr) => {
    if (tr.classList.contains("h") || tr.classList.contains("s")) {
      tr.classList.remove("s");
      tr.classList.add("h");
    }
  });
}

// set collapse all callback
let collapse_button = document.querySelector("#collapse");
collapse_button.addEventListener("click", () => { collapseAll(); });

// set expand all callback
let expand_button = document.querySelector("#expand");
expand_button.addEventListener("click", () => {
  let items = document.querySelectorAll("tr");
  items.forEach((tr) => {
    if (tr.classList.contains("h") || tr.classList.contains("s")) {
      tr.classList.remove("h");
      tr.classList.add("s");
    }
  });
});


// set number of items
let num_sel = document.querySelector("#cnt_selection_value").getAttribute("value");
let num_ful = document.querySelector("#cnt_full_value").getAttribute("value");
console.log(num_sel);
document.querySelector("#cnt_selection").innerText = "(" + num_sel + " items)";
document.querySelector("#cnt_full").innerText = "(" + num_ful + " items)";

