SELECT products.name
FROM products
JOIN providers
ON products.id_providers = providers.id 
WHERE amount BETWEEN 10 and 20 AND providers.name LIKE 'P%'
