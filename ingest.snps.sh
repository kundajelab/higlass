docker exec higlass-manage-container-default python higlass-server/manage.py ingest_tileset  --filename /media/gecco/snps.formatted.bed.gz.beddb --filetype beddb --datatype bedlike --coordSystem hg19 --name GECCO_SNPs --project-name GECCO --no-upload
