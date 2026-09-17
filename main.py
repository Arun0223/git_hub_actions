import sys
from taskflow.manager import TaskManager

def main():
    manager = TaskManager()

    if len(sys.argv) < 2:
        print("Usage: python main.py [add|list|done|del] [args]")
        print("  add \"task description\"")
        print("  list")
        print("  done [task_id]")
        print("  del [task_id]")
        return

    command = sys.argv[1]

    if command == "add" and len(sys.argv) > 2:
        desc = sys.argv[2]
        task = manager.add_task(desc)
        print(f"Added task {task.id}: {desc}")

    elif command == "list":
        tasks = manager.list_tasks()
        if not tasks:
            print("No tasks found.")
        for t in tasks:
            status = "✓" if t.completed else " "
            print(f"[{status}] {t.id}: {t.description}")

    elif command == "done" and len(sys.argv) > 2:
        try:
            tid = int(sys.argv[2])
            if manager.mark_completed(tid):
                print(f"Task {tid} marked as done!")
            else:
                print(f"Task {tid} not found.")
        except ValueError:
            print("Invalid task ID.")

    elif command == "del" and len(sys.argv) > 2:
        try:
            tid = int(sys.argv[2])
            if manager.delete_task(tid):
                print(f"Task {tid} deleted.")
            else:
                print(f"Task {tid} not found.")
        except ValueError:
            print("Invalid task ID.")
    else:
        print("Invalid command or missing arguments.")

if __name__ == "__main__":
    main()
