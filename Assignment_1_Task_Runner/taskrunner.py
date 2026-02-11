import argparse
from tasks import cipher, json, printer
import yaml

TASKS = {
    "cipher": cipher,
    "json": json,
    "printer": printer
}

def main():
    print("Hello from assignment-1-task-runner!")

def run_task(task_name:str, args):
    task = TASKS.get(task_name, error)
    result = task.run()
    return result

if __name__ == "__main__":
    main()
