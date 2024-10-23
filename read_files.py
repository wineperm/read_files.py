import os

def read_files_recursively(root_dir, output_file, exclude_files, exclude_dirs):
    with open(output_file, 'w', encoding='utf-8') as out_file:
        for dirpath, dirnames, filenames in os.walk(root_dir):
            # Исключаем директории из обхода
            dirnames[:] = [d for d in dirnames if d not in exclude_dirs]
            for filename in filenames:
                file_path = os.path.join(dirpath, filename)
                if filename not in exclude_files:
                    with open(file_path, 'r', encoding='utf-8', errors='ignore') as in_file:
                        content = in_file.read()
                        out_file.write(f"{file_path}\n")
                        out_file.write(content)
                        out_file.write("\n\n")

if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.abspath(__file__))
    output_file = os.path.join(current_dir, 'output.txt')
    exclude_files = {'output.txt', 'read_files.py', 'generate_project_structure.py'}
    exclude_dirs = {'.git'}
    read_files_recursively(current_dir, output_file, exclude_files, exclude_dirs)
    print(f"Содержимое всех файлов записано в {output_file}")
