# CLI Tasks

CLI Tasks is a simple command-line to-do list manager built with Python. It allows users to create, view, and manage tasks efficiently from the terminal.

## Features

- Add new tasks
- View all tasks
- Mark tasks as complete
- Delete tasks
- Clear all tasks

## Installation

1. Download the latest release from the [releases page](https://github.com/iCaran/cli_tasks/releases).
2. Extract the downloaded archive.
3. Navigate to the `app` directory.

## Usage

1. Open a terminal in the `app` directory.
2. Run `./task help` to see available commands.

## Available Commands

- `./task add "task description"`: Add a new task.
- `./task list`: List all tasks.
- `./task complete [task_id]`: Mark a task as complete.
- `./task delete [task_id]`: Delete a task.
- `./task clear`: Clear all tasks.

## Example

```sh
./task add "Write documentation"
./task list
./task complete 1
./task delete 1
./task clear
```

For more details, watch the [explanation video](https://vimeo.com/648902045).

---

### Resume Summary

Developed a command-line to-do list manager in Python, enabling users to efficiently create, view, and manage tasks directly from the terminal. Implemented features for adding, listing, completing, deleting, and clearing tasks, providing a streamlined task management solution.
