import time
import requests
from pathlib import Path


# def read_string_file(path):
#     '''
#     Reads a protein sequence.
#     :param path: relative path of the sequence file
#     :return: the protein sequence as a string
#     '''
#     data_folder = Path.cwd() / "predict_peptide_binding/files" / path
#     # data_folder.write_text('asdfsdfasdfasd')
#
#     # with data_folder.open(mode='r') as file:
#     with open(data_folder, 'r') as file:
#         data = file.read()
#
#     return data


# def sliding_window_list(protein, window_length):
#     '''
#     Returns a list of subsequences taken from the given protein sequence using a sliding window.
#     :param protein: a protein sequence of type string
#     :param window_length: an integer, determines the length of subsequences extracted from the protein sequence
#     :return: a list of subsequences, each of length window_length
#     '''
#     a = protein
#     b = [a[i:i + window_length] for i in range(len(a) - window_length + 1)]
#     return b
#     # print(b)


# def predict_binding(pdb_code, pdb_chain, peptide_sequence):
#     '''
#     Calls an API from pepsite2 to predict peptide binding spot and strength. Some code adopted from:
#     https://stackoverflow.com/questions/12979760/wait-for-successful-response-from-api-call
#     :param pdb_code: taken from the protein db bank, string
#     :param pdb_chain: protein chain, string
#     :param peptide_sequence: query sequence, 5-10 letters, string
#     :return: binding predictions, sorted by binding strength, list
#     '''
#     response = ''
#
#     # Try to get the data and json.load it 5 times, then give up
#     tries = 5
#     while tries >= 0:
#
#         try:
#             url = \
#                 "http://pepsite2.russelllab.org/match?" \
#                 "pdb=" + pdb_code + \
#                 "&chain=" + pdb_chain + \
#                 "&ligand=" + peptide_sequence + \
#                 "&format=txt"
#             response = requests.get(url)
#
#             if response.text != '':
#                 break
#             elif tries == 0:
#                 # If we keep failing, raise the exception for the outer exception
#                 # handling to deal with
#                 raise requests.exceptions
#             else:
#                 # Wait a few seconds before retrying and hope the problem goes away
#                 print('predicting...')
#                 time.sleep(2)
#                 tries -= 1
#                 continue
#         except requests.exceptions.HTTPError as e:
#             print(e.response)
#         except requests.exceptions.InvalidURL as e:
#             print(e.response)
#
#     output_string = response.text
#     output_list = str.split(output_string, '\n')
#     scores_list = list(filter(lambda k: 'SCORE' in k, output_list))
#     ret = []
#     for line in scores_list:
#         row = line.split()
#         ret.append(row)
#
#     return ret
