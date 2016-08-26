#!/bin/sh

sqlite3 ../data/purchasing.db <<EOF

	.headers on
	.mode csv
	.output ../data/out.csv
	select * from items where br10qty > 0;;
	.output stdout
	.exit	

EOF
