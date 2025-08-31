from flask import Flask, request, render_template, jsonify, redirect, send_from_directory
import pandas as pd
import numpy as np
import pickle

# lode Databases
sym_des = pd.read_csv("datasets/symtoms_df.csv")
precautions = pd.read_csv("datasets/precautions_df.csv")
workout = pd.read_csv("datasets/workout_df.csv")
description = pd.read_csv("datasets/description.csv")
medications = pd.read_csv("datasets/medications.csv")
diets = pd.read_csv("datasets/diets.csv")

# Lode Models
svc = pickle.load(open('models/svc.pkl', 'rb'))



app = Flask(__name__)

# Serve CSS files from public folder
@app.route('/public/<path:filename>')
def public_files(filename):
    return send_from_directory('public', filename)

# History management
import json
import os
from datetime import datetime

def save_to_history(symptoms, disease):
    history_file = 'history.json'
    history_entry = {
        'symptoms': symptoms,
        'disease': disease,
        'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }
    
    if os.path.exists(history_file):
        with open(history_file, 'r') as f:
            history = json.load(f)
    else:
        history = []
    
    history.insert(0, history_entry)  # Add to beginning
    history = history[:50]  # Keep only last 50 entries
    
    with open(history_file, 'w') as f:
        json.dump(history, f, indent=2)

def get_history():
    history_file = 'history.json'
    if os.path.exists(history_file):
        with open(history_file, 'r') as f:
            return json.load(f)
    return []

def delete_history_entry(index):
    history_file = 'history.json'
    if os.path.exists(history_file):
        with open(history_file, 'r') as f:
            history = json.load(f)
        if 0 <= index < len(history):
            history.pop(index)
            with open(history_file, 'w') as f:
                json.dump(history, f, indent=2)
            return True
    return False

# Helper Functions
def generate_external_links(disease, medications, diet, workout, precautions):
    """Generate external links for various resources"""
    import urllib.parse
    
    links = {
        'wikipedia': f"https://en.wikipedia.org/wiki/{urllib.parse.quote(disease.replace(' ', '_'))}",
        'pharmeasy': f"https://pharmeasy.in/search/all?name={urllib.parse.quote(disease)}",
        'youtube_diet': f"https://www.youtube.com/results?search_query={urllib.parse.quote(f'{disease} diet food')}",
        'youtube_workout': f"https://www.youtube.com/results?search_query={urllib.parse.quote(f'{disease} exercises workout')}",
        'youtube_precaution': f"https://www.youtube.com/results?search_query={urllib.parse.quote(f'{disease} precautions prevention')}"
    }
    return links

def helper(dis):
    desc = description[description['Disease'] == dis]['Description']
    desc = " ".join([w for w in desc])

    pre = precautions[precautions['Disease'] == dis][['Precaution_1', 'Precaution_2', 'Precaution_3', 'Precaution_4']]
    pre = [col for col in pre.values]

    med = medications[medications['Disease'] == dis]['Medication']
    try:
        med = eval(med.iloc[0]) if len(med) > 0 else []
    except:
        med = []

    die = diets[diets['Disease'] == dis]['Diet']
    try:
        die = eval(die.iloc[0]) if len(die) > 0 else []
    except:
        die = []

    wrkout = workout[workout['disease'] == dis]['workout']
    wrkout = wrkout.values.tolist() if len(wrkout) > 0 else []

    # Generate external links
    external_links = generate_external_links(dis, med, die, wrkout, pre)
    
    return desc,pre,med,die,wrkout,external_links


# Input
symptoms_dict = {'itching': 0, 'skin_rash': 1, 'nodal_skin_eruptions': 2, 'continuous_sneezing': 3, 'shivering': 4, 'chills': 5, 'joint_pain': 6, 'stomach_pain': 7, 'acidity': 8, 'ulcers_on_tongue': 9, 'muscle_wasting': 10, 'vomiting': 11, 'burning_micturition': 12, 'spotting_ urination': 13, 'fatigue': 14, 'weight_gain': 15, 'anxiety': 16, 'cold_hands_and_feets': 17, 'mood_swings': 18, 'weight_loss': 19, 'restlessness': 20, 'lethargy': 21, 'patches_in_throat': 22, 'irregular_sugar_level': 23, 'cough': 24, 'high_fever': 25, 'sunken_eyes': 26, 'breathlessness': 27, 'sweating': 28, 'dehydration': 29, 'indigestion': 30, 'headache': 31, 'yellowish_skin': 32, 'dark_urine': 33, 'nausea': 34, 'loss_of_appetite': 35, 'pain_behind_the_eyes': 36, 'back_pain': 37, 'constipation': 38, 'abdominal_pain': 39, 'diarrhoea': 40, 'mild_fever': 41, 'yellow_urine': 42, 'yellowing_of_eyes': 43, 'acute_liver_failure': 44, 'fluid_overload': 45, 'swelling_of_stomach': 46, 'swelled_lymph_nodes': 47, 'malaise': 48, 'blurred_and_distorted_vision': 49, 'phlegm': 50, 'throat_irritation': 51, 'redness_of_eyes': 52, 'sinus_pressure': 53, 'runny_nose': 54, 'congestion': 55, 'chest_pain': 56, 'weakness_in_limbs': 57, 'fast_heart_rate': 58, 'pain_during_bowel_movements': 59, 'pain_in_anal_region': 60, 'bloody_stool': 61, 'irritation_in_anus': 62, 'neck_pain': 63, 'dizziness': 64, 'cramps': 65, 'bruising': 66, 'obesity': 67, 'swollen_legs': 68, 'swollen_blood_vessels': 69, 'puffy_face_and_eyes': 70, 'enlarged_thyroid': 71, 'brittle_nails': 72, 'swollen_extremeties': 73, 'excessive_hunger': 74, 'extra_marital_contacts': 75, 'drying_and_tingling_lips': 76, 'slurred_speech': 77, 'knee_pain': 78, 'hip_joint_pain': 79, 'muscle_weakness': 80, 'stiff_neck': 81, 'swelling_joints': 82, 'movement_stiffness': 83, 'spinning_movements': 84, 'loss_of_balance': 85, 'unsteadiness': 86, 'weakness_of_one_body_side': 87, 'loss_of_smell': 88, 'bladder_discomfort': 89, 'foul_smell_of urine': 90, 'continuous_feel_of_urine': 91, 'passage_of_gases': 92, 'internal_itching': 93, 'toxic_look_(typhos)': 94, 'depression': 95, 'irritability': 96, 'muscle_pain': 97, 'altered_sensorium': 98, 'red_spots_over_body': 99, 'belly_pain': 100, 'abnormal_menstruation': 101, 'dischromic _patches': 102, 'watering_from_eyes': 103, 'increased_appetite': 104, 'polyuria': 105, 'family_history': 106, 'mucoid_sputum': 107, 'rusty_sputum': 108, 'lack_of_concentration': 109, 'visual_disturbances': 110, 'receiving_blood_transfusion': 111, 'receiving_unsterile_injections': 112, 'coma': 113, 'stomach_bleeding': 114, 'distention_of_abdomen': 115, 'history_of_alcohol_consumption': 116, 'fluid_overload.1': 117, 'blood_in_sputum': 118, 'prominent_veins_on_calf': 119, 'palpitations': 120, 'painful_walking': 121, 'pus_filled_pimples': 122, 'blackheads': 123, 'scurring': 124, 'skin_peeling': 125, 'silver_like_dusting': 126, 'small_dents_in_nails': 127, 'inflammatory_nails': 128, 'blister': 129, 'red_sore_around_nose': 130, 'yellow_crust_ooze': 131}
# Output(prognosis)
diseases_list = {15: 'Fungal infection', 4: 'Allergy', 16: 'GERD', 9: 'Chronic cholestasis', 14: 'Drug Reaction', 33: 'Peptic ulcer diseae', 1: 'AIDS', 12: 'Diabetes ', 17: 'Gastroenteritis', 6: 'Bronchial Asthma', 23: 'Hypertension ', 30: 'Migraine', 7: 'Cervical spondylosis', 32: 'Paralysis (brain hemorrhage)', 28: 'Jaundice', 29: 'Malaria', 8: 'Chicken pox', 11: 'Dengue', 37: 'Typhoid', 40: 'hepatitis A', 19: 'Hepatitis B', 20: 'Hepatitis C', 21: 'Hepatitis D', 22: 'Hepatitis E', 3: 'Alcoholic hepatitis', 36: 'Tuberculosis', 10: 'Common Cold', 34: 'Pneumonia', 13: 'Dimorphic hemmorhoids(piles)', 18: 'Heart attack', 39: 'Varicose veins', 26: 'Hypothyroidism', 24: 'Hyperthyroidism', 25: 'Hypoglycemia', 31: 'Osteoarthristis', 5: 'Arthritis', 0: '(vertigo) Paroymsal  Positional Vertigo', 2: 'Acne', 38: 'Urinary tract infection', 35: 'Psoriasis', 27: 'Impetigo'}


# Model Prediction Function
def get_predicted_value(patient_symptoms):
    input_vector = np.zeros(len(symptoms_dict))

    for item in patient_symptoms:
        input_vector[symptoms_dict[item]] = 1
    return diseases_list[svc.predict([input_vector])[0]]

# Creating routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        symptoms = request.form.get('symptoms')
        user_symptoms = [s.strip() for s in symptoms.split(',') if s.strip()]
        user_symptoms = [sym.strip("[]' ") for sym in user_symptoms]
        
        # Filter out invalid symptoms
        valid_symptoms = [sym for sym in user_symptoms if sym in symptoms_dict]
        
        if not valid_symptoms:
            return render_template('index.html', error="Please enter valid symptoms from the dropdown list.")
        
        predicted_disease = get_predicted_value(valid_symptoms)
        desc, pre, med, die, wrkout, external_links = helper(predicted_disease)
        
        # Save to history
        save_to_history(valid_symptoms, predicted_disease)

        return render_template('index.html', predicted_disease=predicted_disease, dis_des=desc, dis_pre=pre, dis_med=med,dis_diet=die, dis_wrkout=wrkout, external_links=external_links)


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/history')
def history():
    history_data = get_history()
    return render_template('history.html', history=history_data)



@app.route('/api/symptoms')
def get_symptoms():
    symptoms_list = list(symptoms_dict.keys())
    return jsonify(symptoms_list)

@app.route('/show_history/<int:index>')
def show_history(index):
    history_data = get_history()
    if 0 <= index < len(history_data):
        entry = history_data[index]
        symptoms_str = ', '.join(entry['symptoms'])
        predicted_disease = entry['disease']
        desc, pre, med, die, wrkout, external_links = helper(predicted_disease)
        return render_template('index.html', predicted_disease=predicted_disease, dis_des=desc, dis_pre=pre, dis_med=med, dis_diet=die, dis_wrkout=wrkout, external_links=external_links, from_history=True)
    return redirect('/history')

@app.route('/delete_history/<int:index>')
def delete_history(index):
    delete_history_entry(index)
    return redirect('/history')

# pip instal repotlab
@app.route('/download_pdf')
def download_pdf():
    from flask import session, make_response
    try:
        from reportlab.lib.pagesizes import letter
        from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
        from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
        from reportlab.lib import colors
        from io import BytesIO
        
        # Get the last prediction from history
        history_data = get_history()
        if not history_data:
            return redirect('/')
        
        latest_entry = history_data[0]
        predicted_disease = latest_entry['disease']
        desc, pre, med, die, wrkout, external_links = helper(predicted_disease)
        
        # Create PDF
        buffer = BytesIO()
        doc = SimpleDocTemplate(buffer, pagesize=letter, leftMargin=36, rightMargin=36)
        styles = getSampleStyleSheet()
        story = []
        
        # Custom style for table content
        content_style = ParagraphStyle(
            'ContentStyle',
            parent=styles['Normal'],
            fontSize=9,
            leading=11,
            wordWrap='CJK'
        )
        
        # Title
        title = Paragraph("Medicine Recommendation Report", styles['Title'])
        story.append(title)
        story.append(Spacer(1, 12))
        
        # Helper function to format text
        def format_text(text, max_length=300):
            if isinstance(text, list):
                text = ', '.join(str(item) for item in text)
            text = str(text)
            if len(text) > max_length:
                text = text[:max_length] + '...'
            return Paragraph(text, content_style)
        
        # Create table data with Paragraphs for proper wrapping
        external_links_text = f"""Wikipedia: {external_links['wikipedia']}
Buy Medicine: {external_links['pharmeasy']}
Diet Videos: {external_links['youtube_diet']}
Workout Videos: {external_links['youtube_workout']}
Precaution Videos: {external_links['youtube_precaution']}"""
        
        data = [
            [Paragraph('<b>Category</b>', styles['Normal']), Paragraph('<b>Information</b>', styles['Normal'])],
            [Paragraph('<b>Predicted Disease</b>', content_style), Paragraph(predicted_disease, content_style)],
            [Paragraph('<b>Description</b>', content_style), format_text(desc, 400)],
            [Paragraph('<b>Precautions</b>', content_style), format_text([item for sublist in pre for item in sublist])],
            [Paragraph('<b>Medications</b>', content_style), format_text(med)],
            [Paragraph('<b>Workouts</b>', content_style), format_text(wrkout)],
            [Paragraph('<b>Diet</b>', content_style), format_text(die)],
            [Paragraph('<b>External Resources</b>', content_style), Paragraph(external_links_text, content_style)]
        ]
        
        # Create table with proper column widths
        available_width = letter[0] - 72  # Page width minus margins
        col1_width = available_width * 0.25  # 25% for category
        col2_width = available_width * 0.75  # 75% for information
        
        table = Table(data, colWidths=[col1_width, col2_width], repeatRows=1)
        table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.green),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 10),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('TOPPADDING', (0, 0), (-1, -1), 8),
            ('BOTTOMPADDING', (0, 1), (-1, -1), 8),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
            ('VALIGN', (0, 0), (-1, -1), 'TOP'),
            ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.lightgrey]),
        ]))
        
        story.append(table)
        doc.build(story)
        
        buffer.seek(0)
        response = make_response(buffer.getvalue())
        response.headers['Content-Type'] = 'application/pdf'
        response.headers['Content-Disposition'] = f'attachment; filename=medical_report_{predicted_disease.replace(" ", "_")}.pdf'
        
        return response
        
    except ImportError:
        return "PDF generation requires reportlab. Install with: pip install reportlab", 500
    except Exception as e:
        return f"Error generating PDF: {str(e)}", 500






# Python Main
if __name__ == "__main__":
    app.run(debug=True)


