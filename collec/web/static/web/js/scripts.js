const submitForm = function(e) {
    const el = e.currentTarget;
    const form = el.form;
    form.submit();
}

const resetForm = function(e) {
    e.preventDefault();
    const el = e.currentTarget;
    const form = el.form;
    const search = form.elements["q"];
    search.value = "";
    form.submit();
}

const showAddModal = async function() {
    const response = await fetch(window.location.href + "add/");
    const html = await response.text();
    const el = document.createElement("div");
    el.innerHTML = html;
    document.body.append(el);
    const modal = new bootstrap.Modal(el.firstElementChild);
    modal.show();
    el.addEventListener("hidden.bs.modal", function() {
        el.remove();
    })
}
