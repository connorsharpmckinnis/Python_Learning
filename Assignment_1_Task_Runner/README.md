How to run the program:
python taskrunner.py --config "config.yaml"

    - Each task will accept different arguments, but the config file will accept all of them. 
    - The program will ignore any arguments that are not accepted by the task.

Config file format:
task: <task_name>
input: <input_string>
retries: <number_of_retries>
name: <name>
age: <age>
city: <city>

Example config file:
task: cipher
input: "Hello World"
retries: 15
name: "Connor McKinnis"
age: 26
city: "Sanford, NC"