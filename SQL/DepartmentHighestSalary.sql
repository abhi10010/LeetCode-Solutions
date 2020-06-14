SELECT
    d.Name as 'Department', e.Name as 'Employee', e.Salary
FROM
    Employee e
INNER JOIN
    Department d ON
        e.DepartmentId = d.Id
WHERE
    (e.DepartmentId, Salary) IN
       (SELECT
            DepartmentId, MAX(Salary)
        FROM
            Employee
        GROUP BY
            DepartmentId)
