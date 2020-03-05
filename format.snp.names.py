import pandas as pd
snps=pd.read_csv("/srv1/scratch/media/gecco/snps.hammock.gz",header=None,sep='\t')
outf=open('snps.formatted.bed','w')
for index,row in snps.iterrows():
    if index%100000==0:
        print(index) 
    chrom=row[0]
    start=str(row[1])
    end=str(row[2])
    metadata=row[3].split(',')
    name=metadata[1].split(':')[1].strip('"')
    pval=str(round(float(metadata[2].split(':')[1].split('[')[1]),2))
    beta=str(round(float(metadata[3].split(']')[0]),2))
    freq=str(round(float(metadata[6].split('=')[1]),2))
    out='\t'.join([chrom,start,end,name,pval,beta,freq])
    #print(out)
    outf.write(out+'\n')
outf.close()

