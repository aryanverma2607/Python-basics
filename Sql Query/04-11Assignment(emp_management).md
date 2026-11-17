============================================================

&#x20;         MYSQL SUBQUERY –  ASSIGNMENT

============================================================



CASE STUDY: EMPLOYEE MANAGEMENT SYSTEM



ABC Technologies wants to develop an Employee Management System.

The company wants to perform different salary, department and

employee analysis using MySQL Subqueries.



You are given the following tables and data.





============================================================

TABLE 1: DEPARTMENT

============================================================



Table Name: department



Structure:

mysql> use employee\_management\_04\_11;

Database changed

mysql> CREATE TABLE DEPARTMENT(DEPT\_ID INT PRIMARY KEY,DEPT\_NAME VARCHAR(30),LOCATION VARCHAR(30));



Column Name     Data Type          Description

\------------------------------------------------------------

dept\_id         INT                Department ID

dept\_name       VARCHAR(30)        Department Name

location        VARCHAR(30)        Department Location





Data:



mysql> INSERT INTO DEPARTMENT

&#x20;   -> VALUES

&#x20;   -> (1,'HR','INDORE'),

&#x20;   -> (2,'IT','PUNE'),

&#x20;   -> (3,'FINANCE','MUMBAI'),

&#x20;   -> (4,'SALES','INDORE'),

&#x20;   -> (5,'ADMIN','DELHI'),

&#x20;   -> (6,'RESEARCH','BANGLORE');

Query OK, 6 rows affected (0.06 sec)

Records: 6  Duplicates: 0  Warnings: 0



dept\_id    dept\_name       location

\------------------------------------------------

1          HR              Indore

2          IT              Pune

3          Finance         Mumbai

4          Sales           Indore

5          Admin           Delhi

6          Research        Bangalore





============================================================

TABLE 2: EMPLOYEE

============================================================



Table Name: employee



Structure:



mysql> CREATE TABLE EMPLOYEE(EMP\_ID INT PRIMARY KEY,EMP\_NAME VARCHAR(30) NOT NULL,SALARY DECIMAL(10,2) NOT NULL,DEPT\_ID INT,FOREIGN KEY(DEPT\_ID) REFERENCES DEPARTMENT(DEPT\_ID));

Query OK, 0 rows affected (0.12 sec)



Column Name     Data Type          Description

\------------------------------------------------------------

emp\_id          INT                Employee ID

emp\_name        VARCHAR(30)        Employee Name

salary          DECIMAL(10,2)      Employee Salary

dept\_id         INT                Department ID





Data:



emp\_id    emp\_name     salary       dept\_id

\------------------------------------------------

101       Amit         30000        1

102       Rahul        50000        2

103       Priya        40000        2

104       Neha         60000        3

105       Rohit        35000        3

106       Sneha        45000        4

107       Karan        55000        4

108       Pooja        28000        1

109       Vijay        70000        2

110       Ankit        32000        5

111       Meena        65000        3

112       Arjun        25000        5





NOTE:

Department 6 currently has no employees.





============================================================

QUESTIONS

============================================================





Q1.

Display all employees whose salary is greater than the average

salary of all employees.



mysql> select \* from employee where salary>(select avg(salary) from employee);

+--------+----------+----------+---------+

| EMP\_ID | EMP\_NAME | SALARY   | DEPT\_ID |

+--------+----------+----------+---------+

|    102 | Rahul    | 50000.00 |       2 |

|    104 | Neha     | 60000.00 |       3 |

|    106 | Sneha    | 45000.00 |       4 |

|    107 | Karan    | 55000.00 |       4 |

|    109 | Vijay    | 70000.00 |       2 |

|    111 | Meena    | 65000.00 |       3 |

+--------+----------+----------+---------+

6 rows in set (0.01 sec)





Q2.

Display the employee or employees who receive the highest salary

in the company.



mysql> select \* from employee where salary = (select max(salary) from employee);

+--------+----------+----------+---------+

| EMP\_ID | EMP\_NAME | SALARY   | DEPT\_ID |

+--------+----------+----------+---------+

|    109 | Vijay    | 70000.00 |       2 |

+--------+----------+----------+---------+

1 row in set (0.00 sec)







Q3.

Display the employee or employees who receive the lowest salary

in the company.



mysql> select \* from employee where salary = (select min(salary) from employee)

+--------+----------+----------+---------+

