SELECT
    s1.Score,
    COUNT(r.Score) 'Rank'
FROM
    Scores s1, 
    (SELECT 
        DISTINCT Score
     FROM
        Scores) r
WHERE
    r.Score >= s1.Score
GROUP BY
    s1.Id
ORDER BY
    s1.Score DESC
