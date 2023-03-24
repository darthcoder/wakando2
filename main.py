import unittest

# create a task class
class Task:
    def __init__(self, name, priority, due_date, status, assigned_to, project, task_id, tags=None):
        self.name = name
        self.priority = priority
        self.due_date = due_date
        self.status = status
        self.assigned_to = assigned_to
        self.project = project
        self.task_id = task_id
        self.tags = tags or []

    def __str__(self):
        return self.name
    
    def __repr__(self):
        return self.name
    
    def __eq__(self, other):
        return self.task_id == other.task_id

    def  __hash__(self):
        return hash(self.task_id)
    
    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name
    
    def set_priority(self, priority):
        self.priority = priority

    def get_priority(self):
        return self.priority
    
    def set_due_date(self, due_date):
        self.due_date = due_date

    def get_due_date(self):
        return self.due_date
    
    def set_status(self, status):
        self.status = status

    def get_status(self):
        return self.status
    
    def set_assigned_to(self, assigned_to):
        self.assigned_to = assigned_to
    
    def get_assigned_to(self):
        return self.assigned_to
    
    def set_project(self, project):
        self.project = project

    def get_project(self):
        return self.project
    
    def set_task_id(self, task_id):
        self.task_id = task_id

    def get_task_id(self):
        return self.task_id
    
    def set_tags(self, tags):
        self.tags = tags
    
    def get_tags(self):
        return self.tags
    
    def add_tag(self, tag):
        self.tags.append(tag)

    def remove_tag(self, tag):
        self.tags.remove(tag)

    
    

# create a task list class
class TaskList:
    def __init__(self):
        self.task_list = []
    
    def add_task(self, task):
        self.task_list.append(task)
    
    def remove_task(self, task):
        self.task_list.remove(task)
    
    def get_task_list(self):
        return self.task_list
    
    def get_task_by_id(self, task_id):
        for task in self.task_list:
            if task.get_task_id() == task_id:
                return task
        return None
    
    def get_task_by_name(self, task_name):
        for task in self.task_list:
            if task.get_name() == task_name:
                return task
        return None
    
    def get_task_by_priority(self, task_priority):
        for task in self.task_list:
            if task.get_priority() == task_priority:
                return task
        return None
    
    def get_task_by_due_date(self, task_due_date):
        for task in self.task_list:
            if task.get_due_date() == task_due_date:
                return task
        return None
    
    def get_task_by_status(self, task_status):
        for task in self.task_list:
            if task.get_status() == task_status:
                return task
        return None
    
    def get_task_by_assigned_to(self, task_assigned_to):
        for task in self.task_list:
            if task.get_assigned_to() == task_assigned_to:
                return task
        return None
    
    def get_task_by_project(self, task_project):
        for task in self.task_list:
            if task.get_project() == task_project:
                return task
        return None
    
    def get_task_by_tag(self, task_tag):
        for task in self.task_list:
            if task_tag in task.get_tags():
                return task
        return None
    
    def get_task_by_tags(self, task_tags):
        for task in self.task_list:
            if task_tags == task.get_tags():
                return task
        return None
    

    

# create a task manager class   
class TaskManager:
    def __init__(self):
        self.task_list = TaskList()
    
    def add_task(self, task):
        self.task_list.add_task(task)
    
    def remove_task(self, task):
        self.task_list.remove_task(task)
    
    def get_task_list(self):
        return self.task_list.get_task_list()
    
    def get_task_by_id(self, task_id):
        return self.task_list.get_task_by_id(task_id)
    
    def get_task_by_name(self, task_name):
        return self.task_list.get_task_by_name(task_name)
    
    def get_task_by_priority(self, task_priority):
        return self.task_list.get_task_by_priority(task_priority)
    
    def get_task_by_due_date(self, task_due_date):
        return self.task_list.get_task_by_due_date(task_due_date)
    
    def get_task_by_status(self, task_status):
        return self.task_list.get_task_by_status(task_status)
    
    def get_task_by_assigned_to(self, task_assigned_to):
        return self.task_list.get_task_by_assigned_to(task_assigned_to)
    
    def get_task_by_project(self, task_project):
        return self.task_list.get_task_by_project(task_project)
    
    def get_task_by_tag(self, task_tag):
        for task in self.task_list.get_task_list():
            if task_tag in task.get_tags():
                return task
        return None
    
    def get_task_by_tags(self, task_tags):
        for task in self.task_list.get_task_list():
            if task_tags == task.get_tags():
                return task
        return None
    
    def get_task_by_tags_and(self, task_tags):
        for task in self.task_list.get_task_list():
            if all(tag in task.get_tags() for tag in task_tags):
                return task
        return None
    
    def get_task_by_tags_or(self, task_tags):
        for task in self.task_list.get_task_list():
            if any(tag in task.get_tags() for tag in task_tags):
                return task
        return None
    
    


# I have a few questions about this code:
# 1. Is there a better way to do this? I feel like there is a better way to do this.
# 2. Is there a way to make this code more efficient? I feel like there is a way to make this code more efficient.
# 3. Is there a way to make this code more readable? I feel like there is a way to make this code more readable.
# 4. Is there a way to make this code more concise? I feel like there is a way to make this code more concise.
# 5. Is there a way to make this code more maintainable? I feel like there is a way to make this code more maintainable.
# 6. Is there a way to make this code more scalable? I feel like there is a way to make this code more scalable.
# 7. Is there a way to make this code more testable? I feel like there is a way to make this code more testable.
# 8. Is there a way to make this code more secure? I feel like there is a way to make this code more secure.
# 9. Is there a way to make this code more reliable? I feel like there is a way to make this code more reliable.
# 10. Is there a way to make this code more reusable? I feel like there is a way to make this code more reusable.
# 11. Is there a way to make this code more extensible? I feel like there is a way to make this code more extensible.
# 12. Is there a way to make this code more flexible? I feel like there is a way to make this code more flexible.
# 13. Is there a way to make this code more portable? I feel like there is a way to make this code more portable.
# 14. Is there a way to make this code more performant? I feel like there is a way to make this code more performant.


class TaskListTest(unittest.TestCase):
    def setUp(self):
        self.task_list = TaskList()
        self.task = Task("Task 1", "High", "2021-01-01", "Not Started", "John Doe", "Project 1", 1)
        self.task_list.add_task(self.task)
    
    def test_add_task(self):
        self.assertEqual(self.task_list.get_task_list()[0], self.task)
    
    def test_remove_task(self):
        self.task_list.remove_task(self.task)
        self.assertEqual(self.task_list.get_task_list(), [])
    
    def test_get_task_by_id(self):
        self.assertEqual(self.task_list.get_task_by_id(1), self.task)
    
    def test_get_task_by_name(self):
        self.assertEqual(self.task_list.get_task_by_name("Task 1"), self.task)
    
    def test_get_task_by_priority(self):
        self.assertEqual(self.task_list.get_task_by_priority("High"), self.task)
    
    def test_get_task_by_due_date(self):
        self.assertEqual(self.task_list.get_task_by_due_date("2021-01-01"), self.task)
    
    def test_get_task_by_status(self):
        self.assertEqual(self.task_list.get_task_by_status("Not Started"), self.task)
    
    def test_get_task_by_assigned_to(self):
        self.assertEqual(self.task_list.get_task_by_assigned_to("John Doe"), self.task)
    
    def test_get_task_by_project(self):
        self.assertEqual(self.task_list.get_task_by_project("Project 1"), self.task)
    
    def tearDown(self):
        self.task_list = None
        self.task = None

    


if __name__ == "__main__":
    unittest.main()
