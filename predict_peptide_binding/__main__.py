# from predict_peptide_binding.dev.binding import read_string_file, sliding_window_list, predict_binding
# from predict_peptide_binding.dev.save_to_excel import to_df, store_in_xlsx
import sys

from pandas import DataFrame

from predict_peptide_binding.df import to_df, store_in_xlsx
from predict_peptide_binding.peptide import Peptide
from predict_peptide_binding.protein import ProteinStructure


def main():
    if len(sys.argv) > 7:
        exit('Too many arguments provided! Expected 6-7, received ' + str(len(sys.argv)) + '.')

    peptide_src_type = sys.argv[1]
    peptide = sys.argv[2]
    pdb_code = sys.argv[3]
    pdb_chain = sys.argv[4]
    window_length = int(sys.argv[5])
    score_count = 10
    if len(sys.argv) == 7:
        score_count = int(sys.argv[6])

    file_output = 'binding_predictions.xlsx'

    protein = ProteinStructure(pdb_code, pdb_chain)
    if peptide_src_type == '-s':
        peptide = Peptide(peptide=peptide)
    elif peptide_src_type == '-f':
        peptide = Peptide(peptide, True)
        if len(peptide.get_sequence()) < window_length:
            exit('window length is less than sequence length! Exiting')

    # pred = protein.predict_peptide_binding(peptide.get_sequence())
    # df = df.append(other=to_df(pred, 6))
    df = DataFrame()
    copyright_sequence = ''
    if peptide_src_type == '-s':
        pred = protein.predict_peptide_binding(peptide.get_sequence())
        df = df.append(other=to_df(pred, score_count))
        copyright_sequence = peptide.get_sequence()
    elif peptide_src_type == '-f':
        pep_list = peptide.get_sliding_window_list(window_length=window_length)
        for pep in pep_list:
            pred = protein.predict_peptide_binding(pep)
            df = df.append(other=to_df(pred, score_count))
        copyright_sequence = pep_list[0]

    copyright_info = protein.get_copyright_info(copyright_sequence)

    print('All peptides successfully predicted! Results stored in', file_output)
    store_in_xlsx(file_output, df, copyright_info)


if __name__ == "__main__":
    main()