| EMP\_ID | EMP\_NAME | SALARY   | DEPT\_ID |

+--------+----------+----------+---------+

|    112 | Arjun    | 25000.00 |       5 |

+--------+----------+----------+---------+

1 row in set (0.00 sec)





Q4.

Display all employees whose salary is greater than the salary

of Amit.



mysql> select \* from employee where salary > (select salary from employee where emp\_name='Amit');

+--------+----------+----------+---------+

| EMP\_ID | EMP\_NAME | SALARY   | DEPT\_ID |

+--------+----------+----------+---------+

|    102 | Rahul    | 50000.00 |       2 |

|    103 | Priya    | 40000.00 |       2 |

|    104 | Neha     | 60000.00 |       3 |

|    105 | Rohit    | 35000.00 |       3 |

|    106 | Sneha    | 45000.00 |       4 |

|    107 | Karan    | 55000.00 |       4 |

|    109 | Vijay    | 70000.00 |       2 |

|    110 | Ankit    | 32000.00 |       5 |

|    111 | Meena    | 65000.00 |       3 |

+--------+----------+----------+---------+

9 rows in set (0.00 sec)





Q5.

Display all employees whose salary is less than the salary

of Rahul.



mysql> select \* from employee where salary < (select salary from employee where emp\_name='Rahul');

+--------+----------+----------+---------+

| EMP\_ID | EMP\_NAME | SALARY   | DEPT\_ID |

+--------+----------+----------+---------+

|    101 | Amit     | 30000.00 |       1 |

|    103 | Priya    | 40000.00 |       2 |

|    105 | Rohit    | 35000.00 |       3 |

|    106 | Sneha    | 45000.00 |       4 |

|    108 | Pooja    | 28000.00 |       1 |

|    110 | Ankit    | 32000.00 |       5 |

|    112 | Arjun    | 25000.00 |       5 |

+--------+----------+----------+---------+

7 rows in set (0.00 sec)





Q6.

Display employees who work in departments located in Indore.



Expected columns:



emp\_id

emp\_name

salary

dept\_id



mysql> SELECT E.EMP\_ID,E.EMP\_NAME,E.SALARY,E.DEPT\_ID FROM EMPLOYEE AS E JOIN DEPARTMENT AS D ON E.DEPT\_ID=D.DEPT\_ID WHERE D.LOCATION='INDORE';

+--------+----------+----------+---------+

| EMP\_ID | EMP\_NAME | SALARY   | DEPT\_ID |

+--------+----------+----------+---------+

|    101 | Amit     | 30000.00 |       1 |

|    108 | Pooja    | 28000.00 |       1 |

|    106 | Sneha    | 45000.00 |       4 |

|    107 | Karan    | 55000.00 |       4 |

+--------+----------+----------+---------+

4 rows in set (0.00 sec)







Q7.

Display employees who work in the IT or Finance departments.



Do not directly specify department IDs such as 2,3.

Obtain the department IDs using a subquery.



mysql> SELECT \* FROM EMPLOYEE WHERE DEPT\_ID IN (SELECT DEPT\_ID FROM DEPARTMENT WHERE DEPT\_NAME IN ('IT','FINANCE'));

+--------+----------+----------+---------+

| EMP\_ID | EMP\_NAME | SALARY   | DEPT\_ID |

+--------+----------+----------+---------+

|    102 | Rahul    | 50000.00 |       2 |

|    103 | Priya    | 40000.00 |       2 |

|    109 | Vijay    | 70000.00 |       2 |

|    104 | Neha     | 60000.00 |       3 |

|    105 | Rohit    | 35000.00 |       3 |

|    111 | Meena    | 65000.00 |       3 |

+--------+----------+----------+---------+

6 rows in set (0.00 sec)





Q8.

Display employees who do not work in departments located in

Indore.



mysql> SELECT E.\* FROM EMPLOYEE AS E JOIN DEPARTMENT AS D ON E.DEPT\_ID=D.DEPT\_ID WHERE D.LOCATION<>'INDORE';

+--------+----------+----------+---------+

| EMP\_ID | EMP\_NAME | SALARY   | DEPT\_ID |

+--------+----------+----------+---------+

|    102 | Rahul    | 50000.00 |       2 |

|    103 | Priya    | 40000.00 |       2 |

|    109 | Vijay    | 70000.00 |       2 |

|    104 | Neha     | 60000.00 |       3 |

|    105 | Rohit    | 35000.00 |       3 |

