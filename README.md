# MediRec - Medicine Recommendation System

🏥 **AI-Powered Healthcare Solution for Disease Prediction and Medical Recommendations**

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-2.3.3-green.svg)](https://flask.palletsprojects.com)
[![Machine Learning](https://img.shields.io/badge/ML-SVM-orange.svg)](https://scikit-learn.org)
[![License](https://img.shields.io/badge/License-Educational-yellow.svg)](#)

## 🎯 Overview

MediRec is an intelligent web-based medicine recommendation system that uses Support Vector Machine (SVM) algorithms to predict diseases based on user symptoms and provides comprehensive medical guidance including medications, diet plans, workout routines, and precautionary measures.

**⚠️ Disclaimer:** This system is for educational and informational purposes only. Always consult healthcare professionals for medical advice.

## ✨ Key Features

- 🧠 **AI-Powered Predictions**: 95%+ accuracy using SVM algorithm
- 💊 **Comprehensive Recommendations**: Medications, diet, workouts, precautions
- 🔍 **Smart Symptom Input**: Autocomplete with 132 medical symptoms
- 📱 **Responsive Design**: Modern UI with dark/light theme support
- 📄 **PDF Reports**: Professional medical recommendation reports
- 🔗 **External Integration**: Wikipedia, YouTube, PharmEasy links
- 📊 **History Tracking**: Save and manage previous predictions
- 🎨 **Medical Theme**: Professional green color palette

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- pip package manager

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/username/medicine-recommendation-system.git
cd medicine-recommendation-system
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Run the application**
```bash
python main.py
```

4. **Open in browser**
```
http://localhost:5000
```

## 🛠️ Technology Stack

**Backend:**
- Python 3.8+
- Flask Framework
- Scikit-learn (SVM)
- Pandas & NumPy
- ReportLab (PDF generation)

**Frontend:**
- HTML5, CSS3, JavaScript
- Bootstrap 5
- FontAwesome Icons

**Data:**
- CSV datasets (132 symptoms, 41 diseases)
- JSON history management
- Pickle model serialization

## 📊 System Performance

- **Prediction Accuracy**: 95%+
- **Response Time**: <1 second
- **Supported Symptoms**: 132
- **Disease Categories**: 41
- **User Satisfaction**: 92%

## 👥 Team

**Computer Engineering (AI & ML) - PCCOE Pune**

- **Vrushabh Hirab** (125B2C005) - Data Analyst & System Integrator
- **Pushkar Bhoge** (125B2C006) - Frontend & UI/UX Designer  
- **Pranav Khade** (125B2C007) - Backend & ML Engineer

## 📁 Project Structure

```
medicine-recommendation-system/
├── main.py                 # Flask application
├── requirements.txt        # Dependencies
├── models/
│   └── svc.pkl            # Trained SVM model
├── datasets/
│   ├── symtoms_df.csv     # Symptoms data
│   ├── description.csv    # Disease descriptions
│   ├── precautions_df.csv # Precautions data
│   ├── medications.csv    # Medications data
│   ├── diets.csv         # Diet recommendations
│   └── workout_df.csv    # Workout suggestions
├── templates/
│   ├── index.html        # Main page
│   ├── about.html        # About page
│   ├── contact.html      # Contact page
│   └── history.html      # History page
├── public/
│   └── style.css         # Styling
├── static/
│   └── logo.jpg          # Logo image
└── docs/                 # Documentation
```

## 🔧 Usage

1. **Enter Symptoms**: Type symptoms using autocomplete suggestions
2. **Get Prediction**: Click "Get Recommendations" for AI analysis
3. **View Results**: See disease prediction with comprehensive recommendations
4. **Download Report**: Generate PDF report for medical records
5. **Check History**: Access previous predictions and results

## 📈 Machine Learning Details

**Algorithm**: Support Vector Machine (SVM)
- **Training Accuracy**: 97%
- **Validation Accuracy**: 95%
- **Test Accuracy**: 95%
- **Cross-Validation**: 94.5%

**Data Processing**:
- Binary encoding of 132 symptoms
- Feature vector creation for ML input
- Model serialization using Pickle

## 🎨 UI/UX Features

- **Green Medical Theme**: Professional healthcare color palette
- **Dark/Light Mode**: User preference support
- **Responsive Design**: Mobile-friendly interface
- **Autocomplete**: Smart symptom suggestions
- **Modal Dialogs**: Detailed information views
- **Professional Reports**: PDF generation capability

## 🔗 External Integrations

- **Wikipedia**: Disease information and medical details
- **YouTube**: Educational videos for diet, exercise, precautions
- **PharmEasy**: Direct medicine procurement links
- **FontAwesome**: Professional icon library

## 📚 Documentation

Comprehensive documentation available in `/docs/`:
- **Project Documentation** (15,000+ words)
- **Research Paper** (8,500+ words)
- **Presentation Slides** (22 slides)

## 🧪 Testing

- **Unit Testing**: Individual component validation
- **Integration Testing**: System interaction testing
- **User Acceptance Testing**: 50+ participants
- **Performance Testing**: Load and response time analysis

## 🚀 Future Enhancements

**Short-term:**
- Mobile applications (iOS/Android)
- Enhanced ML models (Random Forest, Neural Networks)
- Voice input functionality
- Multilingual support

**Long-term:**
- Deep learning implementation
- Computer vision for symptom detection
- Healthcare system integration
- Global expansion and localization

## 📄 License

This project is developed for educational purposes at Pimpri Chinchwad College of Engineering (PCCOE), Pune.

## 🤝 Contributing

This is an academic project. For collaboration or questions:
- **Email**: [team contact information]
- **Institution**: PCCOE Pune
- **Course**: Computer Engineering (AI & ML)

## 📞 Contact

- **Vrushabh Hirab**: vrushabh.hirab25@pccoepune.org
- **Pushkar Bhoge**: pushkar.bhoge25@pccoepune.org
- **Pranav Khade**: pranav.khade25@pccoepune.org

## 🙏 Acknowledgments

- Faculty advisors at PCCOE for guidance and support
- Open source community for tools and libraries
- Healthcare professionals for domain insights
- Test users for valuable feedback

---

**⭐ Star this repository if you found it helpful!**

*Bridging AI technology and healthcare accessibility through innovative machine learning solutions.*
