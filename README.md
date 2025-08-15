This Python program implements a simple To-Do List manager that allows users to add and delete tasks while keeping them saved for future use. The tasks are stored in a text file named todo.txt, enabling the list to persist even after the program is closed.

When the program starts, it checks if the file exists and loads the saved tasks into a list. The add_task() function lets users add a new task, ensuring that blank entries are not allowed. Each valid task is appended to the list and written to the file using the save_tasks() function.

The delete_task() function enables removal of a specific task from the list. Once a task is deleted, the updated list is saved back to the file. If an attempt is made to delete without selecting a task, a warning is displayed.

File operations are handled through two helper functions: load_tasks() for reading tasks from the file and save_tasks() for updating it. This program combines basic Python concepts such as lists, file handling, and conditional checks to create a functional task management system. It is a straightforward yet effective way to manage daily tasks with persistent storage.

Steps to open -
Save the code as todo_list.py.

Make sure Python is installed and added to PATH.

Open Command Prompt/Terminal.

Navigate to the file’s folder using cd.

Run:

python todo_list.py


Tasks will be saved in todo.txt in the same folder