|    111 | Meena    | 65000.00 |       3 |

|    110 | Ankit    | 32000.00 |       5 |

|    112 | Arjun    | 25000.00 |       5 |

+--------+----------+----------+---------+

8 rows in set (0.00 sec)





Q9.

Display departments that currently have no employees.



mysql> SELECT D.\* FROM DEPARTMENT AS D LEFT JOIN EMPLOYEE AS E ON E.DEPT\_ID=D.DEPT\_ID WHERE E.DEPT\_ID IS NULL;

+---------+-----------+----------+

| DEPT\_ID | DEPT\_NAME | LOCATION |

+---------+-----------+----------+

|       6 | RESEARCH  | BANGLORE |

+---------+-----------+----------+

1 row in set (0.00 sec)



Q10.

Display employees whose salary is greater than the average salary

of the IT department.



mysql> SELECT \*

&#x20;   -> FROM EMPLOYEE

&#x20;   -> WHERE SALARY > (

&#x20;   ->     SELECT AVG(SALARY)

&#x20;   ->     FROM EMPLOYEE

&#x20;   ->     WHERE DEPT\_ID = (

&#x20;   ->         SELECT DEPT\_ID

&#x20;   ->         FROM DEPARTMENT

&#x20;   ->         WHERE DEPT\_NAME = 'IT'

&#x20;   ->     )

&#x20;   -> );

+--------+----------+----------+---------+

| EMP\_ID | EMP\_NAME | SALARY   | DEPT\_ID |

+--------+----------+----------+---------+

|    104 | Neha     | 60000.00 |       3 |

|    107 | Karan    | 55000.00 |       4 |

|    109 | Vijay    | 70000.00 |       2 |

|    111 | Meena    | 65000.00 |       3 |

+--------+----------+----------+---------+

4 rows in set (0.00 sec)







Q11.

Display employees whose salary is greater than the average salary

of the Finance department.



mysql> select \* from employee where salary > (select avg(salary) from employee where dept\_id = (select dept\_id from department where dept\_name='finance'));

+--------+----------+----------+---------+

| EMP\_ID | EMP\_NAME | SALARY   | DEPT\_ID |

+--------+----------+----------+---------+

|    104 | Neha     | 60000.00 |       3 |

|    107 | Karan    | 55000.00 |       4 |

|    109 | Vijay    | 70000.00 |       2 |

|    111 | Meena    | 65000.00 |       3 |

+--------+----------+----------+---------+

4 rows in set (0.01 sec)





Q12.

Display employees whose salary is equal to the highest salary

in the IT department.



mysql> select \* from employee where salary = (select max(salary) from employee where dept\_id = (select dept\_id from department where dept\_name='it'));

+--------+----------+----------+---------+

| EMP\_ID | EMP\_NAME | SALARY   | DEPT\_ID |

+--------+----------+----------+---------+

|    109 | Vijay    | 70000.00 |       2 |

+--------+----------+----------+---------+

1 row in set (0.00 sec)





Q13.

Display employees whose salary is less than the lowest salary

in the Sales department.



mysql> select \* from employee where salary < (select min(salary) from employee where dept\_id = (select dept\_id from department where dept\_name='sales'))

;

+--------+----------+----------+---------+

| EMP\_ID | EMP\_NAME | SALARY   | DEPT\_ID |

+--------+----------+----------+---------+

|    101 | Amit     | 30000.00 |       1 |

|    103 | Priya    | 40000.00 |       2 |

|    105 | Rohit    | 35000.00 |       3 |

|    108 | Pooja    | 28000.00 |       1 |

|    110 | Ankit    | 32000.00 |       5 |

|    112 | Arjun    | 25000.00 |       5 |

+--------+----------+----------+---------+

6 rows in set (0.00 sec)





Q14.

Display employees whose salary is greater than at least one

employee working in the HR department.



mysql> select \* from employee where salary > any(select salary from employee where dept\_id = (select dept\_id from department where dept\_name='hr'));

+--------+----------+----------+---------+

| EMP\_ID | EMP\_NAME | SALARY   | DEPT\_ID |

+--------+----------+----------+---------+

|    101 | Amit     | 30000.00 |       1 |

|    102 | Rahul    | 50000.00 |       2 |

|    103 | Priya    | 40000.00 |       2 |

|    104 | Neha     | 60000.00 |       3 |

|    105 | Rohit    | 35000.00 |       3 |

