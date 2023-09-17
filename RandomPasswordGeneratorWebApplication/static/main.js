function copyPassword(password) {
    var takeinput = document.createElement("input");
    takeinput.value = password;
    document.body.appendChild(takeinput);
    takeinput.select();
    document.execCommand("copy");
    document.body.removeChild(takeinput);
}
