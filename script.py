import pandas as pd
import re
import os
import sys

def menu():
    print("\n1) Create novel exon sequence from splice database\n2) Create one piece sequence of rat genome\n3) Exit")
    selection = input("Selection: ")

    if selection=='1':
        novel_seq()

    elif selection=='2':
        straight_seq()

    elif selection=='3':
        sys.exit(0)

    else:
        print("Improper entry")
        menu()


def novel_seq():
    intron_id = int(input("Enter the novel intron number (from firstPass): "))
    bases_left = int(input("Enter the number of bases to the left of intron start you'd like to go: "))
    bases_right = int(input("Enter the number of bases to the right of intron end you'd like to go: "))

    for i in range(50):
        print("-", end="")

    with open('data/firstPass_min.csv', 'r') as f:
        splices = pd.read_csv(f)

    row = splices.loc[splices['X'] == intron_id]
    chromosome = row.iat[0, 1]
    first_base = int(row.iat[0, 2])
    last_base = int(row.iat[0, 3])
    print("\nNovel intron " + str(intron_id) + "\n" + chromosome + ": " + str(first_base) + ".." + str(last_base))

    with open("data/ncbi/GCF_000001895.5/{}.fna".format(chromosome), "r") as f:
        chromosome_sequence = f.read().replace("\n", "")
    print("Chromosome", chromosome, "sequence loaded")

    five_sequence = chromosome_sequence[(first_base-bases_left):first_base]
    three_sequence = chromosome_sequence[(last_base+1):(last_base+bases_right+1)]
    complete_sequence = five_sequence + three_sequence
    complete_sequence_broken = re.sub("(.{81})", "\\1\n", complete_sequence, 0, re.DOTALL)
    print("Proposed exon sequence length:", len(complete_sequence))

    if not os.path.exists("fasta_archive"):
        os.mkdir("fasta_archive")

    fasta = open("fasta_archive/{}.fasta".format(intron_id), "x")
    fasta.write(">" + chromosome + " Rattus norvegicus, Rnor_6.0\n" + complete_sequence_broken + "\n")
    fasta.close()
    print("{}.fasta".format(intron_id) + " created in `~/primer-automation/fasta_archive`")

    menu()

def straight_seq():
    chromosome = input('Enter rn6 chromosome RefSeq (NC_XXXXXX.4): ')
    first = int(input('Enter first base of sequence: '))
    last = int(input('Enter last base of sequence: '))

    try:
        with open("data/ncbi/GCF_000001895.5/{}.fna".format(chromosome), "r") as f:
            chromosome_sequence = f.read().replace("\n", "")
        print("Chromosome", chromosome, "sequence loaded")

    except:
        print('Chromosome RefSeq was entered incorrectly. Try again')
        straight_seq()

    sequence = chromosome_sequence[first:(last+1)]
    print("Sequence length:", len(sequence))

    fasta = open("fasta_archive/rn6_{}_{}_{}.fasta".format(chromosome, first, last), "x")
    fasta.write(">" + chromosome + " Rattus norvegicus, Rnor_6.0:" + str(first) + ".." + str(last) + "\n" + sequence + "\n")
    fasta.close()
    print("rn6_NC{}_{}_{}.fasta created in `~/primer-automation/fasta_archive`".format(chromosome[3:], first, last))

    menu()

if __name__ == '__main__':
    menu()