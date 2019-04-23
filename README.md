# Hadoop-Home-Work-4
Hadoop is an open-source software framework for storing data and running applications on clusters of commodity hardware. It provides massive storage for any kind of data, enormous processing power and the ability to handle virtually limitless concurrent tasks or jobs.

# Objective
* This data was collected from the City of New York’s data website, and contains all reports of vehicular incidents in New York City over a period of time. The file is roughly 175MB in size, and contains over
900,000 records.
* There are a considerable number of fields, including columns with a common format that describe up to 5 vehicles that contributed to the particular incident.
* Using the Hadoop streaming API (the one we demonstrated in class using the Python scripts, but you may use any similar script that can be invoked in a similar manner using STDIN and STDOUT), build
mapper and reducer scripts that analyze the data and yield summary counts for each vehicle that describe the total count, per vehicle type, that the vehicle type was involved in an incident.
* If the same type of vehicle was involved more than once in an incident, count the vehicle twice for the purpose of the summary statistic.

# Preprocessing

In here we have to calculate the number of occurance of a particular vehicle type in an accident. 

* Mapper function is used to return the occurance of every data with a count of 1. Here we have to just consider the 5 columns of the vehicle type which were responsible for the accident on the particular streets.
* To create the the file using the following commands:-

* Login into your hadoop cluster and create python file for Mapper.
```
ghewadsa@hadoop-gate-0:~$ vim mapper.py

```
* Create python file for Reducer.

```
ghewadsa@hadoop-gate-0:~$ vim reducer.py

```

* Check locally if the Python code is executing as expected and returning desired outcome.

```
ghewadsa@hadoop-gate-0:~$ cat /home/tatavag/nyc.data | python mapper.py

AMBULANCE       1
PASSENGER VEHICLE       1
SPORT UTILITY / STATION WAGON   1
PASSENGER VEHICLE       1
SPORT UTILITY / STATION WAGON   1
PASSENGER VEHICLE       1
PASSENGER VEHICLE       1
PASSENGER VEHICLE       1
...
...
```

* Now pass the output of the Mapper python file to Reducer to check if the Reducer is returning the desired outcome.

```
ghewadsa@hadoop-gate-0:~$ cat /home/tatavag/nyc.data | python mapper.py | sort -k1,1 | python reducer.py

12 PA   3
15 PA   2
2 DR SEDAN      72
3D      64
3DC-    1
3-DOOR  112
3-WHE   1
4 DR SEDAN      1468
```
* Now that we have checked the execution of all the files. We can deploy the code on HDFS by creating a directory.

```
ghewadsa@hadoop-gate-0:~$ hadoop fs -mkdir hw4_hadoop
```

* Check the directory of HDFS using following command
```
ghewadsa@hadoop-gate-0:~$ hadoop fs -lsr
lsr: DEPRECATED: Please use 'ls -R' instead.
drwx------   - ghewadsa hdfs          0 2019-04-22 14:00 .Trash
drwx------   - ghewadsa hdfs          0 2019-04-22 02:45 .staging
drwxr-xr-x   - ghewadsa hdfs          0 2019-04-22 02:37 dir_hadoop
```
* Upload the Python files on the HDFS using following command:

```
ghewadsa@hadoop-gate-0:~$ hadoop fs -put mapper.py hw4_hadoop
ghewadsa@hadoop-gate-0:~$ hadoop fs -put reducer.py hw4_hadoop
```
* Check the directory of HDFS using following command
```
ghewadsa@hadoop-gate-0:~$ hadoop fs -lsr
lsr: DEPRECATED: Please use 'ls -R' instead.
drwx------   - ghewadsa hdfs          0 2019-04-22 14:00 .Trash
drwx------   - ghewadsa hdfs          0 2019-04-22 02:45 .staging
drwxr-xr-x   - ghewadsa hdfs          0 2019-04-22 02:37 dir_hadoop
-rw-r--r--   3 ghewadsa hdfs        558 2019-04-22 02:37 dir_hadoop/mapper.py
-rw-r--r--   3 ghewadsa hdfs        569 2019-04-22 02:03 dir_hadoop/reducer.py
```
* Run the Python files using the command:
```
hadoop jar /usr/hdp/current/hadoop-mapreduce-client/hadoop-streaming.jar -file ./mapper.py -mapper ./mapper.py -file ./reducer.py -reducer ./reducer.py -input /tmp/nyc.data -output dir_output
```
* Check the directory of HDFS using following command
```
ghewadsa@hadoop-gate-0:~$ hadoop fs -lsr
lsr: DEPRECATED: Please use 'ls -R' instead.
drwx------   - ghewadsa hdfs          0 2019-04-22 14:00 .Trash
drwx------   - ghewadsa hdfs          0 2019-04-22 02:45 .staging
drwxr-xr-x   - ghewadsa hdfs          0 2019-04-22 02:37 dir_hadoop
-rw-r--r--   3 ghewadsa hdfs        558 2019-04-22 02:37 dir_hadoop/mapper.py
-rw-r--r--   3 ghewadsa hdfs        569 2019-04-22 02:03 dir_hadoop/reducer.py
drwxr-xr-x   - ghewadsa hdfs          0 2019-04-22 02:40 dir_output
-rw-r--r--   3 ghewadsa hdfs          0 2019-04-22 02:40 dir_output/_SUCCESS
-rw-r--r--   3 ghewadsa hdfs       5161 2019-04-22 02:40 dir_output/part-00000
```
* Check the output using the following command:
```
ghewadsa@hadoop-gate-0:~$ hadoop fs -cat ./dir_output/part-00000
"       2
"RED    1
"UNK    1
(CEME   1
12 PA   3
15 PA   2
16M     1
18 WH   3
1S      1
2 DOO   1
2 DR SEDAN      72
```
# Steps for running the Mapper & Reducer on CSCloud

* Delete the directory for the output. This precaution is taken if there is same directory then system throws an error of the same directory exists.

```
hadoop dfs -rm -r dir_output
```

* If there is no such directory at your location then use the following command to execute the file:-
```
hadoop jar /usr/hdp/current/hadoop-mapreduce-client/hadoop-streaming.jar -file /home/ghewadsa/mapper.py -mapper /home/ghewadsa/mapper.py -file /home/ghewadsa/reducer.py -reducer /home/ghewadsa/reducer.py -input /tmp/nyc.data -output dir_output
```
* To check the output of the file run the following command:
```
hadoop fs -cat ./dir_output/part-00000
```
