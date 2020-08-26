# Predicting peptide binding

Based on <a href="www.google.com">Pepsite2</a>, 
predicts binding strength of a 

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

## Examples
Running with a peptide string:
```
python3 -m predict_peptide_binding -s GPAGPPGA 1eak D 10 3
```

Running with a peptide sequence file, ace2.txt:
```
python3 -m predict_peptide_binding -f ace2.txt 1eak D 10 3
```
