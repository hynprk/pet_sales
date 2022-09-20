"""
Created on Wed Aug 31 16:14:12 2022

@author: Grace Hyo-Eun Park
"""

# Business Task: Prepare a list of popular products for the pet box subscription.
# Whether the list should only include the products being purchased more than once.
## Leading Questions:
### 1. How many products are being purchased more than once?
### 2. Do the products being purchased again have better sales than others?
### 3. What products are more likely to be purchased again for different types of pets?

import matplotlib.pyplot as plt
import pandas as pd

pet_df = pd.read_csv("/Users/hyoeungracepark/Desktop/pet_sales/data/pet_product_count.csv")

# Check column names
print(pet_df.keys())

# x = pet_type
# y = count
# hue = product_category
plt.bar(pet_df.pet_type, pet_df.count)
plt.xlabel('Pet type')
plt.ylabel('Count')
plt.title('Number of Repurchases for Different Types of Pets')
plt.show()
