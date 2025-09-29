# Price Optimization Tool

## Business Understanding

### Problem Statement:
- As sellers, setting the right price is crucial to staying competitive and profitable. While we rely on our operational costs, desired margins, and supplier agreements to set prices, what’s often missing is visibility into how competitors are pricing similar products in the market. Without this market context, we risk overpricing (losing customers to cheaper alternatives) or underpricing (cutting into our own profits unnecessarily).

- New sellers entering online marketplaces often struggle with:
    - Price variability – Similar products can vary widely in price (e.g., KSh 499 vs KSh 8,900).
    - Discount strategy – Discounts strongly influence buyers, but the "sweet spot" is unclear.
    - Category saturation – Popular categories are crowded, making it hard for new sellers to compete.
    - Customer trust – Ratings and reviews play a role beyond pricing.

- This project aims to bridge that gap by providing data-driven insights from market listings such as product categories, ratings, reviews, and discounts, so sellers can benchmark against competitors and make smarter pricing decisions. The goal is not to replace existing cost-based pricing strategies, but to complement them with real-time market analysis that helps sellers price confidently and competitively.

### Why This Topic:
- In today’s highly competitive market landscape, pricing transparency for sellers has become essential for staying competitive and driving sales.
- Pricing is one of the strongest levers for profitability, and even small adjustments can significantly impact revenue and customer perception.
- This project empowers sellers to make informed, real-time pricing decisions based on market data rather than intuition, helping them remain competitive and maximize conversions. By optimizing prices, sellers can attract more customers while sustaining healthy profit margins.


### Domain Focus: 
- Competitive Pricing in Online Marketplaces (Pricing Analytics) 

### Target Audience:
- Marketplace Sellers & Vendors who want to track competitor pricing

### Potential Impact: This tool can 
- Help sellers price new products competitively from day one
- Reduce the time sellers spend on manual competitor research
- Increase sales conversions by ensuring listings are within market-accepted ranges

### Reason for considering this project
- The motivation is to empower sellers with a data-driven tool to compete fairly in a rapidly growing marketplace like Kenya.

### Objective
- Price Optimization – Predict competitive price ranges for new products.
- Discount Insights – Quantify how discounts affect buying potential.
- Trust Metrics – Identify how ratings and reviews impact sales success.

### Stakeholders
- New Sellers (B2B Clients): Data-backed guidance on product selection & pricing.
- Marketplace (Jumia): Gains from onboarding more sellers and improving customer experience.
- Business Development Teams: Use insights to attract and support vendors.


## Data Understanding

- The dataset consists of 1,999 product listings with 13 features (columns) including: 
     - current_price → Current product price.
     - original_price → Price before discount
     - discount → Discount percentage
     - main_category → Product category (electronics, fashion, etc.)
     - rating_number & verified_ratings → Customer satisfaction.
     - seller → Who is selling the item.
     - title → Product description.

## Exploratory Data Analysis (EDA)
- We performed detailed data cleaning & exploration, focusing on:
    - Price distribution across categories.
    - Impact of discounts on product visibility.
    - Category trends (Phones, Home & Office electronics, etc.).
    - Customer ratings as indicators of trust and product success.

EDA included visualizations with matplotlib and seaborn to highlight pricing trends, category performance, and rating distributions.

## Modeling

- The project applied machine learning models to:
    - Predict optimal product prices based on features like discount, category, and ratings.
    - Recommend product categories with higher sales potential.

- We experimented with multiple models (e.g., regression-based and classification-based approaches), evaluated performance, and selected the one that balanced accuracy with interpretability.

## Deployment & Deliverables
### Deliverables:

- A Jupyter Notebook with full workflow: data cleaning → EDA → modeling → insights.
- Predictive model for price optimization.
- Business-friendly insights report, including:
    - Price ranges by category
    - Discount impact on sales
    - Rating influence on product success

### Deployment (Future Work):
- Package the model into an API or web dashboard for sellers.
- Automate monthly updates using new e-commerce listings.
- Integrate results into marketplace onboarding tools for vendors.