SELECT 
    class 
FROM 
    (SELECT
        class, COUNT(DISTINCT student) AS num
    FROM
        courses
    GROUP BY class) AS new
WHERE
    num >= 5
