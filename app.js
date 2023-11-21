const express = require('express');
const multer = require('multer');
const path = require('path');

const app = express();

// Set up Multer to handle file uploads
const storage = multer.diskStorage({
 destination: (req, file, cb) => {
    cb(null, path.join(__dirname, 'uploads'));
 },
 filename: (req, file, cb) => {
    cb(null, Date.now() + '-' + file.originalname);
 },
});

const upload = multer({ storage: storage });

// Define a POST route to handle file uploads
app.post('/api/upload', upload.single('movie'), (req, res) => {
 if (!req.file) {
    return res.status(400).json({ message: 'Please upload a movie file.' });
 }

 res.status(200).json({ message: 'Movie uploaded successfully.' });
});

// Start the server
const port = process.env.PORT || 3000;
app.listen(port, () => {
 console.log(`Server is running on port ${port}`);
});
//In this code, we're using Multer to handle file uploads. 
//We've set up Multer to store the uploaded files in a folder named "uploads" within our project directory. 
//The folder "uploads" should be created automatically when the first file is uploaded.