#ingest bigwigs into higlass
import argparse
def parse_args():
    parser=argparse.ArgumentParser()
    parser.add_argument("--bigwigs_file")
    parser.add_argument("--outf")
    return parser.parse_args()

def main():
    args=parse_args()
    bigwig_dict=dict() 
    bigwig_files=open(args.bigwigs_file,'r').read().strip().split('\n')
    for line in bigwig_files:
        tokens=line.split('/')
        sample=tokens[-1].split('.')[0]
        if line.endswith(".pval.signal.bw"):
            sample='_'.join([sample,'PVAL'])
        elif line.endswith(".pval.signal.bigwig"):
            sample='_'.join([sample,'PVAL'])
        elif line.endswith(".fc.signal.bw"):
            sample='_'.join([sample, 'FC'])
        elif line.endswith(".fc.signal.bigwig"):
            sample='_'.join([sample, 'FC'])
        else:
            print("Invalid file ending, must be .pval.signal.bw or .fc.signal.bw")
            print(line)
            raise Exception() 
            
        suffix_for_higlass='/'.join(tokens[4::])
        if sample not in bigwig_dict:
           bigwig_dict[sample]=suffix_for_higlass
    outf=open(args.outf,'w')
    for sample in bigwig_dict:
        outf.write("docker exec higlass-manage-container-default  python higlass-server/manage.py ingest_tileset --filename /media/"+bigwig_dict[sample]+" --filetype bigwig --datatype vector --coordSystem hg19 --name "+sample + " --project-name GECCO --no-upload"+'\n')
        

if __name__=="__main__":
    main()
    
