## `get_files_in_directory.py` Read Directory and Save Filenames as JSON

## Overview

This script aims to get all `.conf` file names from a specified directory, remove the path and `.conf` extension from the file names, and then save them in JSON format sorted naturally. The processed filenames can be used for other automation configuration tasks or data analysis.

### Main Features

1. **Get all `.conf` file names in the directory**  
   Use the `tree` command to traverse the specified directory, extract `.conf` file names, and remove the path and `.conf` extension.

2. **Natural sorting**  
   Sort the file names based on the numeric part, ensuring the filenames are ordered numerically rather than alphabetically.

3. **Save as JSON file**  
   Save the processed file names in JSON format, making it easier to read and process later.

### Function Descriptions

#### `get_files_in_directory(directory_path)`

- **Description**:  
  Executes the `tree` command to traverse the specified directory and get all `.conf` file names, removing the path and `.conf` extension.

- **Parameters**:  
  - `directory_path`: Directory path

- **Return Value**:  
  - Array of file names without path and `.conf` extension

#### `save_to_json(data, file_path)`

- **Description**:  
  Saves data (such as a list of file names) as a JSON file.

- **Parameters**:  
  - `data`: Data to be saved (such as file name array)
  - `file_path`: Path to save the file

- **Return Value**:  
  - No return value, the data will be saved in the specified JSON file.

#### `natural_sort_key(s)`

- **Description**:  
  This function generates a natural sorting key for filenames, allowing sorting based on the numeric part of the filename.

- **Parameters**:  
  - `s`: File name string

- **Return Value**:  
  - Sorting key based on numerical order

### Usage Instructions

1. **Set directory path**  
   In the script, the variable `directory_path` is set to the path of the directory containing the `.conf` files. Change this to the path of your local directory.

2. **Run the script**  
   When executing the script, it will:  
   - Execute the `tree` command to extract all `.conf` file names from the directory.  
   - Remove the path and `.conf` extension from the filenames and sort them naturally.  
   - Finally, it will save the file names in JSON format and output the file path and the number of files.

### Input/Output Examples

- **Input Example**:  
  Assuming the directory `/home/aiml/johnson/Scenario/Scenario_Latest_for_cu_testing/input_data/conf` contains the following files:  
  - `001_cu_gnb_Num_Threads_PUSCH.conf`  
  - `002_cu_gnb_Remote_Address.conf`  
  - `003_cu_gnb_IP_Configuration.conf`

- **Output Example**:  
  The result saved in `cu_input_values.json`:  
  ```json
  {
    "cu_input_values": [
      "001_cu_gnb_Num_Threads_PUSCH",
      "002_cu_gnb_Remote_Address",
      "003_cu_gnb_IP_Configuration"
    ]
  }
