#!/usr/bin/python

import sys
import fileinput
import re
import json

GN, CHR, SP, EP = [], [], [], []

Hene_list = {}

myfile = sys.argv[0]
count = 0
for line in fileinput.input(['/home/singhkak/assignment3/data/Homo_sapiens.GRCh37.75.gtf']):
    if re.match (r'.*\t.*\tgene\t', line):
        gene_name = re.findall('gene_name \"(.*?)\";', line)
        chromosome = re.findall('^..', line)
        start_pos = re.findall('\tgene\t(.*?)\t', line)
        end_pos = re.findall('\tgene\t\d+\t(.*?)\t\.', line)
        count = count + 1
        Gene_list = {"geneName" : gene_name, "chr" : chromosome, "startPos" : start_pos, "endPos" : end_pos}
        print Gene_list
        GN.append(gene_name)
        CHR.append(chromosome)
        SP.append(start_pos)
        EP.append(end_pos)

print "There are {} genes in this data set".format(count)
print type(chromosome)

