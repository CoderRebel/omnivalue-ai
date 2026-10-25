# OmniValue.AI — Used Device Price Predictor

OmniValue.AI is a machine learning web application that estimates the resale price of a used device based on its specifications, age, and usage history.

The project combines a Flask backend, a trained regression model, and a responsive web interface to provide price predictions through a simple form.

## Features

- **Used-device price prediction** based on device specifications and usage.
- **Multiple regression models** evaluated during training, including Linear Regression, Random Forest, and Extra Trees.
- **Data preprocessing** using imputation for missing values and one-hot encoding for categorical features.
- **Responsive web interface** designed for desktop and mobile browsers.
- **Prediction API** powered by Flask.
- **Model persistence** using Joblib for loading the trained model without retraining on each request.

## Tech Stack

- **Language:** Python
- **Machine Learning:** scikit-learn
- **Backend:** Flask
- **Frontend:** HTML, Tailwind CSS, JavaScript
- **Data Processing:** pandas
- **Model Storage:** Joblib
- **Deployment:** Render

## Input Features

The application accepts the following device information:

- Device brand and operating system
- Screen size
- 4G and 5G connectivity
- Rear and front camera megapixels
- Internal storage and RAM
- Battery capacity and device weight
- Release year
- Number of days used

## Project Structure

```text
omnivalue-ai/
├── app.py
├── index.html
├── best_price_model.joblib
└── requirements.txt
```

The training scripts and dataset are used during development and are not required to serve predictions when the saved model is available.

## Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/omnivalue-ai.git
cd omnivalue-ai
```

Replace `YOUR_USERNAME` with your GitHub username.

### 2. Create and activate a virtual environment

```bash
python -m venv .venv
```

On Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Start the application

```bash
python app.py
```

Open the local address shown in the terminal in your browser. For a Flask app using the default development server, this is commonly `http://127.0.0.1:5000`.

## Deployment

The application can be deployed as a Python web service on Render.

Typical deployment settings:

- **Build command:** `pip install -r requirements.txt`
- **Start command:** `gunicorn app:app`

After deployment, the hosting provider supplies a public URL that can be opened on supported mobile and desktop browsers.

## Important Note About Price Estimates

The INR labels currently used for training were derived by transforming normalized price values with a formula. They have **not been independently verified against actual Indian resale-market transactions**.

Consequently, predictions should be treated as experimental estimates based on the training dataset, not as verified market valuations or guaranteed selling prices. The model's performance reflects the quality and limitations of those training labels.

## Future Improvements

- Train and evaluate the model using verified Indian used-device sale prices.
- Add model evaluation metrics and clearer prediction uncertainty.
- Expand device and brand coverage.
- Improve validation and user experience.
- Monitor prediction performance on real-world data.

## Author

Developed as a machine learning portfolio project to explore data preprocessing, regression modelling, model evaluation, and web application deployment.
By Rajeev Menaria
