import os

def get_files_info(working_directory, directory="."):
    # Get the absolute path of the working directory
    working_dir_abs = os.path.abspath(working_directory)

    # Construct the full path to the target directory
    target_dir = os.path.normpath(os.path.join(working_dir_abs, directory))

    # Check if the target directory is within the working directory
    valid_target_dir = os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs

    if not valid_target_dir:
        raise ValueError(
            f'Cannot list "{directory}" as it is outside the permitted working directory'
        )

    try:
        items = os.listdir(target_dir)
        result = []

        for item in items:
            item_path = os.path.join(target_dir, item)
            is_dir = os.path.isdir(item_path)
            file_size = os.path.getsize(item_path) if not is_dir else 0

            result.append({
                "name": item,
                "size": file_size,
                "is_dir": is_dir
            })

        return result

    except Exception as e:
        raise RuntimeError(str(e))
