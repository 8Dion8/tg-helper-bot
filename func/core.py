import os

def handle_user_dir_creation(directory_name: str) -> None: 
    directory_name = "usrstorage/" + directory_name
    if not os.path.exists(f"{directory_name}"):
        os.makedirs(directory_name)
        print(f"Directory '{directory_name}' created.")
    else:
        print(f"Directory '{directory_name}' already exists.")

