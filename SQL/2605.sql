SELECT products.name,providers.name
FROM providers
JOIN products
ON providers.id = products.id_providers 
JOIN categories
ON products.id_categories = categories.id
WHERE categories.id = '6'
