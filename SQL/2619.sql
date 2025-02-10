SELECT products.name, providers.name, products.price
FROM providers
JOIN products
ON providers.id = products.id_providers
JOIN categories
ON products.id_categories = categories.id 

WHERE price > 1000 AND categories.name = 'Super Luxury'