|    106 | Sneha    | 45000.00 |       4 |

|    107 | Karan    | 55000.00 |       4 |

|    109 | Vijay    | 70000.00 |       2 |

|    110 | Ankit    | 32000.00 |       5 |

|    111 | Meena    | 65000.00 |       3 |

+--------+----------+----------+---------+

10 rows in set (0.00 sec)





Q15.

Display employees whose salary is greater than every employee

working in the HR department.



mysql> select \* from employee where salary > all(select salary from employee where dept\_id = (select dept\_id from department where dept\_name='hr'));

+--------+----------+----------+---------+

| EMP\_ID | EMP\_NAME | SALARY   | DEPT\_ID |

+--------+----------+----------+---------+

|    102 | Rahul    | 50000.00 |       2 |

|    103 | Priya    | 40000.00 |       2 |

|    104 | Neha     | 60000.00 |       3 |

|    105 | Rohit    | 35000.00 |       3 |

|    106 | Sneha    | 45000.00 |       4 |

|    107 | Karan    | 55000.00 |       4 |

|    109 | Vijay    | 70000.00 |       2 |

|    110 | Ankit    | 32000.00 |       5 |

|    111 | Meena    | 65000.00 |       3 |

+--------+----------+----------+---------+

9 rows in set (0.00 sec)





Q16.

Display employees whose salary is less than at least one

employee working in the IT department.



mysql> select \* from employee where salary < any(select salary from employee where dept\_id = (select dept\_id from department where dept\_name='it'));

+--------+----------+----------+---------+

| EMP\_ID | EMP\_NAME | SALARY   | DEPT\_ID |

+--------+----------+----------+---------+

|    101 | Amit     | 30000.00 |       1 |

|    102 | Rahul    | 50000.00 |       2 |

|    103 | Priya    | 40000.00 |       2 |

|    104 | Neha     | 60000.00 |       3 |

|    105 | Rohit    | 35000.00 |       3 |

|    106 | Sneha    | 45000.00 |       4 |

|    107 | Karan    | 55000.00 |       4 |

|    108 | Pooja    | 28000.00 |       1 |

|    110 | Ankit    | 32000.00 |       5 |

|    111 | Meena    | 65000.00 |       3 |

|    112 | Arjun    | 25000.00 |       5 |

+--------+----------+----------+---------+

11 rows in set (0.00 sec)





Q17.

Display employees whose salary is greater than every employee

working in the Finance department.



mysql> select \* from employee where salary > all(select salary from employee where dept\_id = (select dept\_id from department where dept\_name='finance'));

+--------+----------+----------+---------+

| EMP\_ID | EMP\_NAME | SALARY   | DEPT\_ID |

+--------+----------+----------+---------+

|    109 | Vijay    | 70000.00 |       2 |

+--------+----------+----------+---------+

1 row in set (0.00 sec)





Q18.

Display employees whose salary is below the salary of every

employee working in the IT department.



mysql> select \* from employee where salary < all(select salary from employee where dept\_id = (select dept\_id from department where dept\_name='it'));

+--------+----------+----------+---------+

| EMP\_ID | EMP\_NAME | SALARY   | DEPT\_ID |

+--------+----------+----------+---------+

|    101 | Amit     | 30000.00 |       1 |

|    105 | Rohit    | 35000.00 |       3 |

|    108 | Pooja    | 28000.00 |       1 |

|    110 | Ankit    | 32000.00 |       5 |

|    112 | Arjun    | 25000.00 |       5 |

+--------+----------+----------+---------+

5 rows in set (0.00 sec)





Q19.

Display employees whose salary is greater than their own

department's average salary.



mysql> select \* from employee as e where salary > (select avg(salary) from employee where dept\_id = e.dept\_id);

+--------+----------+----------+---------+

| EMP\_ID | EMP\_NAME | SALARY   | DEPT\_ID |

+--------+----------+----------+---------+

|    101 | Amit     | 30000.00 |       1 |

|    104 | Neha     | 60000.00 |       3 |

|    107 | Karan    | 55000.00 |       4 |

|    109 | Vijay    | 70000.00 |       2 |

|    110 | Ankit    | 32000.00 |       5 |

|    111 | Meena    | 65000.00 |       3 |

+--------+----------+----------+---------+

6 rows in set (0.02 sec)





Q20.

Display employees whose salary is less than their own

department's average salary.



