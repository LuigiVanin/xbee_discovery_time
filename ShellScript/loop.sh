#!/bin/bash

for i in $(seq 1 30); do
	echo "attempt $i"
 	python3 /home/htnek/Documentos/Project/Python/discovery_time.py;
done
