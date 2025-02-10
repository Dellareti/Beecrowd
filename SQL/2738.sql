SELECT candidate.name,
round((score.math*2+score.specific*3+score.project_plan*5)/10,2) AS avg
FROM score
JOIN candidate
ON score.candidate_id = candidate.id
ORDER BY avg DESC
