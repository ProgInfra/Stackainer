#!/bin/sh

echo "Start Each Services of each Stack ..."

# Get Global Environment Variables
echo "Get Global Environment Variables ..."
source ./.env.sample

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

echo "\nStart Complete !"

exit 0
