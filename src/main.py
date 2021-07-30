from db_handling_files.db_handler import Handler

if __name__ == "__main__":
    path = input(
        "Enter the filename where the db exists or has to be created if it doesn't exist: "
    )
    handler = Handler(path)
    handler.create_db_if_not_exists()
    print("completed")
