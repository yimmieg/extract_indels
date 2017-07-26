import pysam

def extract_reads(options):
    n = get_names(options.names)
    bamfile = pysam.AlignmentFile(options.bam, 'rb')
    header = bamfile.header.copy()
    out = pysam.Samfile(options.out, 'wb', header=header)

    for read in bamfile.fetch():
        if read.is_paired:
            if(read.cigarstring.find("I") or read.cigarstring.find("D")):
                mate <- bamfile.mate(read)
                out.write(read)
                out.write(mate)

    bamfile.close()
    out.close()

if __name__ == "__main__":
    from argparse import ArgumentParser

    parser = ArgumentParser(description='Extract reads containing indels')
    parser.add_argument('-i', '--in', help='bam file', required=True)
    parser.add_argument('-o', '--out', help='bam file output containg indels', required=True)
    options = parser.parse_args()
    extract_reads(options)
