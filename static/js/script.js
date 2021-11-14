let alertWrapper = document.querySelector(".alert");
let alertClose = document.querySelector(".alert__close");

if (alertWrapper) {
  console.log("click action is performed");
  alertClose.addEventListener(
    "click",
    () => (alertWrapper.style.display = "none")
  );
}