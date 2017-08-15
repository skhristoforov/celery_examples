queue:
    sudo rabbitmqctl add_user myuser mypassword
    sudo rabbitmqctl add_vhost myvhost
    sudo rabbitmqctl set_user_tags myuser mytag
    sudo rabbitmqctl set_permissions -p myvhost myuser ".*" ".*" ".*"

    screen -d -S redis redis-server
    screen -d -s celery celery worker -c 5 -l info
