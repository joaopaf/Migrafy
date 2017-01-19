#!/bin/bash

mongo BIVM --eval "db.dropDatabase()" 

mongoimport --db BIVM --collection maquinas --jsonArray --file datasetBase/maquinas.json
mongoimport --db BIVM --collection utilizadores --jsonArray --file datasetBase/utilizadores.json
