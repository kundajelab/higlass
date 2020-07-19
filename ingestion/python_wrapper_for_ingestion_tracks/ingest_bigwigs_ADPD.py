#ingest bigwigs into higlass
import argparse
def parse_args():
    parser=argparse.ArgumentParser()
    parser.add_argument("--bigwig_file_AD_FC",default="/srv1/scratch/media/adpd/fc/AD_FC.bigwigs.txt")
    parser.add_argument("--bigwig_file_AD_PVAL",default="/srv1/scratch/media/adpd/pval/AD_PVAL.bigwigs.txt")
    parser.add_argument("--bigwig_file_PD_FC",default="/srv1/scratch/media/adpd/fc/PD_FC.bigwigs.txt")
    parser.add_argument("--bigwig_file_PD_PVAL",default="/srv1/scratch/media/adpd/pval/PD_PVAL.bigwigs.txt")
    parser.add_argument("--out_suffix",default="adpd_ingest.sh")
    return parser.parse_args()

def main():
    args=parse_args()

    process(args.bigwig_file_AD_FC,'AD','fc',args.out_suffix)
    process(args.bigwig_file_AD_PVAL,'AD','pval',args.out_suffix)
    process(args.bigwig_file_PD_FC,'PD','fc',args.out_suffix)
    process(args.bigwig_file_PD_PVAL,'PD','pval',args.out_suffix)
    
def process(fname,dataset,tracktype,out_suffix):    
    bigwig_file=open(fname,'r').read().strip().split('\n')
    outf=open(dataset+"."+tracktype+"."+out_suffix,'w')
        
    for line in bigwig_file:
        tokens=line.split('/')
        sample=tracktype+":"+'_'.join(tokens[-1].split('.')[0].split('-')[0:5])
        basename=tokens[-1]
        print(sample)
        print(tracktype)            
        outf.write("docker exec higlass-manage-container-default  python higlass-server/manage.py ingest_tileset --filename /media/adpd/"+tracktype+'/'+dataset+'/'+basename+" --filetype bigwig --datatype vector --coordSystem hg38 --name "+sample + " --project-name "+dataset+"_"+tracktype+" --no-upload"+'\n')
        

if __name__=="__main__":
    main()
    
