import datasets
import pdb
from collections import defaultdict
import sys, os

OUTPUT_DIR = sys.argv[1]
SEP = " "

try:
    os.makedirs(OUTPUT_DIR)
except OSError as e:
    print(f"output directory {OUTPUT_DIR} already exists, please remove and run again")
    sys.exit(1)

data = datasets.load_dataset('conll2003')
data_out = defaultdict(dict)

for split in data:
    with open(os.path.join(OUTPUT_DIR, split), 'w') as f:

        words = data[split]['words']
        labels = data[split]['ner']
        output_string = ""
        for w, l in zip(words, labels):
            output_string += "\n".join([SEP.join((ww, ll)) for ww, ll in zip(w, l)])
            output_string += "\n\n"
        f.write(output_string)    

#pdb.set_trace()

#with open(os.path.join(OUTPUT_DIR, 'train.txt')) as f:
#    print("hey")
