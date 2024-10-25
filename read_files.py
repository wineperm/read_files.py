import os

def read_files_recursively(root_dir, output_file, exclude_files, exclude_dirs):
    with open(output_file, 'w', encoding='utf-8') as out_file:
        for dirpath, dirnames, filenames in os.walk(root_dir):
            # Исключаем директории из обхода
            dirnames[:] = [d for d in dirnames if d not in exclude_dirs]
            for filename in filenames:
                file_path = os.path.join(dirpath, filename)
                if filename not in exclude_files:
                    # Относительный путь к файлу
                    relative_path = os.path.relpath(file_path, root_dir)
                    with open(file_path, 'r', encoding='utf-8', errors='ignore') as in_file:
                        content = in_file.read()
                        out_file.write(f"#{relative_path}\n")
                        out_file.write(content)
                        out_file.write("\n\n")

if __name__ == "__main__":
    # Текущая директория, в которой находится скрипт
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # Путь к выходному файлу, в который будет записано содержимое всех файлов
    output_file = os.path.join(current_dir, 'info.tai')

    # Множество имен файлов, которые нужно исключить из обхода
    exclude_files = {'info.tai', 'read_files.py', 'generate_project_structure.py'}

    # Множество имен директорий, которые нужно исключить из обхода
    exclude_dirs = {'.git'}

    # Вызов функции для рекурсивного чтения файлов
    read_files_recursively(current_dir, output_file, exclude_files, exclude_dirs)

    # Сообщение о завершении работы скрипта
    print(f"Содержимое всех файлов записано в {output_file}")
