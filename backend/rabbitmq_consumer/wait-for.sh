#!/bin/sh
set -e

# CMD ["/wait-for.sh", "rabbitmq:5672", "--", "./run.sh"]

# $1: captures the first argument passed to the script
host="$1"
# shift: removes the first argument, as we are used to with shift/pop
shift
# $@: excludes first argument and passes the rest to the command
cmd="$@"

# checking if we can establish a connection to rabbitmq:5672
until nc -z -v -w30 $host; do
  >&2 echo "RabbitMQ is unavailable - sleeping"
  sleep 1
done

# >&2 ~> "write this to the standard error channel"
>&2 echo "RabbitMQ is up - executing command"
# Execute the last argument passed to the script: "./run.sh"
exec $cmd
