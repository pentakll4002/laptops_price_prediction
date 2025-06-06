# 📚 laptops_price_prediction
## Introduction
This project aims to predict laptop prices based on various technical specifications such as CPU, RAM, storage, GPU, etc.
We explore different regression models, perform evaluation, and select the best-performing model.

## Libraries Used
- numpy: for numerical computations

- pandas: for data manipulation and analysis

- seaborn: for statistical data visualization

- matplotlib: for plotting and visualization

- scikit-learn: for building machine learning models and preprocessing

- pickle: for saving trained models

- warnings: for handling warning messages

## Techniques
- EDA (Exploratory Data Analysis):

  - Analyze and understand the dataset.

  - Visualize distributions, correlations, and relationships using seaborn and matplotlib.

- Feature Engineering:

  - Transform categorical and numerical features to prepare for modeling.

- Model Building:

  - Algorithms used:

    - RandomForestRegressor
  
    - AdaBoostRegressor

    - GradientBoostingRegressor

    - LinearRegression

    - Ridge

    - Lasso

    - KNeighborsRegressor

    - DecisionTreeRegressor

- Model Evaluation:

  - Metrics used:

    - R2 Score (r2_score)

    - Mean Absolute Error (mean_absolute_error)

    - Mean Squared Error (mean_squared_error)

  - Hyperparameter Tuning:

    - Used RandomizedSearchCV to randomly search for the best hyperparameters for each model.
   
## Workflow
1. Load and explore the data.

2. Perform EDA to understand key patterns.

3. Preprocess the data: handle missing values, encoding, feature transformation.

4. Train multiple machine learning models.

5. Tune hyperparameters using RandomizedSearchCV.

6. Evaluate models using R2 score, MAE, and MSE.

7. Save the best model using pickle.

## How to Run
1. Clone the repository.

2. Install the required libraries:

```bash
pip install numpy pandas seaborn matplotlib scikit-learn
```
3. Run the Jupyter notebook or Python script step by step.
4. After training, the final model can be saved and used for predictions.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

   
