# File-Sort-Project
File-Sort-Project
A Python script that organizes files into folders based on their extensions, such as images, documents, videos, and more. It creates folders if they don’t exist and moves unknown files to an "others" folder. Built with os and shutil, this script helps keep directories clutter-free.

🚀 Installation
Clone the repository:

bash
Copy
Edit
git clone https://github.com/Santhoshkannan26/File-Sort-Project.git
cd File-Sort-Project
Run the script:

bash
Copy
Edit
python file_sort.py
📌 Usage
Place the file_sort.py script inside the folder where you want to organize files.
Run the script, and it will:
Create folders based on file extensions (e.g., Images, Documents, Videos).
Move files into their respective folders.
Move unknown files into an Others folder.
📸 Sample Output
Before running the script:

Copy
Edit
my_folder/
│── image1.jpg
│── document1.pdf
│── video1.mp4
│── unknownfile.xyz
After running the script:

Copy
Edit
my_folder/
│── Images/
│   ├── image1.jpg
│── Documents/
│   ├── document1.pdf
│── Videos/
│   ├── video1.mp4
│── Others/
│   ├── unknownfile.xyz
📢 Contributing
Feel free to fork this repository, make improvements, and submit a pull request!
