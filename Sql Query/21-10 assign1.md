\# Assignment 6 — Employee Management System



\*\*Use the `employees` table and sample data given below.\*\*



\## Table Structure



Create an `employees` table with the following columns:



\* `employee\_id`

\* `employee\_name`

\* `department`

\* `city`

\* `salary`

\* `joining\_date`

\* `experience`

\* `age`

\* `gender`

\* `employment\_type`

\* `skills`



mysql> create table if not exists employee\_1(employee\_id int,employee\_name varchar(50),department varchar(20),city varchar(20),salary decimal(10,2),joining\_date date,experience int,age int,gender enum("Male","Female"),employment\_type enum("full time","part time","contract","intern"),skills set("java","python","react","angular","c++"));

Query OK, 0 rows affected (0.08 sec)





\* `email`

\* `manager\_id`



mysql> alter table employee\_1 add column email varchar(20),add column manager\_id int;



\### Data Type Requirements



Use:



\* `ENUM` for `gender`

\* `ENUM` for `employment\_type`

\* `SET` for `skills`

\* `DATE` for `joining\_date`

\* `DATE` for any other date column if required

\* Allow appropriate columns such as `email` and `manager\_id` to contain `NULL`



Insert \*\*at least 10 employees\*\* with different values.



&#x20;***INSERT INTO employee\_1***

&#x20;   ***-> (employee\_id, employee\_name, department, city, salary, joining\_date,***

&#x20;   ***->  experience, age, gender, employment\_type, skills, email, manager\_id)***

&#x20;   ***-> VALUES***

&#x20;   ***-> (1, 'Rahul Sharma', 'IT', 'Indore', 45000.00, '2022-01-15', 4, 28,***

&#x20;   ***->  'Male', 'full time', 'java,python', 'rahul@gmail.com', NULL),***

&#x20;   ***->***

&#x20;   ***-> (2, 'Priya Verma', 'HR', 'Bhopal', 38000.00, '2021-06-10', 5, 30,***

&#x20;   ***->  'Female', 'full time', 'python,react', 'priya@gmail.com', 1),***

&#x20;   ***->***

&#x20;   ***-> (3, 'Amit Patel', 'Finance', 'Mumbai', 52000.00, '2020-03-20', 6, 32,***

&#x20;   ***->  'Male', 'full time', 'java,c++', 'amit@gmail.com', 1),***

&#x20;   ***->***

&#x20;   ***-> (4, 'Sneha Gupta', 'IT', 'Pune', 60000.00, '2019-11-05', 7, 31,***

&#x20;   ***->  'Female', 'full time', 'java,react,angular', 'sneha@gmail.com', 1),***

&#x20;   ***->***

&#x20;   ***-> (5, 'Vikas Singh', 'Marketing', 'Delhi', 35000.00, '2023-02-12', 2, 25,***

&#x20;   ***->  'Male', 'part time', 'python', 'vikas@gmail.com', 2),***

&#x20;   ***->***

&#x20;   ***-> (6, 'Anjali Jain', 'IT', 'Indore', 42000.00, '2022-08-18', 3, 27,***

&#x20;   ***->  'Female', 'contract', 'react,angular', 'anjali@gmail.com', 4),***

&#x20;   ***->***

&#x20;   ***-> (7, 'Rohit Yadav', 'Sales', 'Jaipur', 30000.00, '2024-01-08', 1, 24,***

&#x20;   ***->  'Male', 'full time', 'java', 'rohit@gmail.com', 2),***

&#x20;   ***->***

&#x20;   ***-> (8, 'Neha Joshi', 'IT', 'Bangalore', 70000.00, '2018-07-23', 8, 34,***

&#x20;   ***->  'Female', 'full time', 'java,python,react', 'neha@gmail.com', NULL),***

&#x20;   ***->***

&#x20;   ***-> (9, 'Karan Mehta', 'Support', 'Ahmedabad', 28000.00, '2023-09-14', 2, 26,***

&#x20;   ***->  'Male', 'contract', 'c++', NULL, 3),***

&#x20;   ***->***

