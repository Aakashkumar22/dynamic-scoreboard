import os
import pandas as pd
from flask import Flask, render_template, request, redirect, url_for, flash
import plotly.express as px
import plotly.io as pio
from werkzeug.utils import secure_filename
import plotly.express as px
import plotly.io as pio
from werkzeug.utils import secure_filename
import smtplib
from email.message import EmailMessage
import os
import pandas as pd
from flask import Flask, render_template, request, redirect, url_for, flash, send_file
import plotly.express as px
import plotly.io as pio
from werkzeug.utils import secure_filename
import smtplib
from email.message import EmailMessage

app = Flask(__name__)
app.secret_key = '116'  # For flash messages

# Folder to store uploaded files
UPLOAD_FOLDER = 'uploads/'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# CSV file for storing data
DATA_FILE = "scorecard_data.csv"
WEIGHT_FILE = "weights.csv"  # File for storing weights

# Ensure the CSV file exists with correct headers
if not os.path.exists(DATA_FILE):
    df = pd.DataFrame(columns=["Category", "Criteria", "Score"])
    df.to_csv(DATA_FILE, index=False)

# Ensure the weights file exists with correct headers
if not os.path.exists(WEIGHT_FILE):
    weight_df = pd.DataFrame(columns=["Category", "Weight"])
    weight_df.to_csv(WEIGHT_FILE, index=False)


@app.route('/')
def home():
    """Render the home page with data, but no visualizations yet."""
    data = pd.read_csv(DATA_FILE).fillna("")  # Prevent NaN values in the table
    return render_template('index.html', data=data.to_dict(orient="records"), bar_chart=None, pie_chart=None, radar_chart=None)


@app.route('/visualize_data', methods=['POST'])
def visualize_data():
    """Generate the visualizations when the 'Visualize Data' button is clicked."""
    data = pd.read_csv(DATA_FILE).fillna("")  # Prevent NaN values in the table
    weights = pd.read_csv(WEIGHT_FILE).set_index("Category")  # Load weights

    # Add weight to each row of data
    data["Weight"] = data["Category"].apply(lambda x: weights.loc[x, "Weight"] if x in weights.index else 1)

    # Calculate the weighted score for each row
    data["Weighted Score"] = data["Score"] * data["Weight"]
    
    # Summary Calculations
    total_score = data["Weighted Score"].sum()
    category_summary = data.groupby("Category").agg({"Weighted Score": "sum"}).reset_index()

    # Create Bar Chart for category-wise breakdown
    bar_fig = px.bar(category_summary, x="Category", y="Weighted Score", title="Category-wise Breakdown", labels={"Weighted Score": "Total Score"})
    bar_chart = pio.to_html(bar_fig, full_html=False)

    # Create Pie Chart for category distribution
    pie_fig = px.pie(category_summary, names="Category", values="Weighted Score", title="Category-wise Distribution")
    pie_chart = pio.to_html(pie_fig, full_html=False)

    # Create Radar Chart for category performance
    radar_fig = px.line_polar(category_summary, r="Weighted Score", theta="Category", line_close=True, title="Performance Across Categories")
    radar_chart = pio.to_html(radar_fig, full_html=False)

    return render_template(
        'index.html',
        data=data.to_dict(orient="records"),
        total_score=total_score,
        bar_chart=bar_chart,
        pie_chart=pie_chart,
        radar_chart=radar_chart
    )


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


@app.route('/set_weights', methods=['GET', 'POST'])
def set_weights():
    """Allow user to set dynamic weights for each category."""
    if request.method == 'POST':
        # Get weights from form and save to weights file
        category_weights = {
            "Productivity": request.form.get('productivity_weight', type=float),
            "Quality": request.form.get('quality_weight', type=float),
            "Timeliness": request.form.get('timeliness_weight', type=float)
        }
        weight_df = pd.DataFrame(list(category_weights.items()), columns=["Category", "Weight"])
        weight_df.to_csv(WEIGHT_FILE, index=False)
        flash("Weights updated successfully!", 'success')
        return redirect(url_for('home'))
    
    # Render the weight settings page
    return render_template('set_weights.html')

@app.route('/export/csv', methods=['POST'])
def export_csv():
    return send_file(DATA_FILE, as_attachment=True)

@app.route('/export/excel', methods=['POST'])
def export_excel():
    df = pd.read_csv(DATA_FILE)
    excel_path = "scorecard_data.xlsx"
    df.to_excel(excel_path, index=False)
    return send_file(excel_path, as_attachment=True)

@app.route('/export/pdf', methods=['POST'])
def export_pdf():
    from fpdf import FPDF
    df = pd.read_csv(DATA_FILE)
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    
    pdf.cell(200, 10, txt="Scorecard Data", ln=True, align='C')
    pdf.ln(10)
    
    for index, row in df.iterrows():
        pdf.cell(200, 10, txt=f"{row['Category']} - {row['Criteria']} - Score: {row['Score']}", ln=True)
    
    pdf_path = "scorecard_data.pdf"
    pdf.output(pdf_path)
    return send_file(pdf_path, as_attachment=True)

@app.route('/share', methods=['POST'])
def share():
    email = request.form['email']
    subject = "Shared Scorecard Data"
    body = "Please find the attached scorecard data."
    
    df = pd.read_csv(DATA_FILE)
    file_path = "scorecard_data.csv"
    df.to_csv(file_path, index=False)
    
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = "your-email@example.com"
    msg['To'] = email
    msg.set_content(body)
    
    with open(file_path, "rb") as f:
        msg.add_attachment(f.read(), maintype="text", subtype="csv", filename=file_path)
    
    try:
        with smtplib.SMTP('smtp.example.com', 587) as server:
            server.starttls()
            server.login("your-email@example.com", "your-password")
            server.send_message(msg)
        flash("Email sent successfully!", 'success')
    except Exception as e:
        flash(f"Error sending email: {str(e)}", 'danger')
    
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(port=90, debug=True)

