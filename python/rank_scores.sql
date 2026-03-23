SELECT
  S1.score,
  (
    SELECT
      COUNT(DISTINCT S2.score)
    FROM
      Scores S2
    WHERE
      S2.score >= S1.score
  ) AS 'rank'
FROM
  Scores S1
ORDER BY
  S1.score DESC


--SELECT 
--    S1.score,
--    (
--    SELECT
--        COUNT(DISTINCT S2.score)
--        FROM 
--            Scores S2
--        WHERE
--            S2.score >= S1.score
--    ) as 'rank'
--FROM Scores S1
--ORDER BY
--S1.scores DESC;
