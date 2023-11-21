import os
from werkzeug.utils import secure_filename

# Set the upload folder
UPLOAD_FOLDER = 'uploads'

# Get the file from the POST request
file = request.files['file']

# Check if a file has been uploaded
if file:
    # Make the filename secure
    filename = secure_filename(file.filename)

    # Create the upload folder if it doesn't exist
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)

    # Save the file in the upload folder
    file.save(os.path.join(UPLOAD_FOLDER, filename))

    print("The file has been uploaded.")
else:
    print("No file provided")