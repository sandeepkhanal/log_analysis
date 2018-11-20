# LOG ANALYSIS
by Sandeep Khanal
Log Analysis Project, part of Udacity Full Stack Web Developer Nanodegree.

This project is an internal reporting tool that uses information from the database.
## Requirements
This project requires following softwares:

* [Python3](https://www.python.org/)
* [Vagrant](https://www.vagrantup.com/)
* [VirtualBox](https://www.virtualbox.org/wiki/Downloads)
* [PostgreSQL](https://www.postgresql.org)

## Project Purpose
The reporting tool answers following questions:
1. What are the most popular three articles of all time? 
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?

## How to Run the Project
1.Download or clone given repo from github https://github.com/udacity/fullstack-nanodegree-vm
2.Bring the Virtual Machine up 
```sh
vagrant up
```
3.Login to VM
```sh
vagrant ssh
```
4.Navigate to vagrant directory.
```sh
cd /vagrant
```
5.Download the SQL file from [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) and copy it to vagrant directory
6.Connect to the database named 'news'
```sh
psql -d news -f newsdata.sql
```
7.Run the reporting tool.
```sh
python log_analysis.py
```

## Views Created
article_view
```sh
create view article_view as select title,author,count(*) as views 
from articles,log 
where log.path like concat('%',articles.slug) 
group by articles.title,articles.author
order by views desc;
```
all_requests
```sh
create view all_requests as
select count(*) as count,date(time) as date
from log
group by date
order by count desc;
```

error_requests
```sh
create view error_requests as
select count(*) as count,date(time) as date
from log
where status!='200 OK'
group by date
order by count desc;
```

error_percentages
```sh
create view error_percentages as 
select all_requests.date,round((100.0*error_requests.count)/all_requests.count,2) as error_percentage
from error_requests,all_requests
where error_requests.date=all_requests.date;
```
