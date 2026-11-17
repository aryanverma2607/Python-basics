**1.**

Create a table named Students with the following columns:



StudentID (INT, Primary Key)

Name (VARCHAR(50), NOT NULL)

Age (INT, should be between 18 and 25)

Marks (DECIMAL(5,2), should be between 0 and 100)



mysql> create table if not exists student(st\_id int primary key,Name varchar(50) not null,age int,marks decimal(5,2),check(age between 18 and 25 and marks between 0 and 100));

Query OK, 0 rows affected (0.18 sec)





Insert the following records and observe what happens:



(101, 'Alice', 20, 85.5)

(102, 'Bob', 17, 90.0) (This should fail due to Age constraint)

(103, 'Charlie', 22, 105.0) (This should fail due to Marks constraint)

(104, 'David', 24, 75.0)



mysql> insert into student(st\_id,name,age,marks)

&#x20;   -> values

&#x20;   -> (101,"Alice",20,85.5),

&#x20;   -> (102,"Bob",17,90.0),

&#x20;   -> (103,"Charlie",22,105.0),

&#x20;   -> (104,"David",24,75.0);

ERROR 3819 (HY000): Check constraint 'student\_chk\_1' is violated.

mysql> insert into student(st\_id,name,age,marks)

&#x20;   -> values

&#x20;   -> (101,"Alice",20,85.5),

&#x20;   -> (102,"Bob",18,90.0),

&#x20;   -> (103,"Charlie",22,78.0),

&#x20;   -> (104,"David",24,75.0);

Query OK, 4 rows affected (0.01 sec)

Records: 4  Duplicates: 0  Warnings: 0



mysql> select \* from student;

+-------+---------+------+-------+

| st\_id | Name    | age  | marks |

+-------+---------+------+-------+

|   101 | Alice   |   20 | 85.50 |

|   102 | Bob     |   18 | 90.00 |

|   103 | Charlie |   22 | 78.00 |

|   104 | David   |   24 | 75.00 |

+-------+---------+------+-------+

4 rows in set (0.01 sec)

















**2.**



Create a table Patients with:



PatientID (INT, Primary Key)

PatientName (VARCHAR(50), NOT NULL)

Age (INT, should be between 1 and 100)

AdmissionStatus (VARCHAR(15), should be 'Admitted' or 'Discharged', DEFAULT 'Admitted')

TreatmentCost (DECIMAL(10,2), should be at least 1000)





mysql> create table patients(Patient\_id int primary key,Patient\_name varchar(50) not null,age int,admission\_status varchar(15) default "Admitted",treatment decimal(10,2),check(age between 1 and 100 and admission\_status in ("Admitted","Discharged") and treatment>=1000));

Query OK, 0 rows affected (0.13 sec)





Insert records and check constraints:



(201, 'Michael', 25, 'Admitted', 5000)

(202, 'Linda', 105, 'Admitted', 8000) (Should fail due to Age constraint)

(203, 'David', 40, DEFAULT, 1200) (Should insert 'Admitted' as default)

(204, 'Sarah', 30, 'Discharged', 700) (Should fail due to TreatmentCost constraint)



mysql> insert into patients(patient\_id,patient\_name,age,admission\_status,treatment) values

&#x20;   -> (201, 'Michael', 25, 'Admitted', 5000),

&#x20;   -> (202, 'Linda', 105, 'Admitted', 8000),

&#x20;   -> (203, 'David', 40, DEFAULT, 1200)

&#x20;   -> ;

ERROR 3819 (HY000): Check constraint 'patients\_chk\_1' is violated.

mysql> insert into patients(patient\_id,patient\_name,age,admission\_status,treatment) values

&#x20;   -> (201, 'Michael', 25, 'Admitted', 5000),

&#x20;   -> (202, 'Linda', 105, 'Admitted', 8000),

&#x20;   -> (203, 'David', 40, DEFAULT, 1200),

&#x20;   -> (204, 'Sarah', 30, 'Discharged', 700);

