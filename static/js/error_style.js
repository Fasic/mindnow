export default function addStyle(item) {
    var element = document.getElementById(item);
    element.classList.add("form-control-danger");
    element.classList.add("is-invalid");
    element.parentElement.classList.add("has-danger");
}