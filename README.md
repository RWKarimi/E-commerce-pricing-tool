# Price Optimization Tool

![Price Optimization](price_landscape_outputs/Predictor%20Pricing.jpeg)

### Project Collaboration

- [Notion](https://www.notion.so/270e26877fdd815a9017da739a7c8dd7?v=270e26877fdd81c7a17a000c18496f82&source=copy_link) served as our central hub for organizing tasks and resources. We used it to:  
      - Share notes and useful links in one accessible space.  
      - Document meeting notes and decisions for easy reference. 
      - Track deadlines and assigned responsibilities through task boards.  
      - Enable real-time collaboration, reducing miscommunication and delays.

### Project Authors
1. [Lewis Mbugua]
2. [Elizabeth Ogutu](https://www.linkedin.com/in/elizabeth-ogutu-36222b1a6/)
3. [Hafsa M. Aden](https://www.linkedin.com/in/hafsa-m-aden-330451223/)
4. [Ryan Karimi](https://www.linkedin.com/in/ryan-karimi-39a701326/)
5. [Harrison Kuria]
6. [Rose Muthini](https://www.linkedin.com/in/syomiti-muthini-03849a153/)

## Business Understanding
*At what price should one sell a product to remain competitive while still making a profit?*

### Problem Statement:
- Pricing is one of the most critical decisions for any seller. While costs, margins, and supplier agreements guide internal pricing, what’s often missing is visibility into how competitors price similar products. Without this context, sellers face two key risks:
    - Overpricing → losing customers to cheaper alternatives.
    - Underpricing → cutting into profits unnecessarily.

- New sellers entering marketplaces often struggle with:
    - Price variability – Similar products can vary widely in price (e.g., KSh 499 vs KSh 8,900).
    - Discount strategy – Discounts strongly influence buyers, but the "sweet spot" is unclear.

### Objectives: 
- This project aims to bridge that gap by providing data-driven insights from marketplace listings (e.g., product categories, ratings, reviews, discounts). By benchmarking against competitors, sellers gain real-time market information that complements their cost-based pricing strategies, enabling them to set prices that are both competitive and profitable.    

### Stakeholders
- New Sellers : Data-backed guidance on product selection & pricing.
- Marketplace (Jumia): Gains from onboarding more sellers and improving customer experience.
- Business Development Teams: Use insights to attract and support vendors.

### Potential Impact: 
- This tool can 
    - Help sellers price new products competitively from day one
    - Reduce the time sellers spend on manual competitor research
    - Increase sales conversions by ensuring listings are within market-accepted ranges

## Data Understanding

### Data Source
- The dataset we worked with was scraped from [Jumia](https://www.jumia.co.ke/). 
- It consist of 1,999 product listings with 13 features (columns) including: 
     - current_price → Current product price.
     - original_price → Price before discount
     - discount → Discount percentage
     - main_category → Product category (electronics, fashion, etc.)
     - rating_number & verified_ratings → Customer satisfaction.
     - seller → Who is selling the item.
     - title → Product description.


### Data Preparation
- To prepare the dataset for analysis, we applied the following steps:  
   - Removed duplicates: Many sellers list the same product multiple times.
   - Handled missing values: Some products lacked ratings or discounts. Strategies included:
       - Filling missing numeric values with averages.
       - Dropping irrelevant text-only columns when not useful for modeling.
   - Converted datatypes: Prices were stored as strings (KSh 499 → 499). Converted to integers.
   - Created new features:
       - discount_amount = original_price - current_price
       - discount_ratio = % discount offered

## Analysis Overview
- We explored the data to understand patterns and relationships in the data:
    - Price distribution:
         - Plotted Product prices across categories - Found that electronics (Phones, Tablets, Home & Office) have the widest price range.



    - Impact of discounts on product visibility.
         - Observed discounts up to 60%+.
         - Products with moderate discounts (10–30%) performed better than those with extreme discounts.



    - Category Analysis.
         - Phone  & Tablets and Home Electronics dominate listings.
         - Some categories are oversaturated, suggesting sellers should focus on niches within electronics.



    - Customer ratings as indicators of trust and product success.
         - Verified ratings strongly correlated with higher prices (premium products often get better reviews).
         - Low-rated sellers struggled regardless of discounts.

    -  Correlation Matrix
         - Showed strong relationship between discount, current_price, and rating_number.

- For a detailed breakdown of the analysis, please refer to the full notebook: [Price_Optimization.ipynb]()

# Key Insights

- We created an interactive Tableau dashboard to present the results of the analysis in a clear and accessible way. Below are some of the findings:
     - Sellers should avoid extreme discounts; moderate discounts (10–30%) balance visibility and profitability.
     - Ratings matter: Products with higher verified ratings perform better, even at higher prices.
     - Phones & Electronics are profitable but crowded, niche categories offer better opportunities for new sellers.
     - A predictive approach to pricing reduces risk for new sellers entering competitive markets.

[View the Tableau Dashboard](https://public.tableau.com/app/profile/elizabeth.ogutu/viz/Booktwo_17595891616540/Dashboard1?publish=yes)



## Modeling

- The project applied machine learning models to:
    - Predict optimal product prices.
    - Provide sellers with recommendations on optimal pricing.

- Target Variable:current_price (what the customer pays).
- Features: original_price, discount, main_category, rating_number, verified_ratings, etc.

- Model used:
   - Linear Regression: Simple baseline model for price prediction.
   - Decision Tree / Random Forest: Captures non-linear relationships (e.g., how discounts interact with categories).
   - Gradient Boosting: More advanced model for better accuracy.

- We experimented with multiple models (e.g., regression-based and classification-based approaches), evaluated performance, and selected the one that balanced accuracy with interpretability.

- Evaluation matrix: 
   - R² Score: Measures how well the model explains variation in price.
   - MAE (Mean Absolute Error): Measures average difference between predicted and actual prices.

- Results
    - Tree-based models (Random Forest, Gradient Boosting) outperformed linear models.
    - Predictions were accurate enough to recommend competitive price bands by category.


## Deployment

- The project was deployed as a Flask web app and hosted on Render.
- For the Front end, we created a simple website where people can explore the project. The site has diffrent pages:
    - Home → welcoming page with project overview.
    - Data → a page describing the dataset used.
    - Research → key findings and insights.
    - Team → information about the contributors.
- There’s also a prediction form where a user can enter product details and instantly see the predicted price.

- The backend uses a Random Forest model trained on our dataset. The outcome is a live, user-friendly web app that makes predictions in real time.

🔗 [Explore the Price Predictor Tool](https://price-prediction-model-user-interface.onrender.com/)


## Conclusion
- This project shows ...... from exploring the dataset and extracting insights, to training a robust predictive model, and finally transforming it into a live, user-friendly web app.
- The result is a practical tool that allows anyone to input product details and instantly receive a predicted price, bridging the gap between data and real-world application. This highlights  can support better decision-making in e-commerce, such as pricing strategies, deal evaluation, and customer awareness.


## Conclusion  
- This project demonstrates the end-to-end process from exploring the dataset and extracting insights, to training a robust predictive model, and finally transforming it into a live, user-friendly web app.  
- The result is a practical tool that allows anyone to input product details and instantly receive a predicted price, effectively bridging the gap between data and real-world application. It also shows how machine learning can support better decision-making in e-commerce, such as pricing strategies, deal evaluation, and customer awareness.  

### Future Work
- While the project is fully functional, there’s room to expand and improve:
   - Extend beyond price prediction to demand forecasting or profit margin estimation.
   - Incorporate more features like brand popularity, seasonal effects, or customer demographics.

- In summary, this project is not just about predicting prices, it’s about showing how data can be transformed into real-world tools that empower smarter decisions in e-commerce.  
   
