import time
import pandas as pd
import requests


class ProteinStructure:
    def __init__(self, pdb_code, pdb_chain):
        self.pdb_code = pdb_code
        self.pdb_chain = pdb_chain

    def predict_peptide_binding(self, peptide_sequence):
        """Calls an API from pepsite2 to predict peptide binding spot and strength. Some code adopted from:
        https://stackoverflow.com/questions/12979760/wait-for-successful-response-from-api-call

        Parameters
        ----------
        peptide_sequence: str
            Query sequence, 5-10 letters

        Returns
        -------
        binding predictions: list
            Predictions of binding strength, sorted by score
        """
        print('Predicting the binding of', peptide_sequence)
        response = ''

        # Try to get the data and json.load it 5 times, then give up
        tries = 5
        while tries >= 0:

            try:
                url = \
                    "http://pepsite2.russelllab.org/match?" \
                    "pdb=" + self.pdb_code + \
                    "&chain=" + self.pdb_chain + \
                    "&ligand=" + peptide_sequence + \
                    "&format=txt"
                response = requests.get(url)

                if response.text != '':
                    break
                elif tries == 0:
                    # If we keep failing, raise the exception for the outer exception
                    # handling to deal with
                    raise requests.exceptions
                else:
                    # Wait a few seconds before retrying and hope the problem goes away
                    print('predicting...')
                    time.sleep(2)
                    tries -= 1
                    continue
            except requests.exceptions.HTTPError as e:
                print(e.response)
            except requests.exceptions.InvalidURL as e:
                print(e.response)

        output_string = response.text
        output_list = str.split(output_string, '\n')
        scores_list = list(filter(lambda k: 'SCORE' in k, output_list))
        ret = []
        for line in scores_list:
            row = line.split()
            ret.append(row)

        return ret

    def predict_peptide_binding_list(self, peptide_sequence_list):
        """Predicts peptide binding spot and strength for each peptide in a list.

        Parameters
        ----------
        peptide_sequence_list: list
            List of query peptide strings, 5-10 letters each

        Returns
        -------
        list
            Binding prediction list for each query peptide, sorted by binding strength
        """
        binding_strength_list = []

        for peptide in peptide_sequence_list:
            binding_prediction = self.predict_peptide_binding(peptide)
            binding_strength_list.append(binding_prediction)

        return binding_strength_list

    def get_copyright_info(self, peptide_sequence):
        response = ''

        # Try to get the data and json.load it 5 times, then give up
        tries = 5
        while tries >= 0:

            try:
                url = \
                    "http://pepsite2.russelllab.org/match?" \
                    "pdb=" + self.pdb_code + \
                    "&chain=" + self.pdb_chain + \
                    "&ligand=" + peptide_sequence + \
                    "&format=txt"
                response = requests.get(url)

                if response.text != '':
                    break
                elif tries == 0:
                    # If we keep failing, raise the exception for the outer exception
                    # handling to deal with
                    raise requests.exceptions
                else:
                    # Wait a few seconds before retrying and hope the problem goes away
                    print('predicting...')
                    time.sleep(2)
                    tries -= 1
                    continue
            except requests.exceptions.HTTPError as e:
                print(e.response)
            except requests.exceptions.InvalidURL as e:
                print(e.response)

        output_string = response.text
        output_list = str.split(output_string, '\n')
        copyright_list = list(filter(lambda k: '#' in k, output_list))
        ret = []
        for line in copyright_list:
            # row = line.split()
            ret.append(line.split('#')[1].lstrip())

        return ret
