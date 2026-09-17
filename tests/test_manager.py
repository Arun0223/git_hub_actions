import os
import pytest
from taskflow.manager import TaskManager

@pytest.fixture
def temp_manager(tmp_path):
    # Create a temporary storage file for each test
    storage_file = tmp_path / "test_tasks.json"
    return TaskManager(storage_file=str(storage_file))

def test_add_task(temp_manager):
    task = temp_manager.add_task("Test Task 1")
    assert task.id == 1
    assert task.description == "Test Task 1"
    assert len(temp_manager.list_tasks()) == 1

def test_list_tasks(temp_manager):
    temp_manager.add_task("Task 1")
    temp_manager.add_task("Task 2")
    assert len(temp_manager.list_tasks()) == 2

def test_mark_completed(temp_manager):
    task = temp_manager.add_task("Complete Me")
    success = temp_manager.mark_completed(task.id)
    assert success is True
    assert temp_manager.list_tasks()[0].completed is True

def test_mark_completed_not_found(temp_manager):
    success = temp_manager.mark_completed(999)
    assert success is False

def test_delete_task(temp_manager):
    task = temp_manager.add_task("Delete Me")
    success = temp_manager.delete_task(task.id)
    assert success is True
    assert len(temp_manager.list_tasks()) == 0

def test_delete_task_not_found(temp_manager):
    success = temp_manager.delete_task(999)
    assert success is False

def test_persistence(tmp_path):
    storage_file = str(tmp_path / "persistence.json")
    manager1 = TaskManager(storage_file=storage_file)
    manager1.add_task("Persistent Task")

    manager2 = TaskManager(storage_file=storage_file)
    assert len(manager2.list_tasks()) == 1
    assert manager2.list_tasks()[0].description == "Persistent Task"
