higlass-manage start -t /srv/ssd/higlass/tmp \
	       -d /srv/ssd/higlass/data \
	       --site-url 171.67.96.244 \
	       -p 8989 \
	       -n atlas \
	       -m /srv/ssd/higlass/media \
	       --no-public-data \
	       --workers 40 \
	       --use-redis \
	       --redis-dir /srv/ssd/higlass/redis


