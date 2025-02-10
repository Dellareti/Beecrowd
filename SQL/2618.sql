SELECT products.name, providers.name,categories.name
FROM providers
JOIN products 
ON providers.id = products.id_providers
JOIN categories
ON products.id_categories = categories.id
WHERE providers.name = 'Sansul SA' AND categories.name = 'Imported'
