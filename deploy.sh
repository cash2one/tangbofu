#!/bin/bash
 
WEB_PATH='/srv/www/tangbofu'
WEB_USER='www-data'
WEB_USERGROUP='www-data'
 
echo "Start deployment"
cd $WEB_PATH
echo "pulling source code..."
#git reset --hard origin/master
#git clean -f
git pull 
#git checkout master
#echo "changing permissions..."
#chown -R $WEB_USER:$WEB_USERGROUP $WEB_PATH
echo "Finished."