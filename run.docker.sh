docker run --detach \
       --publish 8989:80 \
       --volume /srv1/scratch/data:/data \
       --volume /srv1/scratch/tmp:/tmp \
       --volume /srv1/scratch/media:/media \
       --name higlass-container \
       -e SITE_URL=vayu.stanford.edu \
       higlass/higlass-docker:latest
