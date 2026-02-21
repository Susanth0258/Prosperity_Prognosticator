# Prosperity Prognosticator 🚀

**Unlock the Future of Your Startup with AI-Driven Success Prediction**

"Prosperity Prognosticator" is a Machine Learning-powered web application designed to forecast the outcome of startups. By analyzing key metrics like funding rounds, milestones, and relationships, the system predicts whether a startup is likely to be **Acquired (Success)** or **Closed (Failure)**.

![Prosperity Prognosticator Header](https://via.placeholder.com/800x400?text=Prosperity+Prognosticator+App+Preview)
*(Note: Replace this placeholder with an actual screenshot of your application)*

## ✨ Key Features
- **AI-Driven accuracy**: Uses a robust Random Forest Classifier trained on historical startup data.
- **Instant Predictions**: Get real-time outcomes based on 9 critical business metrics.
- **Modern UI**: A sleek, dark-themed interface built with glassmorphism aesthetics.
- **Data-Backed Insights**: Helps investors and founders make objective, data-driven decisions.

## 🛠️ Tech Stack
- **Frontend**: HTML5, CSS3 (Custom Glassmorphism styles)
- **Backend**: Python, Flask
- **ML Engine**: Scikit-Learn, Pandas, NumPy
- **Model**: Random Forest Classifier

## 📊 Prediction Metrics
The model analyzes the following parameters to generate success forecasts:
1. **Relationships**: Number of professional connections.
2. **Funding Rounds**: Total number of investment rounds.
3. **Total Funding (USD)**: Cumulative capital raised.
4. **Milestones**: Number of key achievements reached.
5. **Avg. Participants**: Mean number of investors per round.
6. **Age at First Funding**: Years from startup birth to first investment.
7. **Age at Last Funding**: Years from startup birth to last investment.
8. **Age at First Milestone**: Years from startup birth to first key milestone.
9. **Age at Last Milestone**: Years from startup birth to last key milestone.

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- Required Libraries: `flask`, `numpy`, `pandas`, `scikit-learn`

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Susanth0258/Prosperity_Prognosticator.git
   cd Prosperity_Prognosticator
   ```
2. Install dependencies:
   ```bash
   pip install flask pandas scikit-learn numpy
   ```
3. Run the application:
   ```bash
   python app/app.py
   ```
4. Open your browser and navigate to `http://127.0.0.1:5000`

## 📂 Project Structure
- `app/`: Contains the Flask application logic and templates.
- `dataset/`: Training data (`startup_data.csv`).
- `models/`: Pre-trained model (`model.pkl`).
- `train_model.py`: Script for retraining the ML model.

## 📝 License
This project is open-source. Feel free to contribute and enhance the model accuracy!

---
Built with ❤️ by [Your Name/Repo Owner]
