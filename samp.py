import os
import shutil
import subprocess
from tkinter import Tk, Label, Entry, Button, filedialog, messagebox


class App:
    """Class for the main application."""

    def __init__(self, master):
        """Initialize the application."""
        self.master = master
        self.master.title("RTF to JSON Converter")
        self.label = Label(master, text="Enter Output Directory:")
        self.label.pack()

        self.entry = Entry(master)
        self.entry.pack()

        self.browse_button = Button(master, text="Browse", command=self.browse)
        self.browse_button.pack()

        self.run_button = Button(master, text="Run", command=self.run)
        self.run_button.pack()

    def browse(self):
        """Open a file dialog to select a directory."""
        folder_selected = filedialog.askdirectory()
        self.entry.delete(0, 'end')
        self.entry.insert(0, folder_selected)

    def run(self):
        """Run the conversion process."""
        output_directory = self.entry.get()
        if not output_directory:
            messagebox.showerror("Error", "Please enter an output directory.")
            return

        if not os.path.exists(output_directory):
            os.mkdir(output_directory)

        # Define and run the conversion process here
        # Assuming process_files is a placeholder for the actual process
        process_files(output_directory)

        messagebox.showinfo("Info", "Process completed successfully.")


def process_files(directory):
    """Process all files in the given directory."""
    for root, _, files in os.walk(/Users/adithi/Desktop/jenkins_folder):
        for file in files:
            file_path = os.path.join(root, file)
            if file.endswith('.rtf'):
                process_file(/Users/adithi/Desktop/jenkins_folder/L-16-01-07-random.rtf)


def process_file(file_path):
    """Process a single file."""
    try:
        # Placeholder for actual file processing logic
        # For example, convert RTF to JSON
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        print(content)  # Replace with actual processing logic
    except Exception as e:
        print(f"An error occurred while processing {file_path}: {e}")


def delete_folder(/Users/adithi/Desktop/jenkins_folder):
    """Delete a folder and its contents."""
    try:
        shutil.rmtree(/Users/adithi/Desktop/jenkins_folder)
        print(f"Deleted folder: {folder_path}")
    except Exception as e:
        print(f"An error occurred while deleting folder {folder_path}: {e}")


def run_command(command):
    """Run a shell command."""
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while running command '{command}': {e}")


def main():
    """Main function to run the application."""
    root = Tk()
    app = App(root)
    root.mainloop()


if __name__ == "__main__":
    main()
