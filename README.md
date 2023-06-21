# Overview of project

A lot of microbiology relies on metagenomic sequencing of bacteria and viruses from animal and plant hosts. Metagenomics is when you extract DNA 
from a mixed sample of organisms and sequence it all together.  One big challenge is that often the Host animal DNA  makes up almost all of the 
sample and you don’t get sequences from the bacteria and viruses you are interested in.  There are existing solutions that try to deal with this 
but all have some disadvantages.  They basically fall into two areas, removing the host DNA you don’t want or selecting the non-host DNA you do 
want.
 
An idea I’ve been toying around with is the idea of designing a pool of short oligonucleotide probes that do not bind to the host but do bind to 
distantly rated organisms.   Existing methods use long 40-60 nt high-specificity oligonucleotides. At kmer lengths (a kmer is a short overlapping 
DNA sequence) of  around of around 14-15 about half of the possible kmers are in the host genome of  the house fly in our experiments.

|k  |kmers in genome|Total Unique kmers|Available kmers|fraction of possible kmers|
|---|---------------|------------------|---------------|--------------------------|
|9  |1.311E+05      |1.313E+05         |2.56E+02       |0.998                     |
|10 |5.248E+05      |5.243E+05         |-5.12E+02      |1.001                     |
|11 |2.097E+06      |2.098E+06         |1.16E+03       |0.999                     |
|12 |8.344E+06      |8.389E+06         |4.47E+04       |0.995                     |
|13 |3.087E+07      |3.356E+07         |2.69E+06       |0.920                     |
|14 |8.872E+07      |1.342E+08         |4.55E+07       |0.661                     |
|15 |1.785E+08      |5.369E+08         |3.58E+08       |0.333                     |

If we take that list of excluded available kmers we can create probes from that list  to capture the dna of other organisms. This approach takes 
advantage of the math of the Birthday problem https://en.wikipedia.org/wiki/Birthday_problem or more generally the probability of independent 
events to randomly grab a small fraction of reads containing kmers from all non-host .
 
The genomes of the non-host organisms are smaller 10^4  to 10^7, but with 10^4  probes which is a reasonable number to synthesize with pooled oligo 
technology probability of capturing tens to  hundreds of sequences per organism is good.  This could be modeled with  a cumulative binomial 
function. 
 
This is also easy to test empirically by exporting the kmers from the host genome,  finding the missing kmers, then looking for those in target 
non-host organisms.

# Other ideas

* Sort kmers by abundance and create shorter kmers tha are allowed to hit some host signletons but not kmers in high abundance in the host
* use  kmercountexact for routine kmer counting https://sourceforge.net/projects/bbmap/

