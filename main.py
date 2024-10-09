from efsa_parser import EfsaResults
import os

def find_efsa_output(sample_dir: str) -> str:
    """
    Find the efsa output directory in the sample directory
    """
    for root, dirs, files in os.walk(sample_dir):
        for dir in dirs:
            if not dir.startswith('work'):
                return os.path.join(root, dir)
    return None

def find_all_efsa_outptus(efsa_output_directoy: str) -> dict:

    efsa_outputs = os.listdir(efsa_output_directoy)
    efsa_outputs = {
        output: os.path.join(efsa_output_directoy, output) for output in efsa_outputs
    }
    efsa_outputs= {
        output: find_efsa_output(efsa_outputs[output]) for output in efsa_outputs
    }

    empty_outputs = [
        output for output in efsa_outputs if efsa_outputs[output] is None
    ]
    efsa_outputs = {
        output: efsa_outputs[output] for output in efsa_outputs if output not in empty_outputs
    }

    return efsa_outputs, empty_outputs

if __name__ == '__main__':

    efsa_output_directoy= 'test_data/efsa_outputs'
    
    # create dict of efsa output directories with subdirectories

    efsa_outputs, empty_directories= find_all_efsa_outptus(efsa_output_directoy)
    output_file= "merged_results.xlsx"
    outputs_directory= "EFSA_output"

    results= EfsaResults(efsa_outputs, outputs_directory, output_file)
    results.parse_all_results()
    results.merge_output()
