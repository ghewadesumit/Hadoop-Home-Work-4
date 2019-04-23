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
ghewadsa@hadoop-gate-0:~$ hadoop fs -put mapper.py dir_hadoop
ghewadsa@hadoop-gate-0:~$ hadoop fs -put reducer.py dir_hadoop
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
ghewadsa@hadoop-gate-0:~$ hadoop jar /usr/hdp/current/hadoop-mapreduce-client/hadoop-streaming.jar -file ./mapper.py -mapper ./mapper.py -file ./reducer.py -reducer ./reducer.py -input /tmp/nyc.data -output dir_output

19/04/22 23:35:10 WARN streaming.StreamJob: -file option is deprecated, please use generic option -files instead.
packageJobJar: [./mapper.py, ./reducer.py] [/usr/hdp/3.1.0.0-78/hadoop-mapreduce/hadoop-streaming-3.1.1.3.1.0.0-78.jar] /tmp/streamjob8466443849846344536.jar tmpDir=null
19/04/22 23:35:12 INFO client.RMProxy: Connecting to ResourceManager at hdfs-0-3.eecscluster/192.168.200.103:8050
19/04/22 23:35:12 INFO client.AHSProxy: Connecting to Application History server at hdfs-0-0.eecscluster/192.168.200.100:10200
19/04/22 23:35:12 INFO client.RMProxy: Connecting to ResourceManager at hdfs-0-3.eecscluster/192.168.200.103:8050
19/04/22 23:35:12 INFO client.AHSProxy: Connecting to Application History server at hdfs-0-0.eecscluster/192.168.200.100:10200
19/04/22 23:35:12 INFO mapreduce.JobResourceUploader: Disabling Erasure Coding for path: /user/ghewadsa/.staging/job_1549995810963_2263
19/04/22 23:35:13 INFO mapred.FileInputFormat: Total input files to process : 1
19/04/22 23:35:13 INFO mapreduce.JobSubmitter: number of splits:3
19/04/22 23:35:13 INFO mapreduce.JobSubmitter: Submitting tokens for job: job_1549995810963_2263
19/04/22 23:35:13 INFO mapreduce.JobSubmitter: Executing with tokens: []
19/04/22 23:35:13 INFO conf.Configuration: found resource resource-types.xml at file:/etc/hadoop/3.1.0.0-78/0/resource-types.xml
19/04/22 23:35:13 INFO impl.YarnClientImpl: Submitted application application_1549995810963_2263
19/04/22 23:35:13 INFO mapreduce.Job: The url to track the job: http://hdfs-0-3.eecscluster:8088/proxy/application_1549995810963_2263/
19/04/22 23:35:13 INFO mapreduce.Job: Running job: job_1549995810963_2263
19/04/22 23:35:21 INFO mapreduce.Job: Job job_1549995810963_2263 running in uber mode : false
19/04/22 23:35:21 INFO mapreduce.Job:  map 0% reduce 0%
19/04/22 23:35:32 INFO mapreduce.Job:  map 33% reduce 0%
19/04/22 23:35:33 INFO mapreduce.Job:  map 52% reduce 0%
19/04/22 23:35:36 INFO mapreduce.Job:  map 65% reduce 0%
19/04/22 23:35:39 INFO mapreduce.Job:  map 78% reduce 0%
19/04/22 23:35:40 INFO mapreduce.Job:  map 100% reduce 0%
19/04/22 23:35:45 INFO mapreduce.Job:  map 100% reduce 68%
19/04/22 23:35:48 INFO mapreduce.Job:  map 100% reduce 100%
19/04/22 23:40:51 INFO mapreduce.Job: Job job_1549995810963_2263 completed successfully
19/04/22 23:40:51 INFO mapreduce.Job: Counters: 54
        File System Counters
                FILE: Number of bytes read=65724275
                FILE: Number of bytes written=132393941
                FILE: Number of read operations=0
                FILE: Number of large read operations=0
                FILE: Number of write operations=0
                HDFS: Number of bytes read=325141742
                HDFS: Number of bytes written=5161
                HDFS: Number of read operations=14
                HDFS: Number of large read operations=0
                HDFS: Number of write operations=2
        Job Counters
                Launched map tasks=3
                Launched reduce tasks=1
                Data-local map tasks=2
                Rack-local map tasks=1
                Total time spent by all maps in occupied slots (ms)=207735
                Total time spent by all reduces in occupied slots (ms)=129840
                Total time spent by all map tasks (ms)=41547
                Total time spent by all reduce tasks (ms)=12984
                Total vcore-milliseconds taken by all map tasks=41547
                Total vcore-milliseconds taken by all reduce tasks=12984
                Total megabyte-milliseconds taken by all map tasks=212720640
                Total megabyte-milliseconds taken by all reduce tasks=132956160
        Map-Reduce Framework
                Map input records=1474746
                Map output records=2879784
                Map output bytes=59964701
                Map output materialized bytes=65724287
                Input split bytes=291
                Combine input records=0
                Combine output records=0
                Reduce input groups=605
                Reduce shuffle bytes=65724287
                Reduce input records=2879784
                Reduce output records=605
                Spilled Records=5759568
                Shuffled Maps =3
                Failed Shuffles=0
                Merged Map outputs=3
                GC time elapsed (ms)=865
                CPU time spent (ms)=49950
                Physical memory (bytes) snapshot=7703769088
                Virtual memory (bytes) snapshot=29335343104
                Total committed heap usage (bytes)=7948206080
                Peak Map Physical memory (bytes)=2511962112
                Peak Map Virtual memory (bytes)=6250000384
                Peak Reduce Physical memory (bytes)=398827520
                Peak Reduce Virtual memory (bytes)=10735513600
        Shuffle Errors
                BAD_ID=0
                CONNECTION=0
                IO_ERROR=0
                WRONG_LENGTH=0
                WRONG_MAP=0
                WRONG_REDUCE=0
        File Input Format Counters
                Bytes Read=325141451
        File Output Format Counters
                Bytes Written=5161
19/04/22 23:40:51 INFO streaming.StreamJob: Output directory: dir_output

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

# Reference
Writing an hadoop map-reduce program using python:
http://www.michael-noll.com/tutorials/writing-an-hadoop-mapreduce-program-in-python/

Data used:
https://data.cityofnewyork.us/Public-Safety/NYPD-Motor-Vehicle-Collisions/h9gi-nx95

# Author
* Sumit Ghewade 

