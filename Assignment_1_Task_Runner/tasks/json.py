import json
import random
# Basic File Write Task

def write_file(content_dict:dict, file_path:str=None):
    """
    Writes a dictionary to a file as a JSON string.
    """
    if file_path is None:
        file_path = "output.json"
    json_string = json.dumps(content_dict, indent=4)

    with open(file_path, 'w') as file:
        file.write(json_string)

    print(f"Successfully wrote to {file_path}")

def generate_dict(name:str, age:int=None, city:str=None) -> dict:
    """
    Generates a dictionary with the given name, age, and city.
    """
    if age is None:
        age = random.randint(10, 100)
    if city is None:
        city = random.choice(["New York", "Los Angeles", "Chicago", "Houston", "Phoenix"])
    return {
        "name": name,
        "age": age,
        "city": city
    }

def main(name:str, age:int=None, city:str=None):
    content_dict = generate_dict(name, age, city)
    write_file(content_dict, "output.json")

if __name__ == "__main__":
    main("Connor", 25, "New York")