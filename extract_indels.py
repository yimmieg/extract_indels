import pysam

def extract_reads(options):
    n = get_names(options.names)
    bamfile = pysam.AlignmentFile(options.bam, 'rb')
    header = bamfile.header.copy()
    out = pysam.Samfile(options.out, 'wb', header=header)

    for read in bamfile.fetch():
        if read.is_paired:
            if( not( read.is_unmapped ) ):   #if it's mapped
                cigarLine=read.cigar;
            for (cigarType,cigarLength) in cigarLine:
               try:
                   if(cigarType == 0): #match
                    elif(cigarType == 1 or cigarType == 2): #insertions
                        mate <- bamfile.mate(read)
                        out.write(read)
                        out.write(mate)
                    ##elif(cigarType == 2): #deletion
                    elif(cigarType == 3): #skip
                    elif(cigarType == 4): #soft clipping
                    elif(cigarType == 5): #hard clipping
                    elif(cigarType == 6): #padding
                    else:
                       print "Wrong CIGAR number";
                       sys.exit(1);
               except:
                   print "Problem";

bamfile.close()
out.close()

if __name__ == "__main__":
    from argparse import ArgumentParser

    parser = ArgumentParser(description='Extract reads containing indels')
    parser.add_argument('-i', '--in', help='bam file', required=True)
    parser.add_argument('-o', '--out', help='bam file output containg indels', required=True)
    options = parser.parse_args()
    extract_reads(options)
