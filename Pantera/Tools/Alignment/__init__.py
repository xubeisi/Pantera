__author__ = 'mahajrod'

from Pantera.Tools.Alignment.BWA import BWA
from Pantera.Tools.Alignment.BLAT import BLAT

from Pantera.Tools.Alignment.STAR import STAR


max_threads = 4
bowtie2_path = ""
bwa_path = ""
novoalign_path = ""
tmap_path = ""
prank_path = ""

BWA = BWA(path=bwa_path, max_threads=max_threads)
BLAT = BLAT()
STAR = STAR()

