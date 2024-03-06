def function_from_module():
    print("Function inside the imported module.")


if __name__ == "__main__":
    print("This script is being run directly")
else:
    print("This script is imported")
