import pandas as pd
import re
import os

intron_id = input("Enter the number of novel intron: ")
intron_id_index = (int(intron_id)-1)

with open('data/splices.csv', 'r') as f:
    splices = pd.read_csv(f, skiprows=intron_id_index, nrows=1)

chromosome = splices.iat[0, 2]
first_base = int(splices.iat[0, 3])
last_base = int(splices.iat[0, 4])
print("Novel intron " + str(intron_id) + "\n" + chromosome + ": " + str(first_base) + ".." + str(last_base))

with open("data/ncbi/GCF_000001895.5/{}.fna".format(chromosome), "r") as f:
    chromosome_sequence = f.read().replace("\n", "")
print("Chromosome", chromosome, "sequence loaded")

five_sequence = chromosome_sequence[(first_base-150):first_base]
three_sequence = chromosome_sequence[(last_base+1):(last_base+151)]
complete_sequence = five_sequence + three_sequence
complete_sequence_broken = re.sub("(.{81})", "\\1\n", complete_sequence, 0, re.DOTALL)

if not os.path.exists("fasta_archive"):
    os.mkdir("fasta_archive")

fasta = open("fasta_archive/{}.fasta".format(intron_id), "x")
fasta.write(">" + chromosome + " Rattus norvegicus, Rnor_6.0\n" + complete_sequence_broken + "\n")
fasta.close()
print("{}.fasta".format(intron_id) + " created in `~/primer-automation/fasta_archive`")