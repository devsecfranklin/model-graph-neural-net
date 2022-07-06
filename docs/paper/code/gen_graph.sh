#!/bin/bash

terraform graph | unflatten -f -l 4 -c 6  | dot > graph.dot
dot -Tpng graph.dot > graph.png
