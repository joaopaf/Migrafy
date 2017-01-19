#!/bin/bash

mongo BIVM --eval "db.dropDatabase()" 

mongoimport --db BIVM --collection maquinas --jsonArray --file datasetMod/maquinas.json
mongoimport --db BIVM --collection utilizadores --jsonArray --file datasetMod/utilizadores.json
mongoimport --db BIVM --collection auditMaquinas --jsonArray --file datasetMod/auditMaquinas.json
mongoimport --db BIVM --collection auditVendas --jsonArray --file datasetMod/auditVendas.json
mongoimport --db BIVM --collection auditUtilizadores --jsonArray --file datasetMod/auditUtilizadores.json
mongoimport --db BIVM --collection auditProdutos --jsonArray --file datasetMod/auditProdutos.json