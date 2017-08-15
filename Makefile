queue:
	screen -S rmq -dm rabbitmq-server start
	rabbitmqctl add_user myuser mypassword
	rabbitmqctl add_vhost myvhost
	rabbitmqctl set_user_tags myuser mytag
	rabbitmqctl set_permissions -p myvhost myuser ".*" ".*" ".*"

	screen -S redis -dm redis-server
	screen -S celery -dm celery -A remote worker -c 5 -l info
	flower -A remote --port=5555