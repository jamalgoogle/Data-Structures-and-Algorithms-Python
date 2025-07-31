class TaskNode:
    def __init__(self, task):
        self.task = task
        self.next = None

class ToDoList:
    def __init__(self):
        self.head = None

    def add_task(self, task):
        new_node = TaskNode(task)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def remove_task(self, task):
        current = self.head
        prev = None
        while current:
            if current.task == task:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                return True
            prev = current
            current = current.next
        return False

    def show_tasks(self):
        current = self.head
        while current:
            print(f"- {current.task}")
            current = current.next

# استخدام
todo = ToDoList()
todo.add_task("Study data structures")
todo.add_task("Build Linked List project")
todo.show_tasks()
todo.remove_task("Study data structures")
print("\nبعد الحذف:")
todo.show_tasks()
