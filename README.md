# TaskFlow - Simple CLI Task Manager

A simple Python project created for testing and CI/CD demonstration.

## Features
- Add tasks
- List tasks
- Mark tasks as completed
- Delete tasks
- Persistence via JSON file

## Installation
```bash
pip install -r requirements.txt
```

## Usage
```bash
# Add a task
python main.py add "Learn Claude Code"

# List tasks
python main.py list

# Mark task 1 as done
python main.py done 1

# Delete task 1
python main.py del 1
```

## Testing
Run the tests using pytest:
```bash
pytest
```
