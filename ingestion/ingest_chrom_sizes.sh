#!/bin/bash
#docker exec higlass-manage-container-default python higlass-server/manage.py ingest_tileset --filetype chromsizes-tsv --datatype chromsizes --coordSystem hg19  --name hg19.chrom.sizes --filename /media/hg19.chrom.sizes
docker exec higlass-manage-container-default python higlass-server/manage.py ingest_tileset --filetype chromsizes-tsv --datatype chromsizes --coordSystem hg38  --name hg38.chrom.sizes --filename /media/hg38.chrom.sizes


