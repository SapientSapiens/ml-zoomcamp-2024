## Predicting Patient No-Shows: A Data-Driven Approach

No-shows at hospitals create significant challenges, wasting valuable resources and delaying care for other patients. For my midterm project in the **MLZoomcamp**, hosted by **DataTalksClub** and led by **Alexey Grigorev**, I tackled the problem of predicting appointment no-shows in Brazilian hospitals using machine learning techniques. Here’s an overview of my approach:

## The Challenge

The dataset used for this project, sourced from **Kaggle**, contains over **110,000** records with features like patient demographics, medical history, and appointment details. However, building an accurate prediction model faced several hurdles:

- **Imbalanced Data**: Around 80% of the appointments were attended, while 20% resulted in no-shows.
- **Feature Engineering**: Critical predictors, such as patient history (previous appointments and missed appointments), were derived from raw data.
- **Bias Mitigation**: Socioeconomic factors, including neighborhood demographics, required thoughtful processing to avoid introducing bias into the model.

## The Solution

After careful data cleaning, feature engineering, and hyperparameter optimization, I experimented with various models, such as **Logistic Regression**, **Random Forest**, and **XGBoost**. Here’s why **XGBoost** outperformed the others:

- **Accuracy**: XGBoost delivered an AUC of **0.748**, which was the best performance in predicting no-shows compared to other models.
- **Fairness**: The model prioritized medical and appointment-specific factors, reducing the influence of potentially biased socioeconomic data.

## Key Insights

- **Lead Time Matters**: The time between scheduling and the actual appointment is a strong predictor of no-shows.
- **Patient History is Crucial**: Patterns related to past missed appointments significantly improve the model's prediction accuracy.
- **Fairness in Engineering**: Ensuring that features were assessed for bias was essential to developing a balanced, fair model.

## Practical Applications

This model offers valuable tools for hospitals to:

- **Identify high-risk appointments** early and allocate resources more efficiently.
- **Optimize no-show management** by predicting appointment probabilities.
- **Enhance patient care** through personalized reminders or interventions.

## Conclusion

This project highlights how machine learning can be applied to solve real-world problems like reducing hospital no-shows. If you're interested in exploring the code and methodology, feel free to check out my **GitHub repository : midtermproject-2024-mlz** for more details.
