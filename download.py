import csv
import subprocess


with open('./allpdf.tsv', encoding='utf-8', newline='') as f:
    for cols in csv.reader(f, delimiter='\t'):
        res = subprocess.call(['curl', '-o', './pdf/' + cols[1] + '.pdf', 'https://www.uec.ac.jp' + cols[0]])
