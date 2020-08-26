from pathlib import Path


class Peptide:
    def __init__(self, peptide, path=False):
        if path:
            self.path = peptide
            data_folder = Path.cwd() / self.path
            # data_folder = Path.cwd() / "predict_peptide_binding/files" / self.path
            # data_folder.write_text('asdfsdfasdfasd')

            # with data_folder.open(mode='r') as file:
            with open(data_folder, 'r') as file:
                data = file.read()

            self.sequence = data
        else:
            self.path = None
            self.sequence = peptide

    def get_sequence(self):
        """Getter, provides the peptide sequence

        Returns
        -------
        str
            Peptide sequence
        """
        return self.sequence

    def get_sliding_window_list(self, window_length):
        """Returns a list of subsequences taken from the given protein sequence using a sliding window.

        Parameters
        ----------
        window_length: int
            Determines the length of subsequences extracted from the protein sequence

        Returns
        -------
        list
            A list of subsequences, each of length window_length
        """

        a = self.sequence
        b = [a[i:i + window_length] for i in range(len(a) - window_length + 1)]
        return b
        # print(b)
