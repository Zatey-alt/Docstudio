# DocStudio

DocStudio is a simple web application built with Flask that allows users to store and manage document and audio files with ease.

## Features

- **Upload Files:** Easily upload document (pdf, doc, docx) and audio (mp3, wav) files.
- **View All Files:** Browse and view a list of all uploaded files with details such as name and date added.
- **Search Files:** Search for files based on their names.
- **Show Documents:** View a list of uploaded document files only.
- **Show Audios:** View a list of uploaded audio files only.
- **Open Files:** Open and view document files in a new tab.
- **Delete Files:** Delete files from the storage.

## Getting Started

1. Clone the repository:

    ```bash
    git clone <repository_url>
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Run the application:

    ```bash
    python app.py
    ```

4. Visit [http://localhost:5000](http://localhost:5000) in your web browser.

## Usage

1. **Splash Page:**
   - Upon accessing the application, you will be welcomed with a splash page. Click the "Start" button to enter the main application.

2. **Main Page (All Files):**
   - The main page displays all uploaded files, including documents and audios.
   - Use the navigation links to filter files by Documents or Audios.
   - Use the search bar to search for specific files.

3. **Document and Audio Pages:**
   - Clicking on "Documents" or "Audios" in the navigation will take you to pages that display only documents or audios, respectively.

4. **Uploading Files:**
   - Click the "Upload" button to upload new files. Choose a file and click "Upload."

5. **File Actions:**
   - Each file entry displays its name, date added, and actions.
   - Actions include opening the file in a new tab and deleting the file.

## File Structure

- `app.py`: Flask application script.
- `templates/`: HTML templates for the different pages.
- `static/`: Static files such as stylesheets and images.

## Dependencies

- Flask
- Lordicon (for icons)

## License

This project is licensed under the [MIT License](LICENSE). Feel free to use, modify, and distribute the code.
