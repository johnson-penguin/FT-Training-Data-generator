## Flow chart
![LLM-cu_ft_data_gen drawio](https://github.com/user-attachments/assets/44bb6ed4-60b4-403f-ad0c-a42911567c4f)

## 1. `cu_input_values.json`
This is a configuration list file, with the following format:
```bash=
{
  "cu_input_values": [
    "0_cu_gnb_original",
    "1_cu_gnb_remote_s_portd",
    ...
    "296_cu_gnb_SCTP_OUTSTREAMS"
  ]
}
```
- It provides an array of parameter names, where each name represents a specific configuration variant for a test execution.
- Each entry corresponds to a specific .conf configuration file and .log output file.

## 2. `gen_training_data_generator.py`
This is an automated batch processing script that generates and executes multiple Jupyter Notebooks based on the parameter list defined in `cu_input_values.json`, and records the results.

Its main functions are as follows:
- Load values from `cu_input_values.json`:
```bash=
cu_input_values = load_cu_input_values(json_path)
```  
- For each `cu_input_value`:
   - Copy and modify the `cu_input_index` variable inside the `.ipynb file` (this variable specifies the target parameter to be tested).
   - Save it as a new Notebook, e.g., `187_cu_gnb_Active_gNBs.ipynb`.
   - Execute the notebook using `jupyter nbconvert` to produce the corresponding result and log files.
- This process is repeated (for the first 100 items, by default) to build a dataset for training or analysis purposes.

## 3. `testing_integration_tool_for_teep_for_cu.ipynb`
This is a ***Jupyter Notebook used for integration testing and data generation.***

For each test case specified by `cu_input_index`, the notebook:
- Loads the corresponding configuration file (e.g., `187_cu_gnb_Active_gNBs.conf`)
- Loads the associated log file (e.g., `187_cu_gnb_Active_gNBs_log.txt`)
- Optionally uses external references such as `reference_config.txt` and `debug.yaml`
- Performs automatic validation and analysis
- Outputs the result in a structured format, which can be used for supervised fine-tuning (SFT) or debugging datasets

The notebook acts as the core execution and reasoning unit, generating training examples based on configuration correctness, error logs, and parameter behavior.
