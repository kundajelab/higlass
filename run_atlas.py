from higlass.client import View, Track
from higlass.tilesets import bigwig, chromsizes
import higlass.tilesets

chromsizes_fp = 'hg38.chrom.sizes'
bigwig_fp = '/var/www/atlas/dnase_processed/atac/6a306305-b6cd-4e0f-8406-8ed3f0ce230a/call-macs2_signal_track/shard-0/execution/ENCSR619BNL.merged.nodup.pval.signal.bigwig'

with open(chromsizes_fp) as f:
    cur_chromsizes = []
    for line in f.readlines():
        chrom, size = line.split('\t')
        cur_chromsizes.append((chrom, int(size)))
        
cs = chromsizes(chromsizes_fp)
print("made cs")
ts = bigwig(bigwig_fp, chromsizes=cur_chromsizes)
print("made ts") 
tr0 = Track('top-axis')
print('made tr0')
tr1 = Track('horizontal-bar', tileset=ts)
print('made tr1') 
tr2 = Track('horizontal-chromosome-labels', position='top', tileset=cs)
print('made tr2') 
view1 = View([tr0, tr1, tr2])
print('made view') 
display, server, viewconf = higlass.display([view1],host='nandi.stanford.edu',server_port=8989,dark_mode=False)
print('started display')
display