ERROR 3819 (HY000): Check constraint 'patients\_chk\_1' is violated.

mysql> insert into patients(patient\_id,patient\_name,age,admission\_status,treatment) values

&#x20;   -> (201, 'Michael', 25, 'Admitted', 5000),

&#x20;   -> (202, 'Linda', 55, 'Admitted', 8000),

&#x20;   -> (203, 'David', 40, DEFAULT, 1200),

&#x20;   -> (204, 'Sarah', 30, 'Discharged', 7000);

Query OK, 4 rows affected (0.02 sec)

Records: 4  Duplicates: 0  Warnings: 0





mysql> select \* from patients;

+------------+--------------+------+------------------+-----------+

| Patient\_id | Patient\_name | age  | admission\_status | treatment |

+------------+--------------+------+------------------+-----------+

|        201 | Michael      |   25 | Admitted         |   5000.00 |

|        202 | Linda        |   55 | Admitted         |   8000.00 |

|        203 | David        |   40 | Admitted         |   1200.00 |

|        204 | Sarah        |   30 | Discharged       |   7000.00 |

+------------+--------------+------+------------------+-----------+

4 rows in set (0.01 sec)





**3.**

Create a table GymMembers with:



MemberID (INT, Primary Key)

MemberName (VARCHAR(50), NOT NULL)

MembershipType (VARCHAR(15), should be 'Basic', 'Premium', or 'VIP', DEFAULT 'Basic')

MonthlyFee (DECIMAL(6,2), should be at least 500)



mysql> create table if not exists GymMembers(Member\_id int primary key,Member\_name varchar(50) not null,Membership\_type varchar(15) default "Basic",MonthlyFee decimal(6,2),check (Membership\_type in ('Basic','Premium','VIP') and monthlyFee>=500));





Insert records and check constraints:



(501, 'John', 'Premium', 1200)

(502, 'Emma', 'Gold', 800) (Should fail due to MembershipType constraint)

(503, 'Daniel', DEFAULT, 700) (Should insert 'Basic' as default)

(504, 'Sophia', 'VIP', 300) (Should fail due to MonthlyFee constraint)







mysql> insert into GymMembers(member\_id,member\_name,membership\_type,Monthlyfee)

&#x20;   -> values

&#x20;   -> (501,"John","Premium",1200),

&#x20;   -> (502,"Emma","Gold",700),

&#x20;   -> (503,"Denial",Default,800),

&#x20;   -> (504,"Sophia","VIP",300);

ERROR 3819 (HY000): Check constraint 'gymmembers\_chk\_1' is violated.

mysql> insert into GymMembers(member\_id,member\_name,membership\_type,Monthlyfee)

&#x20;   -> values

&#x20;   -> (501,"John","Premium",1200),

&#x20;   -> (502,"Emma","Premium",700),

&#x20;   -> (503,"Denial",Default,800),

&#x20;   -> (504,"Sophia","VIP",300);

ERROR 3819 (HY000): Check constraint 'gymmembers\_chk\_1' is violated.

mysql> insert into GymMembers(member\_id,member\_name,membership\_type,Monthlyfee)

&#x20;   -> values

&#x20;   -> (501,"John","Premium",1200),

&#x20;   -> (502,"Emma","Premium",700),

&#x20;   -> (503,"Denial",Default,800),

&#x20;   -> (504,"Sophia","VIP",1000);

Query OK, 4 rows affected (0.02 sec)

Records: 4  Duplicates: 0  Warnings: 0



mysql> select \* from Gymmembers;

+-----------+-------------+-----------------+------------+

| Member\_id | Member\_name | Membership\_type | MonthlyFee |

+-----------+-------------+-----------------+------------+

|       501 | John        | Premium         |    1200.00 |

|       502 | Emma        | Premium         |     700.00 |

|       503 | Denial      | Basic           |     800.00 |

|       504 | Sophia      | VIP             |    1000.00 |

+-----------+-------------+-----------------+------------+

4 rows in set (0.01 sec)

