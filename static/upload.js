const body = document.querySelector('body');
const upload = document.querySelector('.upload');
const uploadButtonText = document.querySelector('.upload-button-text');
const uploadFilename = document.querySelector('.upload-filename');
const fileInput = document.getElementById('file');
fileInput.onchange = () => uploadFile(fileInput.files[0]);

function getCookie(name) {
  const cookieValue = document.cookie.match('(^|;)\\s*' + name + '\\s*=\\s*([^;]+)');
  return cookieValue ? cookieValue.pop() : '';
}

// Upload file to server
function uploadFile(file) {
    if (file) {
        // Add the file name to the input and change the button to an upload button
        uploadFilename.classList.remove('inactive');
        uploadFilename.innerText = file.name;
        uploadButtonText.innerText = 'Upload';
        fileInput.remove();
        uploadButtonText.addEventListener("click", async () => {
            upload.classList.add("uploading");

            const csrftoken = getCookie('csrftoken');

            // Upload file to the pytyhon server
            const formData = new FormData();
            formData.append('file', file);
            const response = await fetch('upload/', {
                method: 'POST',
                headers: {
                  'X-CSRFToken': csrftoken
                },
                body: formData
            });
            
            setTimeout(() => {
                upload.classList.remove("uploading");
            }, 500000);
        });
    }
}
// Drop stuff
const dropArea = document.querySelector('.drop-area');
['dragenter', 'dragover', 'dragleave', 'drop'].forEach(eventName => {
    dropArea.addEventListener(eventName, preventDefaults, false);
});
function preventDefaults(e) {
    e.preventDefault();
    e.stopPropagation();
}
// Add dropArea bordering when dragging a file over the body
;
['dragenter', 'dragover'].forEach(eventName => {
    body.addEventListener(eventName, displayDropArea, false);
});
['dragleave', 'drop'].forEach(eventName => {
    body.addEventListener(eventName, hideDropArea, false);
});
['dragenter', 'dragover'].forEach(eventName => {
    dropArea.addEventListener(eventName, highlight, false);
});
['dragleave', 'drop'].forEach(eventName => {
    dropArea.addEventListener(eventName, unhighlight, false);
});
function highlight(e) {
    if (!dropArea.classList.contains('highlight'))
        dropArea.classList.add('highlight');
}
function unhighlight(e) {
    dropArea.classList.remove('highlight');
}
function displayDropArea() {
    if (!dropArea.classList.contains('highlight'))
        dropArea.classList.add('droppable');
}
function hideDropArea() {
    dropArea.classList.remove('droppable');
}
// Handle dropped files
dropArea.addEventListener('drop', handleDrop, false);
function handleDrop(e) {
    let dt = e.dataTransfer;
    let files = dt.files;
    let file = files[0];
    uploadFile(file);
}
