document
  .querySelector(".password")
  ?.addEventListener("click", function (event) {
    window
      .getSelection()
      .selectAllChildren(document.getElementById("password"));
    navigator.clipboard.writeText(window.getSelection().toString());
  });
