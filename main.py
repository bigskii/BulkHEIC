from heic2png import HEIC2PNG as h2p
import tkinter as tk
import tkinter.filedialog
import os

root = tk.Tk()
folder = ''

label = tk.Label(root, text="Select a folder")
label.pack()

button = tk.Button(root, text="Open Folder File Browser", command=lambda: open_folder_file_browser())
button.pack()

def find_heic_files(directory):
    heic_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.lower().endswith('.heic'):
                heic_files.append(os.path.join(root, file))
    return heic_files

def open_folder_file_browser():
    folder = tk.filedialog.askdirectory()
    if __name__ == "__main__":
        search_directory = folder
        heic_files_list = find_heic_files(search_directory)
        for i in heic_files_list:
            currentheic = h2p(i)
            currentheic.save()
        label.config(text=f"{len(heic_files_list)} files converted.")

root.mainloop()





