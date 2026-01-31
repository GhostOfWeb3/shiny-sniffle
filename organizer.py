import sys
import time
import os
import shutil  # NEW: Library for moving files
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Define your source and destination paths
source_dir = os.path.join(os.path.expanduser("~"), "Downloads")

# Define where you want things to go.
# Feel free to change "Organized_Images" to whatever you want the folder to be named.
dest_dirs = {
    "images": os.path.join(source_dir, "Organized_Images"),
    "docs": os.path.join(source_dir, "Organized_Docs"),
    "installers": os.path.join(source_dir, "Organized_Installers"),
}


def move_file(file_path, dest_folder):
    # 1. Create the destination folder if it doesn't exist yet
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)

    # 2. Get the file name
    filename = os.path.basename(file_path)
    new_path = os.path.join(dest_folder, filename)

    # 3. Check if a file with that name already exists to avoid overwriting
    if os.path.exists(new_path):
        print(f"File already exists in destination: {filename}. Skipping.")
        return

    # 4. Move it!
    try:
        # Small pause to let the browser finish releasing the file
        time.sleep(1)
        shutil.move(file_path, new_path)
        print(f"Moved {filename} to {dest_folder}")
    except Exception as e:
        print(f"Error moving file: {e}")


class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.is_directory:
            return

        filename, extension = os.path.splitext(event.src_path)
        extension = extension.lower()

        if extension in [".tmp", ".crdownload", ".part"]:
            return

        # --- DECISION LOGIC ---
        if extension in [".jpg", ".jpeg", ".png", ".gif", ".webp"]:
            move_file(event.src_path, dest_dirs["images"])

        elif extension in [".pdf", ".docx", ".txt", ".xlsx"]:
            move_file(event.src_path, dest_dirs["docs"])

        elif extension in [".zip", ".rar", ".exe", ".msi"]:
            move_file(event.src_path, dest_dirs["installers"])


# START THE SCRIPT
print(f"Watching {source_dir}...")
event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, source_dir, recursive=False)
observer.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
    print("Stopping...")

observer.join()
