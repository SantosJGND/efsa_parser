## Efsa Parser

Script to parse EFSA pipeline output.

### Usage

```python

from efsa_parser import EfsaResults

dir_to_sample= {
    "sample1": "/home/bioinf/Desktop/INSA/OTHER/EFSA_output/friendly_waddington",
    "sample2": "/home/bioinf/Desktop/INSA/OTHER/EFSA_output/friendly_waddington2"
}

output_file= "/home/bioinf/Desktop/INSA/OTHER/EFSA_output/merged_results.xlsx"
outputs_directory= "/home/bioinf/Desktop/INSA/OTHER/EFSA_output"

results= EfsaResults(dir_to_sample, outputs_directory, output_file)
results.parse_all_results()
results.merge_output()

```
