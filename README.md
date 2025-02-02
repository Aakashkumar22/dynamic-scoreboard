# Dynamic Scorecard Tool 🎯📊

Welcome to the **Dynamic Scorecard Tool**! 🚀 This web-based application helps evaluate performance based on multiple criteria. It allows users to submit data, visualize results in various chart formats, and share scorecards via email. Plus, it supports uploading CSV/Excel files and exporting scorecards in multiple formats like CSV, Excel, and PDF.


## Features 🌟

- **Data Submission**: Submit performance data, including category, criteria, and score. 📝
- **File Upload**: Upload performance data from CSV or Excel files. 📂
- **Category Weights**: Set weights for categories (Productivity, Quality, Timeliness) to adjust score calculations. ⚖️
- **Data Visualization**: Visualize performance data with bar charts 📊, pie charts 🍰, and radar charts 🕹️.
- **Export Options**: Export the scorecard data in CSV, Excel, or PDF formats. 💾
- **Email Sharing**: Share the scorecard via email with any recipient. 📧

## Technologies Used ⚙️

- **Frontend**: HTML, CSS 🌐
- **Backend**: Python (Flask), Flask-Mail 🐍
- **Data Visualization**: Chart.js (Bar, Pie, Radar charts) 📈
- **File Upload**: CSV, Excel files 📥
- **Email Service**: Gmail (via Flask-Mail) 📬

## Setup 🛠️

### Prerequisites

Before running the application, make sure you have the following installed:

- Python 3.x 🐍
- Flask 🧪
- Flask-Mail 📧

Install the required libraries using the following command:


## Running the Application 🚀##
Clone the repository:
** git clone <repository-url> ** 
**cd <repository-folder> ***


python app.py
** Open your browser and go to http://127.0.0.1:5000/ to access the application.**

## Environment Variables 🔐
Set up the following environment variables for Gmail to send emails:

## MAIL_USERNAME: Your Gmail email address 📧
## MAIL_PASSWORD: Your Gmail password or app-specific password (if 2-step verification is enabled) 🔑
You can set these variables directly in your code or use a .env file with a library like python-dotenv to manage environment variables.

## How to Use 🎯
**Submit Data** : Choose a category, enter the criteria, and provide the score. Click the Submit button. ✍️
**Upload File**: Upload a CSV or Excel file containing performance data. 📂
**Set Weights**: Update the weights for each category (Productivity, Quality, Timeliness) to adjust the score calculation. ⚖️
**Visualize Data**: Click the Visualize Data button to view your data in bar, pie, and radar chart formats. 📊
**Export**: Export your scorecard data in your preferred format (CSV, Excel, PDF). 💾
**Share via Email**: Enter an email address and click Send Email to share the scorecard with the recipient. 📧

## File Structure 📁
bash
Copy
Edit
/project-folder
    /templates
        index.html         # Main HTML template
    /static
        /css
            style.css      # Custom CSS
    app.py                  # Main Flask app
    requirements.txt        # Python dependencies



## Future Improvements 🚀

- **User Authentication**: Add login and user management for personalized scorecards 🔒.
- **Additional Chart Types**: Add more types of data visualizations like line charts 📈.
- **Mobile Support**: Make the UI responsive for better mobile support 📱.
- **Enhanced File Parsing**: Improve support for various file formats (e.g., .txt, .json) 📊.


## License 📝
This project is licensed under the MIT License - see the LICENSE file for details.

Feel free to modify and expand upon this README to fit any additional features or customizations you've made to the project! ✨

## Contributions: Contributions are welcome! Feel free to submit issues, fork the repo, and open pull requests. 🙌
