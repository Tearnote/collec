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

const showAddModal = async function(e) {
    const button = e.currentTarget;
    const href = button.getAttribute("data-href-template");
    const response = await fetch(href);
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

const showModal = async function(e) {
    e.preventDefault();
    const anchor = e.currentTarget;
    const href = anchor.getAttribute("href");
    const response = await fetch(href);
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

const itemDelete = function(e) {
    if (!confirm("Are you sure you want to delete the item? This cannot be undone."))
        e.preventDefault();
}
