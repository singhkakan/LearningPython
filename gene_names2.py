#!/usr/bin/python

import sys
import fileinput
import re
import json

GN, CHR, SP, EP = [], [], [], []

Gene_list={}

myfile = sys.argv[0]
count = 0
for line in fileinput.input(['/home/singhkak/assignment3/data/Homo_sapiens.GRCh37.75.gtf']):
    if re.match (r'.*\t.*\tgene\t', line):
        gene_name = re.findall('gene_name \"(.*?)\";', line)
        chromosome = re.findall('^(.*?)\t', line)
        start_pos = re.findall('\tgene\t(.*?)\t', line)
        end_pos = re.findall('\tgene\t\d+\t(.*?)\t\.', line)
        count = count + 1
        Gene_list[str(gene_name)] = {"chr" : str(chromosome), "startPos" : str(start_pos), "endPos" : str(end_pos)}
        GN.append(gene_name)
        CHR.append(chromosome)
        SP.append(start_pos)
        EP.append(end_pos)

json_GeneList = json.dumps(Gene_list, indent =4, sort_keys =True, separators = (', ', ': '))

print json_GeneList
print "There are {} genes in this data set".format(count)

