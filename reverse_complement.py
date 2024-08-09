def reverse_complement(seq):
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C',
                  'a': 't', 't': 'a', 'c': 'g', 'g': 'c'}
    return ''.join(complement[base] for base in reversed(seq))

def process_barcode_file(input_file, output_file):
    import gzip

    with gzip.open(input_file, 'rt') as infile, gzip.open(output_file, 'wt') as outfile:
        for line in infile:
            barcode = line.strip()
            rev_comp_barcode = reverse_complement(barcode)
            outfile.write(rev_comp_barcode + '\n')

input_file = 'input_sequences.txt.gz'
output_file = 'input_sequences-REVERSE-COMPLEMENTED.txt.gz'

process_barcode_file(input_file, output_file)
