form = new FormData();
form.append("file", myFile);
let response = await fetch('/uploadfile/', {
    method: 'POST',
    body: form
    });

    let result = await response.json();