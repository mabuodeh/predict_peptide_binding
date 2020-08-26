import unittest
from predict_peptide_binding.protein import ProteinStructure


class ProteinClassTests(unittest.TestCase):

    def setUp(self):
        pdb_code = "1eak"
        pdb_chain = "D"

        self.protein = ProteinStructure(pdb_code, pdb_chain)
        # self.peptide = Peptide('test_read.txt')

    def test_predict_binding(self):
        peptide_sequence = "GPAGPPGA"

        pred_list = self.protein.predict_peptide_binding(peptide_sequence)
        # print(pred_list)
        # input('')
        # print('end')

        self.assertIn('pro-2', ''.join(pred_list[0]))
        self.assertIn('ala-3', ''.join(pred_list[0]))
        self.assertIn('ala-8', ''.join(pred_list[0]))
        self.assertIn('gly-7', ''.join(pred_list[0]))

        self.assertNotIn('pro-2', ''.join(pred_list[1]))
        self.assertIn('ala-3', ''.join(pred_list[1]))
        self.assertIn('pro-5', ''.join(pred_list[1]))
        self.assertNotIn('gly-7', ''.join(pred_list[1]))

    def test_predict_peptide_binding_list(self):
        peptide_sequence_list = ["GPAGPPGA", "GPAGPPGG", "GPAGPPGA"]

        pred_list_of_lists = self.protein.predict_peptide_binding_list(peptide_sequence_list)

        self.assertIn('pro-2', ''.join(pred_list_of_lists[0][0]))
        self.assertIn('ala-3', ''.join(pred_list_of_lists[0][0]))
        self.assertIn('ala-8', ''.join(pred_list_of_lists[0][0]))
        self.assertIn('gly-7', ''.join(pred_list_of_lists[0][0]))

        self.assertIn('ala-3', ''.join(pred_list_of_lists[1][0]))
        self.assertIn('pro-5', ''.join(pred_list_of_lists[1][0]))
        self.assertIn('pro-6', ''.join(pred_list_of_lists[1][0]))
        self.assertNotIn('ala-8', ''.join(pred_list_of_lists[1][0]))
        self.assertNotIn('gly-7', ''.join(pred_list_of_lists[1][0]))

        self.assertIn('pro-2', ''.join(pred_list_of_lists[2][0]))
        self.assertIn('ala-3', ''.join(pred_list_of_lists[2][0]))
        self.assertIn('ala-8', ''.join(pred_list_of_lists[2][0]))
        self.assertIn('gly-7', ''.join(pred_list_of_lists[2][0]))
