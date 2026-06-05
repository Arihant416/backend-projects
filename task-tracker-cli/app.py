import cmd
import middleware
from task import Status


class TaskCLI(cmd.Cmd):
    intro = "Welcome to the Task-CLI Playground! Type 'help' or '?' to list commands.\n"

    prompt = "task-cli> "

    def do_add(self, arg):
        """Add a new task: add <description>"""
        if not arg:
            print("Error: Please provide a description.")
            return
        middleware.add_task(arg)

    def do_update(self, arg):
        """Update a task description: update <id> <new description>"""
        parts = arg.split(" ", 1)
        if len(parts) < 2:
            print("Error: Usage: update <id> <new description>")
            return

        try:
            task_id = int(parts[0])
            description = parts[1]
            middleware.update_task(task_id, description)
        except ValueError:
            print("Error: Task ID must be a valid number.")

    def do_delete(self, arg):
        """Delete a task: delete <id>"""
        try:
            task_id = int(arg)
            middleware.delete_task(task_id)
        except ValueError:
            print("Error: Task ID must be a valid number.")

    def do_check_status(self, arg):
        """Get status of a task: status <id>"""
        try:
            task_id = int(arg)
            middleware.get_task_status(task_id)
        except ValueError:
            print(f"Error: Task ID must be a valid number")

    def do_mark_in_progress(self, arg):
        """Mark a task as in-progress: mark_in_progress <id>"""
        try:
            task_id = int(arg)
            middleware.mark_status(task_id, Status.in_progress)
            print(f"Task {task_id} marked as in-progress.")
        except ValueError:
            print("Error: Task ID must be a valid number.")
        except Exception as e:
            print(f"StatusUpdateFailure: {e}")

    def do_mark_done(self, arg):
        """Mark a task as done: mark_done <id>"""
        try:
            task_id = int(arg)
            middleware.mark_status(task_id, Status.complete)
            print(f"Task {task_id} marked as done.")
        except ValueError:
            print("Error: Task ID must be a valid number.")
        except Exception as e:
            print(f"StatusUpdateFailure: {e}")

    def do_list(self, arg):
        """List tasks. Optional: list <todo|in-progress|done>"""
        if arg in ["todo", "in-progress", "done"]:
            middleware.list_task_by_status(arg)
        elif arg == "":
            middleware.list_all_tasks()
        else:
            print("Error: Invalid status. Use todo, in-progress, or done.")

    def do_exit(self, arg):
        """Save tasks and exit the playground."""
        print("Saving tasks and exiting playground... Goodbye!")
        middleware.task_manager.save_tasks_to_file()
        return True


def main():
    TaskCLI().cmdloop()


if __name__ == "__main__":
    main()
