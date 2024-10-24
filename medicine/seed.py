from faker import Faker
import random
from .models import *

medicine_list = [
  {
    "name": "Paracetamol",
    "generic_name": "Acetaminophen",
    "manufacturer": "Medico Pharma",
    "description": "Effective for relieving mild to moderate pain and fever."
  },
  {
    "name": "Amoxicillin",
    "generic_name": "Amoxicillin Trihydrate",
    "manufacturer": "Healix Pharmaceuticals",
    "description": "A broad-spectrum antibiotic used for bacterial infections."
  },
  {
    "name": "Ibuprofen",
    "generic_name": "Ibuprofen",
    "manufacturer": "Global Remedies",
    "description": "Used for relieving pain, inflammation, and reducing fever."
  },
  {
    "name": "Cetirizine",
    "generic_name": "Cetirizine Hydrochloride",
    "manufacturer": "PureHealth Pharma",
    "description": "Antihistamine used for treating allergic reactions and hay fever."
  },
  {
    "name": "Metformin",
    "generic_name": "Metformin Hydrochloride",
    "manufacturer": "Diabetica Labs",
    "description": "Used for managing blood sugar levels in type 2 diabetes."
  },
  {
    "name": "Aspirin",
    "generic_name": "Acetylsalicylic Acid",
    "manufacturer": "Bayer HealthCare",
    "description": "Pain reliever and anti-inflammatory; also reduces risk of heart attack."
  },
  {
    "name": "Lisinopril",
    "generic_name": "Lisinopril",
    "manufacturer": "HeartCure Pharmaceuticals",
    "description": "Commonly used for managing high blood pressure and heart failure."
  },
  {
    "name": "Omeprazole",
    "generic_name": "Omeprazole Magnesium",
    "manufacturer": "DigestiveAid Pharma",
    "description": "Used to reduce stomach acid and treat GERD."
  },
  {
    "name": "Simvastatin",
    "generic_name": "Simvastatin",
    "manufacturer": "Cardio Health Inc.",
    "description": "Cholesterol-lowering drug that reduces the risk of heart disease."
  },
  {
    "name": "Losartan",
    "generic_name": "Losartan Potassium",
    "manufacturer": "HealthFirst Pharma",
    "description": "Used to treat high blood pressure and protect the kidneys in diabetic patients."
  },
  {
    "name": "Levothyroxine",
    "generic_name": "Levothyroxine Sodium",
    "manufacturer": "ThyroMed Pharmaceuticals",
    "description": "Used to treat hypothyroidism (underactive thyroid)."
  },
  {
    "name": "Atorvastatin",
    "generic_name": "Atorvastatin Calcium",
    "manufacturer": "LipidCare Labs",
    "description": "Helps lower bad cholesterol and fats in the blood."
  },
  {
    "name": "Clindamycin",
    "generic_name": "Clindamycin Phosphate",
    "manufacturer": "BioLife Pharmaceuticals",
    "description": "Used to treat bacterial infections in the skin, lungs, and internal organs."
  },
  {
    "name": "Doxycycline",
    "generic_name": "Doxycycline Hyclate",
    "manufacturer": "Sunbeam Labs",
    "description": "An antibiotic for various bacterial infections, including respiratory tract infections."
  },
  {
    "name": "Gabapentin",
    "generic_name": "Gabapentin",
    "manufacturer": "NeuroPharm",
    "description": "Used for treating nerve pain and seizures."
  },
  {
    "name": "Azithromycin",
    "generic_name": "Azithromycin Dihydrate",
    "manufacturer": "Zithro Pharmaceuticals",
    "description": "Antibiotic commonly used for respiratory infections and STIs."
  },
  {
    "name": "Pantoprazole",
    "generic_name": "Pantoprazole Sodium",
    "manufacturer": "Stomach Relief Inc.",
    "description": "Treats acid reflux and prevents damage to the esophagus."
  },
  {
    "name": "Tramadol",
    "generic_name": "Tramadol Hydrochloride",
    "manufacturer": "PainFree Labs",
    "description": "Used for treating moderate to severe pain."
  },
  {
    "name": "Sertraline",
    "generic_name": "Sertraline Hydrochloride",
    "manufacturer": "MoodCare Pharma",
    "description": "Antidepressant used to treat depression, anxiety, and PTSD."
  },
  {
    "name": "Ciprofloxacin",
    "generic_name": "Ciprofloxacin Hydrochloride",
    "manufacturer": "Infectio Cure Inc.",
    "description": "Broad-spectrum antibiotic used for treating bacterial infections."
  },
  {
    "name": "Hydrochlorothiazide",
    "generic_name": "Hydrochlorothiazide",
    "manufacturer": "CardioAid Pharmaceuticals",
    "description": "Diuretic used to treat high blood pressure and fluid retention."
  },
  {
    "name": "Furosemide",
    "generic_name": "Furosemide",
    "manufacturer": "AquaHealth Labs",
    "description": "A loop diuretic used to treat fluid buildup and swelling due to heart failure."
  },
  {
    "name": "Amlodipine",
    "generic_name": "Amlodipine Besylate",
    "manufacturer": "VasoMed Pharma",
    "description": "Calcium channel blocker used to treat high blood pressure and angina."
  },
  {
    "name": "Fluoxetine",
    "generic_name": "Fluoxetine Hydrochloride",
    "manufacturer": "MindCare Pharma",
    "description": "Used to treat depression, OCD, and certain eating disorders."
  },
  {
    "name": "Warfarin",
    "generic_name": "Warfarin Sodium",
    "manufacturer": "Anticoagulation Pharma",
    "description": "An anticoagulant (blood thinner) used to prevent blood clots."
  },
  {
    "name": "Prednisone",
    "generic_name": "Prednisone",
    "manufacturer": "CorticoPharm",
    "description": "A corticosteroid used to treat inflammation, allergies, and immune disorders."
  },
  {
    "name": "Metoprolol",
    "generic_name": "Metoprolol Tartrate",
    "manufacturer": "CardioPro Labs",
    "description": "Used to treat high blood pressure, chest pain, and heart failure."
  },
  {
    "name": "Spironolactone",
    "generic_name": "Spironolactone",
    "manufacturer": "ElectroBalance Pharma",
    "description": "Diuretic used to treat heart failure, high blood pressure, and edema."
  },
  {
    "name": "Alprazolam",
    "generic_name": "Alprazolam",
    "manufacturer": "AnxioFree Pharmaceuticals",
    "description": "Used to treat anxiety and panic disorders."
  },
  {
    "name": "Nitrofurantoin",
    "generic_name": "Nitrofurantoin",
    "manufacturer": "UTICure Pharma",
    "description": "Antibiotic used to treat urinary tract infections."
  }
]

fake = Faker()
def seed_db(n=30):
    try:
        for i in range(0, n):
            name = medicine_list[i]['name']
            generic_name = medicine_list[i]['generic_name']
            manufacturer = medicine_list[i]['manufacturer']
            description = medicine_list[i]['description']
            price = random.randint(100, 1000)
            batch_number = fake.bothify( text = 'batch_no: ???#####')
            form = random.choice(['Tablet', 'Capsule', 'Syrup'])
            stock_quantity = random.randint(100, 5000)

            MedicineModel.objects.create(
                name = name,
                generic_name = generic_name,
                manufacturer = manufacturer,
                description = description,
                price = price,
                batch_number = batch_number,
                form = form,
                stock_quantity = stock_quantity
                )

    except Exception as e:
        print(e)


