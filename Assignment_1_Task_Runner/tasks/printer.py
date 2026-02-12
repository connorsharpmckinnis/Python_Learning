#Basic print task
#Doesn't really do much of anything
def run(name:str, **kwargs):
    print(f"Hello, {name}!")
    print("Welcome to the basic print task!")
    return True



if __name__ == "__main__":
    main(name="Connor")