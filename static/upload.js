const body = document.querySelector('body');
const upload = document.querySelector('.upload');

var fileInput = document.getElementById('myForm').elements['file'];
var submitButton = document.getElementById('myForm').elements['submit'];
var fileName = document.getElementById('fileName');


function preventDefaults (e) {
  e.preventDefault()
  e.stopPropagation()
}


/* ------------------------------
Disable the upload button if no file has been selected and update the name of the uploaded file
------------------------------ */
function validateForm() {
  if (fileInput.value === '') {
      submitButton.disabled = true;
  } else {
      submitButton.disabled = false;
  }

  if (fileInput.files.length > 0) {
      fileName.textContent = fileInput.files[0].name;
  } else {
      fileName.textContent = "Pas de fichier selectionné";
  }
}

/* ------------------------------
Change the form to a loading screen
------------------------------ */
function uploading() {
  var divElement = document.getElementById("uploading");

  divElement.classList.add("uploading");
}


/* ------------------------------
Check status of each tasks to check the checkbox
------------------------------ */
function checkTaskStatus() {
  /*var fileInput =*/

  var ClamAV = document.getElementById('task1');
  var Comodo = document.getElementById('task2');
  var RKhunter = document.getElementById('task3');

  if (fileInput.value === '') {
    ClamAV.disabled = true;
  } else {
    ClamAV.disabled = false;
  }

  if (fileInput.value === '') {
    Comodo.disabled = true;
  } else {
    Comodo.disabled = false;
  }

  if (fileInput.value === '') {
    RKhunter.disabled = true;
  } else {
    RKhunter.disabled = false;
  }
}