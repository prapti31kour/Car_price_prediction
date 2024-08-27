from flask import Flask, render_template, request, jsonify
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import numpy as np

app = Flask(__name__)

# Load and prepare the dataset
df = pd.read_csv('house_data.txt')
X = df[['Bedrooms', 'SquareFootage', 'Location']]
y = df['Price']

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

@app.route('/')
def index():
    return render_template('index.html')

# @app.route('/predict', methods=['POST'])
# def predict():
#     data = request.get_json()
#     bedrooms = int(data['bedrooms'])
#     square_footage = int(data['square_footage'])
#     location = int(data['location'])
    
#     # Predict the price using the model
#     input_data = np.array([[bedrooms, square_footage, location]])
#     predicted_price = model.predict(input_data)[0]
    
#     return jsonify({'predicted_price': predicted_price})

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        print("Received data:", data)  # Debug print
        bedrooms = int(data['bedrooms'])
        square_footage = int(data['square_footage'])
        location = int(data['location'])
        
        # Predict the price using the model
        input_data = np.array([[bedrooms, square_footage, location]])
        predicted_price = model.predict(input_data)[0]
        print("Predicted price:", predicted_price)  # Debug print
        
        return jsonify({'predicted_price': predicted_price})
    except Exception as e:
        print("Error:", e)
        return jsonify({'error': str(e)})


if __name__ == '__main__':
    app.run(debug=True)
