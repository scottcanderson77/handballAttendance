rm -rf db/ && mkdir db && cp -a empty_db/. db/ && docker stop mysql && docker start mysql
