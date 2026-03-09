# Organizer

A straightforward Python script designed to streamline file management by automatically sorting and organizing files within a specified directory into categorized subfolders based on their file types. This tool helps declutter crowded directories, making your file system more manageable and accessible.

## Features

*   **Automated File Sorting**: Quickly categorize and move files such as documents, images, videos, audio, archives, and executables into dedicated subdirectories.
*   **Dynamic Folder Creation**: Automatically creates appropriate subfolders (e.g., `Documents`, `Images`, `Videos`, `Archives`, `Others`) if they do not already exist in the target directory.
*   **Intelligent Categorization**: Identifies file types based on common file extensions and groups them logically.
*   **Command Line Interface**: Easy to use and integrate into workflows via a simple command line execution.
*   **Clear Feedback**: Provides real-time information on files being moved and folders being created during the organization process.

## Tech Stack

*   **Python**: The core programming language used to develop this script.
    *   **Standard Libraries**: Relies solely on Python's built-in modules, primarily `os` for interacting with the operating system (e.g., creating directories, checking file paths) and `shutil` for high-level file operations (e.g., moving files). No external dependencies are required.

## Project Structure

The project is minimalist, consisting of a single Python script:

```
.
└── organizer.py
```

## Installation Instructions

To get started with the Organizer script, ensure you have Python 3 installed on your system.

1.  **Download the script**:
    Download the `organizer.py` file to a directory of your choice. If you obtained the file directly, simply place it in your desired working directory.

2.  **Verify Python Installation**:
    Confirm that Python 3 is installed on your system by running the following command in your terminal or command prompt:
    ```bash
    python3 --version
    ```
    If Python 3 is not installed, please download it from the official Python website: [python.org](https://www.python.org/downloads/).

3.  **No further dependencies**:
    This script relies only on Python's standard library, so no `pip install` commands or additional package installations are necessary.

## Usage Instructions

The `organizer.py` script is designed to be run from the command line, taking the target directory path as its main argument.

1.  **Navigate to the script's directory**:
    Open your terminal or command prompt and change your current directory to where you have saved `organizer.py`.
    ```bash
    cd /path/to/your/organizer_script/
    ```

2.  **Run the script**:
    Execute the script by providing the absolute or relative path to the directory you wish to organize.

    **Important**: The script will create subfolders and move files *within* the specified directory. It is highly recommended to back up important data or test with a sample directory first to understand its behavior.

    ```bash
    python3 organizer.py /path/to/your/cluttered_directory
    ```
    **Example**:
    If you want to organize files in your `~/Downloads` folder, you would run:
    ```bash
    python3 organizer.py ~/Downloads
    ```
    The script will then process the files in the specified directory, creating folders like `Images`, `Documents`, `Videos`, etc., and moving files into their respective categories. Files that do not match predefined categories will be moved into an `Others` folder.

## License Information

This project is licensed under the MIT License. For more details, see the full license text below.

```
MIT License

Copyright (c) [Year] [Your Name or Project Maintainers]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```