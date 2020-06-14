SELECT 
    MAX(SALARY) as SecondHighestSalary
FROM 
    Employee
WHERE 
    Salary NOT IN 
        (SELECT 
            MAX(Salary)
          FROM 
            Employee)
