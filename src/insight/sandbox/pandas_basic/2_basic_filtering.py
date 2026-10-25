import pandas as pd
data = {
    'Product': ['Laptop', 'Mouse', 'Monitor', 'Keyboard', 'Webcam'],
    'Price': [1200, 25, 300, 75, 100],
    'Stock': [5, 50, 12, 20, 8]
}
df_store = pd.DataFrame(data)

filter_price_100 = df_store[ df_store['Price'] > 100  ]

print(filter_price_100)


alert_products = df_store[ (df_store['Price'] <50) | (df_store['Stock'] <10) ]

print(alert_products)