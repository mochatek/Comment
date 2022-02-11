document.getElementById("filter_button").addEventListener("click", (event) => {
  const filter =
    document.getElementById("filter_button").innerText === " Filter Mine"
      ? "mine"
      : "others";
  window.location.assign(`${window.location.origin}?comment_filter=${filter}`);
});
