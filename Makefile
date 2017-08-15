queue:
	screen -S -dm rmq rabbitmq-server start
	rabbitmqctl add_user myuser mypassword
	rabbitmqctl add_vhost myvhost
	rabbitmqctl set_user_tags myuser mytag
	rabbitmqctl set_permissions -p myvhost myuser ".*" ".*" ".*"

	screen -S -dm redis redis-server
	screen -S -dm celery celery -A remote worker -c 5 -l info
	flower -A remote --port=5555