import argparse
from tasks import cipher, json, printer, error
import yaml

def parse_yaml(file_path:str):
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)


parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument(
    "--task",
    help="Name of the task to run"
)

parser.add_argument(
    "--input",
    help="Input string for the task"
)

parser.add_argument(
    "--retries",
    type=int,
    default=5,
    help="Number of retries for applicable tasks"
)

parser.add_argument(
    "--name",
    default="John Smith",
    help="A name input for applicable tasks"
)

parser.add_argument(
    "--age",
    type=int,
    default=50,
    help="An age input for applicable tasks"
)

parser.add_argument(
    "--city",
    default="Raleigh",
    help="A city input for applicable tasks"
)

parser.add_argument(
    "--config",
    help="Path to a YAML config file"
)

TASKS = {
    "cipher": cipher,
    "json": json,
    "printer": printer,
    "error": error
}

def main(task:str, **kwargs):
    print("Hello from assignment-1-task-runner!")

def run_task(task_name:str, **kwargs):
    task = TASKS.get(task_name, error)
    print(f"Running {task}")
    result = task.run(**kwargs)
    return result

args = parser.parse_args()

task = args.task
input_string = args.input
retries = args.retries
name = args.name
age = args.age
city = args.city
config = args.config

if config:
    config_data = parse_yaml(config)
    print(config_data)
    task = config_data.get("task", task)
    input_string = config_data.get("input", input_string)
    retries = config_data.get("retries", retries)
    name = config_data.get("name", name)
    age = config_data.get("age", age)
    city = config_data.get("city", city)

run_task(task_name=task, input=input_string, retries=retries, name=name, age=age, city=city)
