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
- **Submit Data** : Choose a category, enter the criteria, and provide the score. Click the Submit button. ✍️
- **Upload File**: Upload a CSV or Excel file containing performance data. 📂
- **Set Weights**: Update the weights for each category (Productivity, Quality, Timeliness) to adjust the score calculation. ⚖️
- **Visualize Data**: Click the Visualize Data button to view your data in bar, pie, and radar chart formats. 📊
- **Export**: Export your scorecard data in your preferred format (CSV, Excel, PDF). 💾
- **Share via Email**: Enter an email address and click Send Email to share the scorecard with the recipient. 📧

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
## Output
## Data Input Interface Upload files via Upload Option.
<img width="524" alt="image" src="https://github.com/user-attachments/assets/310c2914-9d3c-4294-9232-f27f5b4a45d6" />
<img width="497" alt="image" src="https://github.com/user-attachments/assets/1166e29c-09b2-4919-b453-fa4f301ea791" />

## Upload data manually.
<img width="524" alt="image" src="https://github.com/user-attachments/assets/e222725d-798c-41dc-bdd9-0c90e2578159" />
<img width="797" alt="image" src="https://github.com/user-attachments/assets/b73e2426-0cc8-4032-ba13-8d959efe8e3a" />

## Dynamic Customization of weights.
<img width="565" alt="image" src="https://github.com/user-attachments/assets/0bc8d79d-b641-4c9e-9843-96770a86b061" />

## Data Visualization.
<img width="497" alt="image" src="https://github.com/user-attachments/assets/a45ac3c1-17b8-4c5f-a351-21c004842efd" />
<img width="698" alt="image" src="https://github.com/user-attachments/assets/0a66e5c0-4be5-43ac-af91-f6d2e097e87c" />
<img width="723" alt="image" src="https://github.com/user-attachments/assets/4792bdbc-210a-4e3b-9f79-f6d4e6d6a73e" />
<img width="652" alt="image" src="https://github.com/user-attachments/assets/b4650be3-c1dd-47d2-91db-445e4ff7276f" />

## Export Feature.
<img width="878" alt="image" src="https://github.com/user-attachments/assets/0c931f4a-c351-4b66-ba92-eb5a30d7e6c2" />
<img width="542" alt="image" src="https://github.com/user-attachments/assets/5c152b91-7130-46d2-8d4a-4bb20ac141ce" />

## Sharing Feature.
<img width="449" alt="image" src="https://github.com/user-attachments/assets/01043ba4-ac0e-4396-a23f-dda06466502a" />














## Future Improvements 🚀

- **User Authentication**: Add login and user management for personalized scorecards 🔒.
- **Additional Chart Types**: Add more types of data visualizations like line charts 📈.
- **Mobile Support**: Make the UI responsive for better mobile support 📱.
- **Enhanced File Parsing**: Improve support for various file formats (e.g., .txt, .json) 📊.


## License 📝
This project is licensed under the MIT License - see the LICENSE file for details.

Feel free to modify and expand upon this README to fit any additional features or customizations you've made to the project! ✨

## Contributions: Contributions are welcome! Feel free to submit issues, fork the repo, and open pull requests. 🙌
