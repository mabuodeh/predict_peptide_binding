import unittest

from predict_peptide_binding.peptide import Peptide


class PeptideClassTests(unittest.TestCase):
    def test_read_string_file(self):
        expected = '123123123123123123'
        peptide = Peptide('test_read.txt', path=True)
        actual = peptide.sequence

        self.assertEqual(expected, actual)

    def test_get_sliding_window_list(self):
        protein = 'abcdef'
        window_length = 3
        expected_seq_list = ['abc', 'bcd', 'cde', 'def']

        peptide = Peptide(protein)
        actual_seq_list = peptide.get_sliding_window_list(window_length)

        self.assertEqual(actual_seq_list, expected_seq_list)

        # protein = 'abcdef'
        # window_length = 2
        # expected_seq_list = ['ab', 'bc', 'cd', 'de', 'ef']
        # actual_seq_list = sliding_window_list(protein, window_length)
        #
        # self.assertEqual(actual_seq_list, expected_seq_list)
