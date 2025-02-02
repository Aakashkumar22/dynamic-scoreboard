import os
import pandas as pd
from flask import Flask, render_template, request, redirect, url_for, flash
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = '116'  # For flash messages

# Folder to store uploaded files
UPLOAD_FOLDER = 'uploads/'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# CSV file for storing data
DATA_FILE = "scorecard_data.csv"

# Ensure the CSV file exists with correct headers
if not os.path.exists(DATA_FILE):
    df = pd.DataFrame(columns=["Category", "Criteria", "Score"])
    df.to_csv(DATA_FILE, index=False)


@app.route('/')
def home():
    ""Render the home page and display stored data."""
    data = pd.read_csv(DATA_FILE).fillna("")  # Prevent NaN values in the table
    return render_template('index.html', data=data.to_dict(orient="records"))


@app.route('/submit', methods=['POST'])
def submit():
    """Handle manual data entry submission."""
    try:
        category = request.form['category'].strip()
        criteria = request.form['criteria'].strip()
        score = request.form['score'].strip()

        # Validate input data
        if not category or not criteria or not score:
            flash("All fields are required!", "danger")
            return redirect(url_for('home'))

        # Convert score to float
        score = float(score)

        # Read existing data
        df = pd.read_csv(DATA_FILE)

        # Append new data properly
        new_row = pd.DataFrame([[category, criteria, score]], columns=["Category", "Criteria", "Score"])
        df = pd.concat([df, new_row], ignore_index=True)
        
        # Save updated data
        df.to_csv(DATA_FILE, index=False)

        flash(f"Data submitted successfully! Category: {category}, Criteria: {criteria}, Score: {score}", 'success')
    except ValueError:
        flash("Invalid score! Please enter a valid number.", "danger")
    except Exception as e:
        flash(f"Error: {str(e)}", 'danger')

    return redirect(url_for('home'))


@app.route('/upload', methods=['POST'])
def upload_file():
    """Handle CSV/Excel file uploads."""
    try:
        if 'file' not in request.files:
            flash("No file part", 'danger')
            return redirect(request.url)
        
        file = request.files['file']
        if file.filename == '':
            flash("No selected file", 'danger')
            return redirect(request.url)
        
        if file and (file.filename.endswith('.csv') or file.filename.endswith('.xlsx')):
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(file.filename))
            file.save(filepath)

            # Load and append data to existing CSV
            if file.filename.endswith('.csv'):
                data = pd.read_csv(filepath)
            elif file.filename.endswith('.xlsx'):
                data = pd.read_excel(filepath)

            # Ensure correct columns
            if not set(["Category", "Criteria", "Score"]).issubset(data.columns):
                flash("Invalid file format! Ensure columns: Category, Criteria, Score", 'danger')
                return redirect(url_for('home'))

            # Read existing data
            df = pd.read_csv(DATA_FILE)

            # Append new data and save
            df = pd.concat([df, data], ignore_index=True)
            df.to_csv(DATA_FILE, index=False)

            flash("File uploaded and data processed successfully!", 'success')
        else:
            flash("Invalid file format. Please upload a CSV or Excel file.", 'danger')
    except Exception as e:
        flash(f"Error: {str(e)}", 'danger')

    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(port=90, debug=True)


