from efsa_parser import EfsaResults, find_all_efsa_outptus
import os

if __name__ == "__main__":

    efsa_output_directoy = "efsa_outputs"

    # create dict of efsa output directories with subdirectories

    efsa_outputs, empty_directories = find_all_efsa_outptus(efsa_output_directoy)
    output_file = "merged_results.xlsx"
    outputs_directory = "EFSA_output"

    results = EfsaResults(efsa_outputs, outputs_directory, output_file, log=False)
    results.parse_all_results()
    results.merge_output()
