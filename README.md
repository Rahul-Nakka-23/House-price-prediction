# 🏡 House Price Prediction 
A machine learning project to predict house prices using Linear Regression and Random Forest Regression models. The model is trained on a real-world dataset sourced from Kaggle and deployed via a Flask web application for user interaction.
# 📊 Features
✅ Predicts house prices based on multiple features
✅ Implements both Linear and Random Forest regression models
✅ Performs extensive data preprocessing and encoding
✅ Evaluates model performance with standard regression metrics
✅ Deploys the trained model using Flask
✅ Visualizes data and insights with Seaborn and Matplotlib
# 🧰 Technologies Used
- Python

- Pandas & NumPy

- Scikit-learn (Regression models & metrics)

- Seaborn & Matplotlib (Data visualization)

- Flask (Web deployment)

- Joblib (Model saving/loading)
# 📁 Dataset
- Source: https://www.kaggle.com/datasets/faisal012/hyderabad-house-price
- Contains features such as number of rooms, location, area, and other property characteristics.
# ⚙️ Workflow
  1. Data Preprocessing
     - Handled missing values
     - Encoded categorical features using LabelEncoder and OneHotEncoder
     - Used ColumnTransformer for efficient preprocessing
  2. Model Building
     - Applied Linear Regression
     - Applied Random Forest Regressoion
  3. Model Evaluation
     - Evaluated using MAE, MSE, RMSE, and R² Score
  5. Model Deployment
     - Trained models were saved using joblib
     - A simple Flask web app was developed to interact with the model
# 📈 Model Performance
## 🔹 Linear Regression
     Mean Absolute Error (MAE): 3,798,044.98
     Mean Squared Error (MSE): 85,642,229,711,146.75
     Root Mean Squared Error (RMSE): 9,254,308.71
     R² Score: 0.7744
## 🔹 Random Forest Regression
    Mean Absolute Error (MAE): 629,179.27
    Mean Squared Error (MSE): 19,911,524,559,047.23
    Root Mean Squared Error (RMSE): 4,462,233.14
    R² Score: 0.9476
✅ Random Forest outperformed Linear Regression, offering more accurate predictions with significantly lower error metrics.
# 🚀 Deployment
The project includes a Flask-based web interface where users can input property features and receive predicted prices. The backend loads the trained model using joblib and returns real-time predictions.
``` bash
pip install -r requirements.txt
python app.py
```
# 📱output 
![image](https://github.com/user-attachments/assets/c567c650-73a0-46b4-aeed-40183b3a81d8)


# 📌 Conclusion
This project demonstrates the use of regression algorithms to solve real-world prediction problems. The comparison between Linear and Random Forest models showcases how ensemble methods can greatly improve prediction accuracy.
# 🤝 Connect with Me

- [Github](https://github.com/Rahul-Nakka-23)
- [LinkedIn](https://www.linkedin.com/in/nakka-rahul/)


