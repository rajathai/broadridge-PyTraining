import imported_module


def function_in_main():
    print("Function inside the main script.")


# if __name__ == "__main__":
#     function_in_main()
#     imported_module.function_from_module()

if __name__ == "__main__":
    function_in_main()
    imported_module.function_from_module()
