"""
Author: https://github.com/kataksk/convert_gff_id 
"""

import sys

prefix = sys.argv[1]
gff_in = sys.argv[2]

# prefix = "TO"
# gff_in = "/work2/yuka97524/Temma/26EVM/EVM.all.gff3"

count = 0

with open(gff_in, 'r') as f:
    for line in f:
        line_list = line.rstrip().split('\t')
        # print(line_list)
        if line_list[0] == '':
            print()
            count += 1
        else:
            if line_list[2] == 'gene':
                line_list[8] = 'ID=' + str(prefix) + '.' + str(count) + ';Name=' + str(prefix) + '.' + str(count)
                out = '\t'.join(line_list)
                print(out)
            elif line_list[2] == 'mRNA':
                line_list[8] = 'ID=' + str(prefix) + '.' + str(count) + ';Parent=' + str(prefix) + '.' + str(count) + ';Name=' + str(prefix) + '.' + str(count)
                out = '\t'.join(line_list)
                print(out)
            elif line_list[2] == 'exon' or line_list[2] == 'CDS':
                line_list[8] = 'ID=' + str(prefix) + '.' + str(count) + ';Parent=' + str(prefix) + '.' + str(count)
                out = '\t'.join(line_list)
                print(out)
        
            # elif line_list[2] == 'mRNA':
            #     line_list_attribute = line_list[8].split(';')
            #     print(line_list_attribute[0])