&#x20;   ***-> (10, 'Pooja Mishra', 'HR', 'Indore', 40000.00, '2021-12-01', 4, 29,***

&#x20;   ***->  'Female', 'full time', 'python,angular', 'pooja@gmail.com', 2),***

&#x20;   ***->***

&#x20;   ***-> (11, 'Arjun Das', 'IT', 'Hyderabad', 55000.00, '2020-05-17', 5, 30,***

&#x20;   ***->  'Male', 'full time', 'java,angular', 'arjun@gmail.com', 4),***

&#x20;   ***->***

&#x20;   ***-> (12, 'Kavya Nair', 'Design', 'Chennai', 32000.00, '2024-06-03', 1, 23,***

&#x20;   ***->  'Female', 'intern', 'react', 'kavya@gmail.com', NULL),***

&#x20;   ***->***

&#x20;   ***-> (13, 'Suresh Kumar', 'Finance', 'Bhopal', 48000.00, '2019-04-22', 7, 35,***

&#x20;   ***->  'Male', 'full time', 'python,c++', 'suresh@gmail.com', 3),***

&#x20;   ***->***

&#x20;   ***-> (14, 'Divya Shah', 'IT', 'Pune', 65000.00, '2021-10-11', 5, 29,***

&#x20;   ***->  'Female', 'contract', 'java,python,angular', 'divya@gmail.com', 4),***

&#x20;   ***->***

&#x20;   ***-> (15, 'Manish Tiwari', 'Marketing', 'Delhi', 36000.00, '2023-07-19', 2, 26,***

&#x20;   ***->  'Male', 'part time', 'react,c++', 'manish@gmail.com', 2);***



Your data must include:



\* At least SOME different departments

\* At least SOME different cities

\* Some employees with `NULL` email

\* Some employees with `NULL` manager\_id

\* Different employment types such as `FULL\_TIME`, `PART\_TIME`, `CONTRACT`, `INTERN`

\* Different combinations of skills using `SET`

\* Employees who joined before 2022

\* Employees who joined between 2022 and 2024

\* Employees who joined after 2024

\* Different salary ranges

\* Different experience levels

\* Both male and female employees



\---



\## Write SQL queries for the following questions:



Find employees from IT, Finance, or HR who joined after '2023-01-01', have salary between ₹40,000 and ₹90,000, and have experience greater than 3 years.



select \* from employee\_1 where department in('it','hr','finance') and joining\_date>'2023-01-01' and salary between 40000 and 90000 and experience>3;







2\. Find employees whose email is NULL, salary is greater than ₹50,000, and joining date is after '2022-01-01'.



select \* from employee\_1 where department in('it','hr','finance') and joining\_date>'2023-01-01' and salary between 40000 and 90000 and experience>3;





3\. Find employees whose manager\_id is NOT NULL, department is not HR, and salary is either below ₹40,000 or above ₹80,000.



select \* from employee\_1 where manager\_id is null and department not in ("hr") and (salary<40000 or salary>80000);





4\. Find employees from Indore, Pune, or Delhi who joined between '2022-01-01' and '2025-12-31', have salary greater than ₹45,000, and experience of at least 3 years.



select \* from employee\_1 where city in ("indore","pune","delhi") and (joining\_date between "2022-01-01" and "2025-12-31") and salary > 45000 and experience >=3;





5\. Find employees who are FULL\_TIME, have JAVA or PYTHON in their skills, salary greater than ₹50,000, and email is NOT NULL.



select \* from employee\_1 where skills in("java","python") and salary>50000 and email is not null and employment\_type = "full time";





6\. Find employees whose name starts with A or S, joining date is after '2023-01-01', salary is between ₹30,000 and ₹80,000, and age is between 25 and 35.



* select \* from employee\_1 where (employee\_name like "a%" or employee\_name like "s%") and joining\_date>"2023-01-01" and (salary between 30000 and 80000) and (age between 25 and 55);





7\. Find employees who belong to IT or Finance, have JAVA in skills, experience greater than 4 years, and salary is NOT between ₹50,000 and ₹80,000.



