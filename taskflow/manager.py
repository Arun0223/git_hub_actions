import json
import os
from .models import Task
from typing import List, Optional

class TaskManager:
    def __init__(self, storage_file: str = "tasks.json"):
        self.storage_file = storage_file
        self.tasks: List[Task] = self._load_tasks()

    def _load_tasks(self) -> List[Task]:
        if not os.path.exists(self.storage_file):
            return []
        try:
            with open(self.storage_file, "r") as f:
                data = json.load(f)
                return [Task.from_dict(item) for item in data]
        except (json.JSONDecodeError, IOError):
            return []

    def _save_tasks(self):
        with open(self.storage_file, "w") as f:
            json.dump([t.to_dict() for t in self.tasks], f, indent=4)

    def add_task(self, description: str) -> Task:
        new_id = max([t.id for t in self.tasks], default=0) + 1
        task = Task(id=new_id, description=description)
        self.tasks.append(task)
        self._save_tasks()
        return task

    def list_tasks(self) -> List[Task]:
        return self.tasks

    def mark_completed(self, task_id: int) -> bool:
        for task in self.tasks:
            if task.id == task_id:
                task.completed = True
                self._save_tasks()
                return True
        return False

    def delete_task(self, task_id: int) -> bool:
        initial_count = len(self.tasks)
        self.tasks = [t for t in self.tasks if t.id != task_id]
        if len(self.tasks) < initial_count:
            self._save_tasks()
            return True
        return False
