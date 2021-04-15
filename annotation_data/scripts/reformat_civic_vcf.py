import sys


def get_reformatted_civic_vcf(ivcf):
    # read and modify header lines
    for line in ivcf:
        if line[:2] == '##':
            if line[:7] != '##INFO=':
                yield line.strip('\n\r')
        elif line[:1] == '#':
            yield '##INFO=<ID=CVU,Number=1,Type=String,Description="CIViC Variant URL">'
            yield line.strip('\n\r')
            break
    # read and modify variant records
    for line in ivcf:
        fields = line.split('\t')
        fields[7] = 'CVU=https://civic.genome.wustl.edu/links/variants/' \
                    + fields[2]
        yield '\t'.join(fields)


if __name__ == '__main__':
    with open(sys.argv[1]) as ivcf:
        for reformatted_line in get_reformatted_civic_vcf(ivcf):
            print(reformatted_line)
