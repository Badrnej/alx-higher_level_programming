-- Lists all records in the second_table with a score >= 10.
-- Records are ordered by descending score.
SELECT `score`, `name`
FROM `second_table`
WHERE `score` >= 10
ORDER BY `score` DESC;
