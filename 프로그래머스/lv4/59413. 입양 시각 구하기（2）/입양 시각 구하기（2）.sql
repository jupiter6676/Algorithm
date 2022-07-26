WITH RECURSIVE HOURS AS (
  SELECT 0 AS H
  UNION ALL
  SELECT H + 1 FROM HOURS
  WHERE H < 23
)

SELECT H, COUNT(HOUR(ANIMAL_OUTS.DATETIME)) FROM HOURS
LEFT JOIN ANIMAL_OUTS
    ON HOURS.H = HOUR(ANIMAL_OUTS.DATETIME)
GROUP BY HOURS.H
ORDER BY HOURS.H;