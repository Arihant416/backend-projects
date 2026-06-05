# 🚀 Task-Tracker-CLI

A sleek, interactive Command Line Interface (CLI) application for managing tasks. Built entirely in Python, this tool provides a continuous interactive shell (REPL) to add, update, track, and delete tasks without constantly restarting the application.
Data is seamlessly and safely persisted to a local JSON file using an auto-save mechanism upon exit.

Project URL : [https://roadmap.sh/projects/task-tracker](https://roadmap.sh/projects/task-tracker)

## ✨ Features

* *Interactive Playground:* Powered by Python's cmd module, offering a continuous shell with a custom task-cli> prompt.
* *Smart State Tracking:* Tasks automatically update their updated_at timestamps whenever their properties are modified.
* *Status Management:* Easily transition tasks between todo, in-progress, and done.
* *Robust Error and Exception Handling:* Built-in custom exceptions ensure graceful failures without crashing the application.
* *Auto-Saving:* Tasks are safely serialized and written to data.json when exiting the playground.

## 🏗️ Architecture

This project is built using strict separation of concerns, heavily inspired by the *Model-View-Controller (MVC)* design pattern:

* *app.py (The View / Router):* Manages the interactive cmd shell, parses raw user input, and routes commands to the middleware.
* *middleware.py (The Controller):* Acts as the executive layer. It catches custom exceptions, interacts with the backend manager, and formats the terminal output for the user.
* *task_manager.py (The Model / Database Layer):* Handles all pure data manipulation, state management, and file I/O operations with data.json.
* *task.py (The Entity):* Contains the strictly typed Task model, ITask interface, and Status enumerations.

## 🚀 Getting Started

### Prerequisites

* *Python 3.11+* (Requires support for StrEnum)
* No external dependencies required! The app uses 100% standard Python libraries.

### Installation & Execution

 1. Clone the repository to your local machine.
 2. Navigate to the project directory.
 3. Boot up the playground:

```bash
python3 app.py
```

## 🛠️ Available Commands

Once inside the task-cli> prompt, you can use the following commands. Type help or ? at any time to see the built-in documentation.

| Command | Usage Example | Description |
|---|---|---|
| *add* | add "Buy groceries" | Creates a new task with the status todo. |
| *update* | update 1 "Buy fresh groceries" | Updates the description of the task with ID 1. |
| *delete* | delete 1 | Permanently removes the task with ID 1. |
| *mark_in_progress* | mark_in_progress 1 | Sets the status of task 1 to in-progress. |
| *mark_done* | mark_done 1 | Sets the status of task 1 to done. |
| *status* | status 1 | Checks the current status of task 1. |
| *list* | list | Lists all tasks currently in the registry. |
| *list status* | list done | Filters the list by todo, in-progress, or done. |
| *exit* | exit | Saves all data to data.json and closes the application. |

📂 Project

```text
├── app.py                  # Entry point and interactive shell
├── middleware.py           # Command execution, error handling, and output formatting
├── task_manager.py         # Data persistence and logic
├── task.py                 # Task entity and enums
├── custom_exceptions.py    # Custom error definitions
└── data.json               # Auto-generated database file
```
