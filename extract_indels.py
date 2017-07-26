import pysam

def extract_reads(options):
    bamfile = pysam.AlignmentFile(options.input, 'rb')
    header = bamfile.header.copy()
    out = pysam.Samfile(options.output, 'wb', header=header)

    for read in bamfile.fetch():
        if read.is_paired:
            if( not( read.is_unmapped ) and not (read.mate_is_unmapped ) ):
                if(read.cigarstring.find("I") != -1 or read.cigarstring.find("D") != -1):
                    mate = bamfile.mate(read)
                        if (read.tid == mate.tid) :
                            out.write(read)
                            out.write(mate)

    bamfile.close()
    out.close()

if __name__ == "__main__":
    from argparse import ArgumentParser

    parser = ArgumentParser(description='Extract reads containing indels')
    parser.add_argument('-i', '--input', help='bam file', required=True)
    parser.add_argument('-o', '--output', help='bam file output containg indels', required=True)
    options = parser.parse_args()
    extract_reads(options)
