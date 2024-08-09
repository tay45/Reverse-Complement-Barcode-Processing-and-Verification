import random

def reverse_complement(seq):
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C',
                  'a': 't', 't': 'a', 'c': 'g', 'g': 'c'}
    return ''.join(complement[base] for base in reversed(seq))

def verify_random_reverse_complements(input_file, output_file, num_seqs=5):
    import gzip

    # Read all lines to get total count
    with gzip.open(input_file, 'rt') as infile:
        input_lines = infile.readlines()

    with gzip.open(output_file, 'rt') as outfile:
        output_lines = outfile.readlines()

    total_lines = len(input_lines)
    indices = random.sample(range(total_lines), num_seqs)

    for i in indices:
        input_seq = input_lines[i].strip()
        output_seq = output_lines[i].strip()
        if reverse_complement(input_seq) != output_seq:
            print("Error: Sequence {} does not match its reverse complement {}".format(input_seq, output_seq))
            return False
        else:
            print("Verified: {} -> {}".format(input_seq, output_seq))
    return True

input_file = 'input_sequences.txt.gz'
output_file = 'input_sequences-REVERSE-COMPLEMENTED.txt.gz'

if verify_random_reverse_complements(input_file, output_file):
    print("All sequences verified successfully.")
else:
    print("There were errors in the sequences.")


