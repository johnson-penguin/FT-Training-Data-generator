import subprocess
import os
import json

def get_files_in_directory(directory_path):
    """
    執行 tree 命令，取得指定目錄中的所有檔案，去掉路徑和 .conf 擴展名，並返回陣列。
    Execute the tree command to get all files in the specified directory, remove the path and .conf extension, and return as an array.

    :param directory_path: 目錄路徑 (Directory path)
    :return: 去除路徑與 .conf 的檔案名稱陣列 (Array of file names without path and .conf extension)
    """
    # 執行 tree 命令並獲取輸出
    command = f"tree {directory_path} -if --noreport"
    result = subprocess.run(command, shell=True, capture_output=True, text=True)

    if result.returncode != 0:
        print("Error running tree command")
        return []

    # 解析輸出的檔案名稱，去掉路徑和 .conf 擴展名並儲存在陣列中
    file_names = []
    for line in result.stdout.splitlines():
        # 只選擇檔案行（過濾掉目錄）
        if line.endswith('.conf'):
            # 去掉路徑和 .conf 擴展名
            file_name_without_conf = os.path.basename(line).replace('.conf', '')
            file_names.append(file_name_without_conf)
    
    return file_names

def save_to_json(data, file_path):
    """
    將資料儲存為 JSON 檔案 (Save the data as a JSON file).
    
    :param data: 要儲存的資料（如檔案名稱陣列）(Data to be saved, such as file name array)
    :param file_path: 儲存檔案的路徑 (Path to save the file)
    """
    with open(file_path, 'w', encoding='utf-8') as json_file:
        json.dump({"cu_input_values": data}, json_file, ensure_ascii=False, indent=4)

def natural_sort_key(s):
    """
    生成自然排序鍵（處理數字排序）(Generate a natural sorting key, handling numerical sorting).
    
    :param s: 檔案名稱字串 (File name string)
    :return: 按照數字順序的排序鍵 (Sorting key based on numerical order)
    """
    import re
    return [int(text) if text.isdigit() else text.lower() for text in re.split('([0-9]+)', s)]

# 設定目錄路徑 (Set directory path)
directory_path = '/home/aiml/johnson/Scenario/Scenario_Latest_for_cu_testing/input_data/conf'

# 獲取並處理檔案名稱 (Get and process file names)
cu_input_values = get_files_in_directory(directory_path)

# 根據檔案名稱中的數字部分進行自然排序 (Sort based on the numeric parts of file names)
cu_input_values.sort(key=natural_sort_key)

# 儲存為 JSON 文件 (Save as JSON file)
output_json_path = '/home/aiml/johnson/Scenario/Scenario_Latest_for_cu_testing/cu_input_values.json'
save_to_json(cu_input_values, output_json_path)

# 輸出結果 (Output the result)
print(f"Total number of cu_input_values: {len(cu_input_values)}")  # 輸出檔案數量 (Output the number of files)
print(f"cu_input_values sorted and saved to {output_json_path}")  # 輸出儲存的 JSON 路徑 (Output the saved JSON path)
