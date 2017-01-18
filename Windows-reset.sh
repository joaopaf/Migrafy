#!/bin/bash

echo "use BIVM\ndb.dropDatabase()\n" | mongo

mongoimport /db BIVM /collection maquinas /jsonArray /file datasetBase/maquinas.json
mongoimport /db BIVM /collection utilizadores /jsonArray /file datasetBase/utilizadores.json