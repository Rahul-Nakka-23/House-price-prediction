from flask import Flask, render_template, request
import joblib
import pandas as pd
import os

app = Flask(__name__)

# Debug: Print current working directory
print("Current working directory:", os.getcwd())

try:
    model = joblib.load('house_price_rf_model.joblib')
    preprocessor = joblib.load('preprocessor.joblib')
    print("Model and preprocessor loaded successfully")
except Exception as e:
    print(f"Error loading model files: {e}")
    model = None
    preprocessor = None

@app.route('/', methods=['GET', 'POST'])
def predict():
    print("\nNew request - Method:", request.method)
    
    if request.method == 'POST':
        print("Form data received:", request.form)
        
        if not model or not preprocessor:
            error_msg = "Model not loaded. Please check server logs."
            print(error_msg)
            return render_template('index.html', 
                                   error=error_msg,
                                   show_prediction=False)
        
        try:
            # Get form data
            title = request.form.get('title')
            location = request.form.get('location')
            building_status = request.form.get('building_status')
            area = request.form.get('area')
            rate_input = request.form.get('rate_persqft')

            print(f"Input values - Title: {title}, Location: {location}, "
                  f"Status: {building_status}, Area: {area}, Rate Input: {rate_input}")
            
            # Validate required inputs
            if not all([title, location, building_status, area]):
                error_msg = "All fields except rate per sq.ft are required"
                print(error_msg)
                return render_template('index.html', 
                                       error=error_msg,
                                       show_prediction=False)
            
            try:
                area = float(area)
            except ValueError:
                error_msg = "Area must be a valid number"
                print(error_msg)
                return render_template('index.html', 
                                       error=error_msg,
                                       show_prediction=False)
            
            # Handle optional rate input
            if rate_input:
                try:
                    rate_persqft = float(rate_input)
                except ValueError:
                    error_msg = "Rate per sq.ft must be a number if provided"
                    print(error_msg)
                    return render_template('index.html', 
                                           error=error_msg,
                                           show_prediction=False)
            else:
                rate_persqft = 6000  # Default average rate
                print("Rate per sq.ft not provided. Using default:", rate_persqft)

            # Create input DataFrame
            input_data = pd.DataFrame({
                'title': [title],
                'location': [location],
                'building_status': [building_status],
                'rate_persqft': [rate_persqft],
                'area_insqft': [area]
            })
            print("Input DataFrame created:", input_data)
            
            # Preprocess and predict
            processed_input = preprocessor.transform(input_data)
            print("Input processed successfully")
            
            prediction = model.predict(processed_input)[0]
            prediction_lakhs = prediction / 100000
            print(f"Prediction made: {prediction_lakhs:.2f} Lakhs")
            
            return render_template('index.html', 
                                   prediction=f"₹{prediction_lakhs:,.2f} Lakhs",
                                   show_prediction=True)
        
        except Exception as e:
            error_msg = f"Prediction error: {str(e)}"
            print(error_msg)
            return render_template('index.html', 
                                   error=error_msg,
                                   show_prediction=False)
    
    return render_template('index.html', show_prediction=False)

if __name__ == '__main__':
    app.run(debug=True)
