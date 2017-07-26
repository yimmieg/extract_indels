import pysam

def extract_reads(options):
    n = get_names(options.names)
    bamfile = pysam.AlignmentFile(options.bam, 'rb')

    for read in bamfile.fetch():
     if read.is_paired:
         if( not( read.is_unmapped ) ):   #if it's mapped
            cigarLine=read.cigar;
            for (cigarType,cigarLength) in cigarLine:
               try:
                   if(  cigarType == 0): #match
               elif(cigarType == 1 || cigarType == 2): #insertions
                mate <- bamfile.mate(read)
               .write(read)
                   elif(cigarType == 2): #deletion
                   elif(cigarType == 3): #skip
                   elif(cigarType == 4): #soft clipping
                   elif(cigarType == 5): #hard clipping
                   elif(cigarType == 6): #padding
                   else:
                       print "Wrong CIGAR number";
                       sys.exit(1);
               except:
                   print "Problem";

         if
             pairedreads.write(read)

    pairedreads.close()

    name_indexed = pysam.IndexedReads(bamfile)
    name_indexed.build()
    header = bamfile.header.copy()
    out = pysam.Samfile(options.out, 'wb', header=header)
    for name in n:
        try:
            name_indexed.find(name)
        except KeyError:
            pass
        else:
            iterator = name_indexed.find(name)
            for x in iterator:
                out.write(x)




for read in samfile.fetch():
     if read.is_paired:
             pairedreads.write(read)

pairedreads.close()
samfile.close()

for read in samfile.fetch('chr1', 100, 120):
     print read

samfile.close()

if __name__ == "__main__":
    from argparse import ArgumentParser

    parser = ArgumentParser(description='Extract reads containing indels')
    parser.add_argument('-i', '--in', help='bam file', required=True)
    parser.add_argument('-o', '--out', help='bam file output containg indels', required=True)
    options = parser.parse_args()
    extract_reads(options)
