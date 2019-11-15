#ingest bigwigs into higlass
import argparse
def parse_args():
    parser=argparse.ArgumentParser()
    parser.add_argument("--bigwigs_file")
    parser.add_argument("--outf")
    parser.add_argument("--bigwig_category") 
    return parser.parse_args()

def main():
    args=parse_args()
    bigwig_dict=dict() 
    bigwig_files=open(args.bigwigs_file,'r').read().strip().split('\n')
    for line in bigwig_files:
        tokens=line.split('/')
        sample=tokens[-1].split('.')[0]
        suffix_for_higlass='/'.join(tokens[7::])
        if sample not in bigwig_dict:
            bigwig_dict[sample]=suffix_for_higlass
    outf=open(args.outf,'w')
    for sample in bigwig_dict:
        outf.write("docker exec higlass-container  python higlass-server/manage.py ingest_tileset --filename /data/"+bigwig_dict[sample]+" --filetype bigwig --datatype vector --coordSystem hg38 --name "+sample+"."+args.bigwig_category+" --project-name atlas_hg38"+'\n')
        

if __name__=="__main__":
    main()
    
