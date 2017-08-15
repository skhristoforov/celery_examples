queue:
	screen -d -S rmq rabbitmq-server start
	rabbitmqctl add_user myuser mypassword
	rabbitmqctl add_vhost myvhost
	rabbitmqctl set_user_tags myuser mytag
	rabbitmqctl set_permissions -p myvhost myuser ".*" ".*" ".*"

	screen -d -S redis redis-server
	screen -d -s celery celery worker -c 5 -l info
