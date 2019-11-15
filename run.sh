docker run --detach \
       --publish 8989:80 \
       --volume /var/www/atlas:/data \
       --volume /tmp:/tmp \
       --name higlass-container \
       -e SITE_URL=nandi.stanford.edu \
       higlass/higlass-docker:v0.6.1
