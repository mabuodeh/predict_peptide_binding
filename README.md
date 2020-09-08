# Predicting peptide binding

<p>This package uses an API from <a href="http://pepsite2.russelllab.org/">PepSite2</a>, 
which "can predict binding of a given peptide onto a protein structure".</p>

<p>
The API provided by PepSite is limited to only one peptide sequence.
This package allows the researcher to give a full protein sequence,
split it into a list of peptide sequences, returning the predictions
for each sequence.
</p>

<p>
The researcher also has the ability to choose the peptide sequence size,
as well as the number of binding scores returned per prediction.
</p>

<p>
This package gives added functionality to the base PepSite, but to use
results, <b>please cite the original paper</b>:<br>
<em>PepSite: prediction of peptide-binding sites from protein surfaces.<br>
Trabuco LG, Lise S, Petsalaki E, and Russell RB.<br>
Nucleic Acids Res. 2012; 40(Web Server issue):W423-426.</em>
</p>

### Usage

run predict_peptide_binding, passing the following arguments:
```
- peptide_src_type: if the peptide is a file or a string.
- peptide: provide path (if file) or the peptide string.
- pdb_code: such as 1eak.
- pdb_chain: such as D.
- window_length: splits the peptide sequence into 
                    subsequences of size window_length. 
                    Required if peptide_src_type is a file 
                    (-f).
- [score_count]: optional, returns the top scores 
                    rather than all scores of the 
                    prediction. Default is 10. 
```
Currently, the sliding window only works when providing 
the peptide sequence in file format, and the sequence 
length must be greater than the window_length provided.

### Examples
Running with a peptide string:
```
python3 -m predict_peptide_binding -s GPAGPPGA 1eak D 10 3
```

Running with a peptide sequence file, ace2.txt:
```
python3 -m predict_peptide_binding -f ace2.txt 1eak D 10 3
```
