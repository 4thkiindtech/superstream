const fileInput = document.getElementById('fileInput');
const uploadButton = document.getElementById('uploadButton');
const progressBar = document.getElementById('progressBar');
const status = document.getElementById('status');

uploadButton.addEventListener('click', () => {
 if (fileInput.files.length === 0) {
    status.textContent = 'Please select a movie file to upload.';
    return;
 }

 const file = fileInput.files[0];
 const formData = new FormData();
 formData.append('movie', file);

 const xhr = new XMLHttpRequest();
 xhr.open('POST', '/api/upload', true);

 xhr.upload.addEventListener('progress', (event) => {
    if (event.lengthComputable) {
      const percentComplete = (event.loaded / event.total) * 100;
      progressBar.style.width = percentComplete + '%';
    }
 });

 xhr.addEventListener('load', () => {
    if (xhr.status === 200) {
      status.textContent = 'Movie uploaded successfully!';
    } else {
      status.textContent = 'Failed to upload movie.';
    }
 });

 xhr.send(formData);
});