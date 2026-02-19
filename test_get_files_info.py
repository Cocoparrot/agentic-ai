from functions.get_files_info import get_files_info

def main():
    print("get_files_info(\"calculator\", \".\"):")
    try:
        result = get_files_info("calculator", ".")
        print("Result for current directory:")
        for item in result:
            print(f"  - {item['name']}: file_size={item['size']} bytes, is_dir={item['is_dir']}")
    except Exception as e:
        print(f"    Error: {e}")

    print("\nget_files_info(\"calculator\", \"pkg\"):")
    try:
        result = get_files_info("calculator", "pkg")
        print("Result for 'pkg' directory:")
        for item in result:
            print(f"  - {item['name']}: file_size={item['size']} bytes, is_dir={item['is_dir']}")
    except Exception as e:
        print(f"    Error: {e}")

    print("\nget_files_info(\"calculator\", \"/bin\"):")
    try:
        result = get_files_info("calculator", "/bin")
        print("Result for '/bin' directory:")
        for item in result:
            print(f"  - {item['name']}: file_size={item['size']} bytes, is_dir={item['is_dir']}")
    except Exception as e:
        print(f"    Error: {e}")

    print("\nget_files_info(\"calculator\", \"../\"):")
    try:
        result = get_files_info("calculator", "../")
        print("Result for '../' directory:")
        for item in result:
            print(f"  - {item['name']}: file_size={item['size']} bytes, is_dir={item['is_dir']}")
    except Exception as e:
        print(f"    Error: {e}")

if __name__ == "__main__":
    main()