* ***select \* from employee\_1 where department in ('it','finance') and skills='java' and experience>4 and salary not between 50000 and 80000;***



8\. Find employees whose department is IT, HR, or Marketing, city is not Mumbai, salary is greater than ₹40,000, and either email is NULL or manager\_id is NULL.



* ***select \* from employee\_1 where department in('it','hr','marketing') and city!='mumbai' and salary>40000 and email is null or manager\_id is null;***





8\. Find employees who joined after '2022-01-01', are not INTERN, have salary greater than ₹45,000, and have either SQL or PYTHON in their skills.



* ***select \* from employee\_1 where joining\_date>"2022-01-01" and employment\_type!="intern" and salary>45000 and (skills in ('sql','python'));***



9\. Find employees whose salary is greater than ₹60,000 OR experience is greater than 7 years, but exclude employees from Mumbai and Bhopal.



* ***select \* from employee\_1 where (salary>60000 or experience>7) and city not in ('mumbai','bhopal');***



10\. Find employees who joined between '2023-01-01' and '2026-12-31', belong to Electronics-related departments? Instead, use: departments IT or Development, salary greater than ₹50,000, and email is NOT NULL.



* ***select \* from employee\_1 where joining\_date between "2023-01-01" and "2026-12-31" and department in('it','development') and salary>50000 and email is not null;***





11\. Find employees whose name contains the letter a, department is not HR, salary is between ₹35,000 and ₹75,000, and joining date is after '2022-06-01'.



* ***select \* from employee\_1 where employee\_name like "%a%" and department != 'hr' and salary between 35000 and 75000 and joining\_date > "2022-06-01";***





12\. Find employees who have both JAVA and SQL skills, salary greater than ₹55,000, experience greater than 3 years, and manager\_id is NOT NULL.



* ***select \* from employee\_1 where (department='java' and department='sql') and salary>55000 and experience>3 and manager\_id is not null;***



13\. Find employees who have PYTHON or REACT skills, belong to IT or Development, joined after '2023-01-01', and salary is greater than ₹50,000.



* ***select \* from employee\_1 where skills in('python','react') and department in('it','development') and joining\_date >"2023-01-01" and salary>50000;***



14\. Find employees whose employment type is CONTRACT or PART\_TIME, salary is greater than ₹35,000, joining date is between '2022-01-01' and '2025-12-31', and email is NOT NULL.



* ***select \* from employees where employment\_type in ('contract','part time') and salary>35000 and joining\_date between '2022-01-01' and '2025-12-31' and email is not null;***



15\. Find employees whose gender is FEMALE, department is IT or Finance, salary is greater than ₹45,000, and experience is greater than 2 years.



* ***select \* from employees where gender='female' and department in ('it','finance') and salary>45000 and experience>2;***



16\. Find employees whose city is Indore, Pune, or Delhi, department is not HR, joining date is after '2023-01-01', salary is between ₹40,000 and ₹1,00,000, and manager\_id is NOT NULL.



* ***select \* from employees where city in ('indore','pune','delhi') and department <> 'hr' and joining\_date >"2023-01-01" and salary between 40000 and 100000 and manager\_id is not null;***



17\. Find employees whose salary is NOT between ₹30,000 and ₹60,000, experience is greater than 5 years, and either department is IT or Finance.



* ***select \* from employees where (salary not between 30000 and 60000) and experience > 5 and department in ('it','finance');***



18\. Find employees whose email is NULL OR manager\_id is NULL, but salary must be greater than ₹40,000 and joining date must be after '2022-01-01'.



* ***select \* from employees where email is null or manager\_id is null and salary>40000 and joining\_date > "2022-01-01";***



19\. Find employees whose name starts with S OR contains a, department is IT or Finance, salary is between ₹40,000 and ₹90,000, and experience is at least 3 years.



* ***select \* from employees where employee\_name like "s%" or employee\_name like "%a%" and department in('it','finance') and salary between 40000 and 90000 and experience>=3;***





20\. Find employees who joined between '2022-01-01' and '2025-12-31', are not from Mumbai or Bhopal, salary is greater than ₹50,000, and have JAVA in their skills.



