SELECT 
    Request_at AS Day,
    ROUND(COUNT(DISTINCT(CASE 
                            WHEN T.STATUS = 'cancelled_by_driver' 
                            OR T.STATUS = 'cancelled_by_client' 
                                THEN T.ID 
                         END)) / COUNT(DISTINCT(T.ID)),2) 
    AS 'Cancellation Rate'
FROM 
    TRIPS AS T
JOIN 
    USERS AS A ON A.USERS_ID = T.CLIENT_ID
JOIN 
    USERS AS B ON B.USERS_ID = T.DRIVER_ID
WHERE 
    (A.BANNED = 'NO' AND B.BANNED = 'NO')
    AND 
    (Request_at BETWEEN '2013-10-01' AND '2013-10-03')
GROUP BY Request_at
