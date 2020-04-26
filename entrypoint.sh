#!/bin/sh

while true; do
  flask db upgrade
  if [[ "$?" == "0" ]]; then
    break
  fi
  echo "Upgrade failed, waiting 5 seconds..."
  sleep 5
done

flask run