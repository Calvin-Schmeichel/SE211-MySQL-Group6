1. Pull the MySql docker image from DockerHub
    `docker pull mysql:latest`
    * [MySQL on Docker Hub](https://hub.docker.com/_/mysql)

2. Create a docker network:
    `docker network create “NETWORK-NAME”`

3. Start the MySQL container:
    `docker run --name “CONTAINER-NAME” -e MYSQL_ROOT_PASSWORD=”PASSWORD” -d --network=“NETWORK-NAME” mysql:latest`

4. Verify the MySQL container is running:
	 `docker ps`
    * Note the *“CONTAINER ID”* of your running container

5. Connect to MySQL container
   ` docker exec -it “CONTAINER-NAME” mysql -uroot -p`
    * Enter *”PASSWORD”*
    * You logged in successfully if you see your command line change to *“mysql”*
    * Type `exit` to leave the container

6. Now copy your .sql script you want to run
    * From your command line navigate to the folder containing your script file
    * Once you are in the correct path enter `docker cp “FILENAME.sql” “CONTAINER ID”:/home/files`
    * Now your file is saved to the container

7. Connect to MySQL container (Again)
    `docker exec -it “CONTAINER-NAME” mysql -uroot -p`
    * Enter *”PASSWORD”*

8. Create a local Database:
    `CREATE DATABASE “DATABASENAME”;`
    `USE “DATABASENAME”;`
    * You can verify that you are in the new database by running SELECT DATABASE();

9. Then type:
    `source /home/files`
    * You know if it worked if you get a message along the lines of *“Query OK, 0 rows affected (0.01 sec)”*

10. You're done!:
    * From here you can run more commands to interact with your database or tables
    * If you update your file in your IDE/Text Editor just run the step 6 copy command again to update it.