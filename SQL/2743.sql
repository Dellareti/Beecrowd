SELECT people.name, char_length(people.name) AS length
FROM people
ORDER BY length DESC