mysql> select \* from employee as e where salary < (select avg(salary) from employee where dept\_id = e.dept\_id);

+--------+----------+----------+---------+

| EMP\_ID | EMP\_NAME | SALARY   | DEPT\_ID |

+--------+----------+----------+---------+

|    102 | Rahul    | 50000.00 |       2 |

|    103 | Priya    | 40000.00 |       2 |

|    105 | Rohit    | 35000.00 |       3 |

|    106 | Sneha    | 45000.00 |       4 |

|    108 | Pooja    | 28000.00 |       1 |

|    112 | Arjun    | 25000.00 |       5 |

+--------+----------+----------+---------+

6 rows in set (0.00 sec)





Q21.

Display employees whose salary is exactly equal to their own

department's average salary.



mysql> select \* from employee as e where salary = (select avg(salary) from employee where dept\_id = e.dept\_id);

Empty set (0.01 sec)





Q22.

Display the employee or employees who receive the highest salary

in each department.



Expected columns:



emp\_id

emp\_name

salary

dept\_id



mysql> select \* from employee as e where salary = (select max(salary) from employee where dept\_id=e.dept\_id);

+--------+----------+----------+---------+

| EMP\_ID | EMP\_NAME | SALARY   | DEPT\_ID |

+--------+----------+----------+---------+

|    101 | Amit     | 30000.00 |       1 |

|    107 | Karan    | 55000.00 |       4 |

|    109 | Vijay    | 70000.00 |       2 |

|    110 | Ankit    | 32000.00 |       5 |

|    111 | Meena    | 65000.00 |       3 |

+--------+----------+----------+---------+

5 rows in set (0.01 sec)





Q23.

Display the employee or employees who receive the lowest salary

in each department.



mysql> select \* from employee as e where salary = (select min(salary) from employee where dept\_id=e.dept\_id);

+--------+----------+----------+---------+

| EMP\_ID | EMP\_NAME | SALARY   | DEPT\_ID |

+--------+----------+----------+---------+

|    103 | Priya    | 40000.00 |       2 |

|    105 | Rohit    | 35000.00 |       3 |

|    106 | Sneha    | 45000.00 |       4 |

|    108 | Pooja    | 28000.00 |       1 |

|    112 | Arjun    | 25000.00 |       5 |

+--------+----------+----------+---------+

5 rows in set (0.00 sec)





Q24.

Display employees who are not the highest-paid employees of

their respective departments.



mysql> select \* from employee as e where salary <> (select max(salary) from employee where dept\_id=e.dept\_id);

+--------+----------+----------+---------+

| EMP\_ID | EMP\_NAME | SALARY   | DEPT\_ID |

+--------+----------+----------+---------+

|    102 | Rahul    | 50000.00 |       2 |

|    103 | Priya    | 40000.00 |       2 |

|    104 | Neha     | 60000.00 |       3 |

|    105 | Rohit    | 35000.00 |       3 |

|    106 | Sneha    | 45000.00 |       4 |

|    108 | Pooja    | 28000.00 |       1 |

|    112 | Arjun    | 25000.00 |       5 |

+--------+----------+----------+---------+

7 rows in set (0.02 sec)





Q25.

Display employees who are not the lowest-paid employees of

their respective departments.



mysql> select \* from employee as e where salary <> (select min(salary) from employee where dept\_id=e.dept\_id);

+--------+----------+----------+---------+

| EMP\_ID | EMP\_NAME | SALARY   | DEPT\_ID |

+--------+----------+----------+---------+

|    101 | Amit     | 30000.00 |       1 |

|    102 | Rahul    | 50000.00 |       2 |

|    104 | Neha     | 60000.00 |       3 |

|    107 | Karan    | 55000.00 |       4 |

|    109 | Vijay    | 70000.00 |       2 |

|    110 | Ankit    | 32000.00 |       5 |

|    111 | Meena    | 65000.00 |       3 |

+--------+----------+----------+---------+

7 rows in set (0.01 sec)





Q26.

Display the second-highest salary in the company.



Do not use LIMIT.

mysql> select max(salary) from employee where salary < (select max(salary) from employee);

+-------------+

| max(salary) |

+-------------+

|    65000.00 |

+-------------+

1 row in set (0.01 sec)





Q27.

Display the employee or employees having the second-highest

salary.



Do not use LIMIT.



mysql> select \* from employee where salary = (select max(salary) from employee where salary < (select max(salary) from employee));

+--------+----------+----------+---------+

