#!/bin/sh

echo "Stop Each Services of each Stack ..."

# For Each Stack
for stack in */; do
    echo "\nStack : $(echo $stack | sed 's/.$//' | sed 's/.*/\u&/')"
    cd $stack
    # For Each Service
    for service in */; do
        echo "\nService : $(echo $service | sed 's/.$//' | sed 's/.*/\u&/')"
        cd $service
        cat docker-compose.yml
        cd ..
    done
    cd ..
done

echo "\nStop Complete !"

exit 0
