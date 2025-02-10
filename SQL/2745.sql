SELECT people.name, round((0.10*people.salary),2) AS tax
FROM people
WHERE people.salary > 3000