| EMP\_ID | EMP\_NAME | SALARY   | DEPT\_ID |

+--------+----------+----------+---------+

|    111 | Meena    | 65000.00 |       3 |

+--------+----------+----------+---------+

1 row in set (0.02 sec)





Q28.

Display the third-highest salary in the company.



Do not use LIMIT.



mysql> select max(salary) from employee where salary < (select max(salary) from employee where salary <(select max(salary) from employee));

+-------------+

| max(salary) |

+-------------+

|    60000.00 |

+-------------+

1 row in set (0.00 sec)





Q29.

Display the employee or employees having the third-highest

salary.



mysql> select \* from employee where salary = (select max(salary) from employee where salary < (select max(salary) from employee where salary <(select max(salary) from employee)));

+--------+----------+----------+---------+

| EMP\_ID | EMP\_NAME | SALARY   | DEPT\_ID |

+--------+----------+----------+---------+

|    104 | Neha     | 60000.00 |       3 |

+--------+----------+----------+---------+

1 row in set (0.01 sec)







**At least one employee → EXISTS ya INNER JOIN + DISTINCT**

**No employees → NOT EXISTS ya LEFT JOIN + IS NULL**

Q30.

Display all departments for which at least one employee exists.



mysql> select \* from department as d where exists (select 1 from employee as e where e.dept\_id=d.dept\_id);



mysql> select distinct D.\* from department as d inner join employee as e where e.dept\_id=d.dept\_id;

+---------+-----------+----------+

| DEPT\_ID | DEPT\_NAME | LOCATION |

+---------+-----------+----------+

|       1 | HR        | INDORE   |

|       2 | IT        | PUNE     |

|       3 | FINANCE   | MUMBAI   |

|       4 | SALES     | INDORE   |

|       5 | ADMIN     | DELHI    |

+---------+-----------+----------+

5 rows in set (0.02 sec)





Q31.

Display all departments for which no employee exists.



mysql> select distinct D.\* from department as d left join employee as e on e.dept\_id=d.dept\_id where e.emp\_id is null;



mysql> select \* from department as d where not exists (select 1 from employee as e where e.dept\_id=d.dept\_id);

+---------+-----------+----------+

| DEPT\_ID | DEPT\_NAME | LOCATION |

+---------+-----------+----------+

|       6 | RESEARCH  | BANGLORE |

+---------+-----------+----------+

1 row in set (0.00 sec)





Q32.

Display departments where at least one employee earns more

than 60000.





Q33.

Display departments where no employee earns more than 60000.





Q34.

Display departments where at least one employee earns less

than 30000.





Q35.

Display departments where no employee earns less than 30000.





Q36.

Display employees who belong to a department that exists in

the department table.





Q37.

Display employees whose salary is greater than their own

department's average salary.



Use a correlated subquery.





Q38.

Display employees whose salary is the maximum salary of their

department.



Use a correlated subquery.





Q39.

Display employees whose salary is the minimum salary of their

department.



Use a correlated subquery.





Q40.

Display each employee along with the average salary of his/her

department.



Expected columns:



emp\_id

emp\_name

salary

dept\_id

department\_average\_salary





Q41.

Display each employee along with the highest salary in his/her

department.



Expected columns:



emp\_id

emp\_name

salary

dept\_id

department\_highest\_salary





Q42.

Display each employee along with the lowest salary in his/her

department.



Expected columns:



emp\_id

emp\_name

salary

dept\_id

department\_lowest\_salary





Q43.

Display each employee along with the company's overall average

salary.



Expected columns:



emp\_id

emp\_name

salary

company\_average\_salary





Q44.

Display each employee along with the difference between his/her

salary and the company's average salary.



Expected columns:



emp\_id

emp\_name

salary

salary\_difference





Q45.

Display each employee along with the name of his/her department.



The department name must be obtained using a subquery.



Expected columns:



emp\_id

emp\_name

salary

dept\_name





Q46.

Display departments whose average salary is greater than the

average salary of the entire company.





Q47.

Display departments whose average salary is less than the

average salary of the entire company.





Q48.

Display the department having the highest average salary.





Q49.

Display the department having the lowest average salary.





Q50.

Display employees who work in the department having the

highest average salary.





Q51.

Display employees who work in the department having the

lowest average salary.





Q52.

Display departments having more employees than the average

number of employees per department.





Q53.

Display departments where every employee earns more than 30000.





Q54.

