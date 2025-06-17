import json
import re
import subprocess
import time
from pathlib import Path

base_dir = Path(__file__).resolve().parent
print(f"Base directory: {base_dir}")

def test_replace_cu_input_index(notebook_path, cu_input_value, output_notebook_path):
    """
    Replace cu_input_index in the notebook file with the new value using regex, and save it as a new file.

    :param notebook_path: The path to the original notebook file.
    :param cu_input_value: The new value to replace in cu_input_index.
    :param output_notebook_path: The path to save the modified notebook file.
    :return: The modified notebook content.
    """
    # Read the notebook content
    with open(notebook_path, 'r', encoding='utf-8') as file:
        notebook_content = json.load(file)

    # Iterate over the notebook cells and replace cu_input_index in 'source' field
    for cell in notebook_content.get('cells', []):
        if cell.get('cell_type') == 'code':
            # Replace the cu_input_index value in the source code cell
            cell['source'] = [re.sub(r'cu_input_index\s*=\s*"[^\"]+"', f'cu_input_index = "{cu_input_value}"', line) for line in cell['source']]

    # Save the modified content to a new notebook file
    with open(output_notebook_path, 'w', encoding='utf-8') as file:
        json.dump(notebook_content, file, indent=2)

    return notebook_content

def load_cu_input_values(json_path):
    with open(json_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data['cu_input_values']

def run_ipynb(input_notebook_path, output_notebook_path):
    """
    Run the Jupyter notebook programmatically using nbconvert.

    :param input_notebook_path: Path to the input .ipynb file.
    :param output_notebook_path: Path to save the executed notebook.
    """
    command = [
        'jupyter', 'nbconvert',
        '--to', 'notebook', '--execute', '--inplace',
        '--allow-errors', str(input_notebook_path)
    ]
    
    # Specify the output notebook path
    command.extend(['--output', str(output_notebook_path)])
    
    try:
        # Run the command
        subprocess.run(command, check=True)
        print(f"Notebook executed successfully: {output_notebook_path}")
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while executing notebook: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

# Example notebook path (original file)
notebook_path = '/home/aiml/johnson/Scenario/Scenario_Latest_for_cu_testing/testing_integration_tool_for_teep_for_cu.ipynb'

# New cu_input_values to replace (as a list)
# cu_input_values = ["187_cu_gnb_Active_gNBs", "188_cu_gnb_Active_gNBs", "189_cu_gnb_Active_gNBs", "190_cu_gnb_Active_gNBs", "191_cu_gnb_Active_gNBs", "192_cu_gnb_Active_gNBs", "193_cu_gnb_Active_gNBs", "194_cu_gnb_Active_gNBs", "195_cu_gnb_Active_gNBs"]
json_path = base_dir / "cu_input_values.json"
cu_input_values = load_cu_input_values(json_path)

print(f"Loading cu_input_values from: {json_path}")
print(f"Loaded cu_input_values: {cu_input_values}")
print(f"length of cu_input_values: {len(cu_input_values)}")


cu_input_values_1 = cu_input_values[1:100]  # 前 100 個
cu_input_values_2 = cu_input_values[100:200]  # 接下來的 100 個
cu_input_values_3 = cu_input_values[200:]  # 剩餘部分


# Step 1: Loop over the cu_input_values array and execute the notebook for each value
start_time = time.time()
for cu_input_value in cu_input_values_1:
    # Define output path for the modified notebook (new file)
    output_notebook_path = f'/home/aiml/johnson/Scenario/Scenario_Latest_for_cu_testing/{cu_input_value}.ipynb'

    # Step 1: Replace cu_input_index and save as a new file
    modified_content = test_replace_cu_input_index(notebook_path, cu_input_value, output_notebook_path)

    # Step 2: Execute the modified notebook
    run_ipynb(output_notebook_path, output_notebook_path)
    print(f"Processed notebook for cu_input_value: {cu_input_value}")

end_time = time.time()
print(f"Total time taken for cu_input_values_1: {end_time - start_time} seconds")