import itertools
import random

# bash command for creating kmer counts with bbtools
#/kmercountexact.sh in=NC_002640.1.fasta k=11 out= NC_002640.1.k11.txt fastadump=f

# define utility functions
def rev_compl(st: str) -> str:
    nn = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
    return "".join(nn[n] for n in reversed(st))

def create_unique_kmer(kmer: str) ->str:
    rckmer = rev_compl(kmer)
    if kmer >= rckmer:
        return kmer
    else:
        return rckmer

def iterate_kmers(k: int):
    bases = ['A','C','T','G']
    kmers = [''.join(p) for p in itertools.product(bases, repeat=k)]
    unique_kmers = set(map(create_unique_kmer, kmers))
    return unique_kmers

def import_bbtools_kmers(filename: str) -> list:
    kmers = []
    with open(filename, 'r') as fly:
        for line in fly:
            kmers.append(line.strip().split()[0])
    return kmers


# k=13 kmer analysis #

# process kmers from fly genome
flymers = import_bbtools_kmers("fly_13mers.txt")
unique_flymers = set(flymers) # 30869191

# create set of all possible unique 13-kmers
unique_kmers = iterate_kmers(13) # 33554432

# find kmers not in the fly genome
unique_kmers_no_fly = unique_kmers.difference(unique_flymers) #2685241

# select  10,000 random kmers not in the flu genome

uknf = list( unique_kmers_no_fly)
# Twist biosciences Tier 6 oligos 6k-12k cost $3120
rand10k =set(random.choices(uknf, k=10000))

# test how many of these kmers appear in the  Denv4 genome
denv4 = set(import_bbtools_kmers("NC_002640.1.k13.txt"))
kmersindenv4 = rand10k.intersection(denv4)
print(len(kmersindenv4)) # 0 at 10k, 8 at 100k

#test how many kmers are in brucella suis

bsuis = set(import_bbtools_kmers("Bsuis_1330.k13.txt"))
kmersinbsuis = rand10k.intersection(bsuis)
print(len(kmersinbsuis)) # 1127

# K=12 analysis

# process kmers from fly genome
flymers = import_bbtools_kmers("fly_12mers.txt")
unique_flymers = set(flymers) #  8343900
print(len(unique_flymers))

# create set of all possible unique 12-kmers
unique_kmers = iterate_kmers(12) #
print(len(unique_kmers)) # 8390656
# find kmers not in the fly genome
unique_kmers_no_fly = unique_kmers.difference(unique_flymers) #
print(len(unique_kmers_no_fly)) # 46756
# select  10,000 random kmers not in the fly genome

uknf = list( unique_kmers_no_fly)
# Twist biosciences Tier 6 oligos 6k-12k cost $3120
random.seed(10)
rand10k =set(random.choices(uknf, k=10000))

# test how many of these kmers appear in the  Denv4 genome
denv4 = set(import_bbtools_kmers("NC_002640.1.k12.txt"))
kmersindenv4 = rand10k.intersection(denv4)
print(len(kmersindenv4)) # 1 could the rna virus quasispecies make detection easier?

#test how many kmers are in brucella suis
 #genome size ratio
 #651000000/ 3315810 =  196.3

 # 12-kmer ratio
#  8343900/ 2001517 = 4.2

bsuis = set(import_bbtools_kmers("Bsuis_1330.k12.txt")) # 2001517
kmersinbsuis = rand10k.intersection(bsuis)
print(len(kmersinbsuis)) # 6501


# K=11 analysis

# process kmers from fly genome
flymers = import_bbtools_kmers("fly_11mers.txt")
unique_flymers = set(flymers)
len(unique_flymers) # 2097017

# create set of all possible unique 13-kmers
unique_kmers = iterate_kmers(11)
len(unique_kmers) # 2097152

# find kmers not in the fly genome
len(unique_kmers_no_fly) #135

 #135 is too few to be useful.