Display departments where at least one employee earns more

than 50000 and at least one employee earns less than 35000.





Q55.

Display departments where every employee earns less than 70000.





Q56.

Display employees whose salary is greater than the average of

all department average salaries.





Q57.

Display the department whose maximum employee salary is the

highest among all departments.





Q58.

Display the department whose minimum employee salary is the

lowest among all departments.





Q59.

Display employees whose salary is greater than the maximum

salary of the HR department.





Q60.

Display employees whose salary is less than the minimum salary

of the Finance department.





Q61.

Display employees whose salary is greater than every employee

in HR but less than the salary of at least one employee in IT.





Q62.

Display employees whose salary is greater than at least one

employee in Finance but less than every employee in IT.





Q63.

Display employees who work in departments where the department's

average salary is greater than 40000.





Q64.

Display departments where the average salary is greater than

40000 and at least one employee earns more than 60000.





Q65.

Display employees whose salary is greater than their department

average salary but less than the company's overall average salary.





Q66.

Display employees whose salary is less than their department

average salary but greater than the company's overall average

salary.





Q67.

Display the highest-paid employee from each department without

using GROUP BY to directly select the employee.





Q68.

Display the second-highest salary employee from each department.





Q69.

Display departments that have at least two employees.





Q70.

Display employees working in departments that have more employees

than the HR department.





Q71.

Display employees working in departments that have fewer employees

than the IT department.





Q72.

Display the department(s) having the same average salary as the

Finance department.





Q73.

Display employees whose salary is equal to the highest salary

of any department other than their own department.





Q74.

Display employees whose salary is greater than the average salary

of every department.





Q75.

Display employees whose salary is greater than the average salary

of at least one department.





Q76.

Display the employee whose salary is closest to the company's

average salary.





Q77.

Display the department whose average salary is closest to the

company's overall average salary.





Q78.

Display employees who are earning more than the average salary

of all employees but are not the highest-paid employee.





Q79.

Display employees who earn more than the average salary of their

department and whose department has at least two employees.





Q80.

Find employees who satisfy ALL of the following conditions:



1\. Salary is greater than the company average salary.

2\. Salary is greater than their department average salary.

3\. Their department has at least two employees.

4\. They are not the highest-paid employee in the company.





============================================================

CHALLENGE QUESTIONS

============================================================





Q81.

Find the department having the second-highest average salary.





Q82.

Find the employee working in the department having the

second-highest average salary.





Q83.

Find the second-highest salary employee from every department.





Q84.

Find the department having the second-highest maximum salary.





Q85.

Find employees whose salary is greater than the average salary

of the department having the second-highest average salary.





Q86.

Find the employee(s) whose salary is closest to the highest

salary in the company without being the highest-paid employee.





Q87.

Find departments where the difference between the highest and

lowest salary is greater than 30000.





Q88.

Find employees whose salary is above their department average

and whose salary difference from the department average is

greater than 10000.





Q89.

Find the department(s) where the highest-paid employee earns

more than the highest-paid employee of the HR department.





Q90.

Find employees who earn more than every employee in HR,

Finance, and Sales.





============================================================

FINAL INTERVIEW CHALLENGE

============================================================





Q91.

Without using:



JOIN

LIMIT

WINDOW FUNCTIONS



Find the employee having the third-highest distinct salary.





Q92.

Without using LIMIT or Window Functions, find the employee

having the second-highest salary in each department.





Q93.

Find the department(s) in which every employee earns more than

the company's average salary.





Q94.

Find the department(s) in which at least one employee earns more

than the company's average salary and at least one employee earns

less than the company's average salary.





Q95.

Find employees whose salary satisfies all the following:



1\. Greater than their department average.

2\. Greater than the company average.

3\. Less than the highest salary in the company.





Q96.

Find the department having the highest average salary and then

display all employees belonging to that department along with

their salary.





Q97.

Find the department having the lowest average salary and then

display all employees belonging to that department.





Q98.

Find the department with the highest number of employees and

display all employees belonging to that department.





Q99.

Find the department with the lowest number of employees,

excluding departments having zero employees, and display its

employees.





Q100.

Find employees who satisfy ALL of the following conditions:



1\. Salary is above their department average.

2\. Salary is above the company average.

3\. Employee is not the highest-paid employee of the department.

4\. Employee works in a department having at least 2 employees.



Display:



emp\_id

emp\_name

salary

dept\_id





============================================================