* ***select \* from employees where joining\_date between "2022-01-01" and "2025-12-31" and city not in('bhopal','mumbai') and salary>50000 and skills='java';***



21\. Find employees who are FULL\_TIME, joined after '2023-01-01', have salary greater than ₹60,000, and have either JAVA + SQL or PYTHON + REACT skills.



* ***select \* from employees where employment\_type = 'full time' and joining\_date>"2023-01-01" and salary>60000 and (skills in ('java','sql') or skills in ('python','react'));***



22\. Find employees from IT, Finance, or Development whose salary is between ₹45,000 and ₹90,000, experience is greater than 3 years, email is NOT NULL, and manager\_id is NOT NULL.



* ***select \* from employees where department in ('it','finance','development') and salary between 45000 and 90000 and experience>3 and email is not null and manager\_id is not null;***



23\. Find employees whose joining date is after '2023-01-01', department is not HR, salary is greater than ₹50,000 OR experience is greater than 6 years, and city is not Mumbai.



* ***select \* from employees where joining\_date >"2023-01-01" and department <>"hr" and salary>50000 and experience>6 and city<>'mumbai';***



24\. Find employees whose name starts with A or M, gender is FEMALE, employment type is FULL\_TIME, salary is greater than ₹45,000, and email is NOT NULL.



* ***select \* from employees where employee\_name like "a%" or employee\_name like "m%" and gender = 'female' and employment\_type='full time' and salary>45000 and email is not null;***





25\. Find employees who have JAVA or SPRING in their skills, joined after '2022-01-01', salary is NOT between ₹40,000 and ₹70,000, and manager\_id is NOT NULL.



select \* from employees where skills in ('java','spring') and joining\_date>"2022-01-01" and salary between 40000 and 70000 and manager\_id is not null;





26\. Find employees from Indore, Pune, or Delhi whose joining date is between '2023-01-01'

&#x20;and '2026-12-31', salary is between ₹40,000 and ₹1,00,000, experience is greater than 2 years, and either email or manager\_id is NULL.



* ***select \* from employees where city in('indore','pune','delhi') and joining\_date between "2023-01-01" and "2026-12-31" and salary between 40000 and 100000 and experience>2 and (email is null or manager\_id is null);***



27\. Find employees belonging to IT or Development, whose name contains a, skills contain JAVA or PYTHON, salary is greater than ₹50,000, joining date is after '2023-01-01', and email is NOT NULL.



* ***select \* from employees where department in('it','development') and employee\_name like "%a%" and skills in ('java','python') and salary>50000 and joining\_date > "2023-01-01" and email is not null;***







28\. Find employees whose department is IT, Finance, or Development, city is not Mumbai or Bhopal, salary is between ₹40,000 and ₹90,000, experience is greater than 3 years, skills contain SQL, and manager\_id is NOT NULL. Display the result ordered by salary in descending order.



* ***select \* from employees where department in('it','finance','development') and city not in ('mumbai','bhopal') and salary between 40000 and 90000 and experience>3 and skills='sql' and manager\_id is not null order by salary desc;*** 







29\. Find employees whose name starts with S OR contains a, department is IT or Finance, joining date is between '2023-01-01' and '2026-12-31', salary is between ₹40,000 and ₹1,00,000, experience is greater than 2 years, email is NOT NULL, manager\_id is NOT NULL, skills contain JAVA or PYTHON, and city is Indore, Pune, or Delhi. Display the result first by department ascending and then by salary descending.





* ***select \* from employees where employee\_name like "s%a%" and department in('it','finance') and joining\_date between "2023-01-01" and "2026-12-31" and salary between 40000 and 100000 and experience>2 and email is not null and manager\_id is not null and skills in('java','python') and city in('indore','pune','delhi') order by salary desc;***



Display the result first by department ascending



* ***select \* from employees where employee\_name like "s%a%" and department in('it','finance') and joining\_date between "2023-01-01" and "2026-12-31" and salary between 40000 and 100000 and experience>2 and email is not null and manager\_id is not null and skills in('java','python') and city in('indore','pune','delhi') order by salary;***

