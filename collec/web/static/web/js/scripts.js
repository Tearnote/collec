const resetForm = function(e) {
    e.preventDefault();
    const el = e.currentTarget;
    const form = el.form;
    const search = form.elements["q"];
    search.value = "";
    form.submit();
}
