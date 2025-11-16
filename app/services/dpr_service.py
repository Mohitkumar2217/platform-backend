from app.utils.pdf_extractor import extract_text_from_pdf
from app.nlp.section_extractor import extract_sections
from app.nlp.inconsistency_checker import find_inconsistencies
from app.ml.feature_engineering import create_features
from app.ml.risk_predictor import predict_risk

async def process_dpr(file):
    # 1. Extract text from PDF
    text = await extract_text_from_pdf(file)

    #2. Extract sections (like budget, objective, timeline etc.)
    sections = extract_sections(text)

    #3. detect inconsistncies
    inconsistencies = find_inconsistencies(text, sections)
    
    # 4. Convert it innto ML features
    features = create_features(text, sections, inconsistencies)
    

    #5. Run ML model to get risk score
    risk = predict_risk(features)


    #6. Return everthing
    return {
        "raw_text": text,
        "sections": sections,
        "inconsistencies": inconsistencies,
        "features": features,
        "risk": risk
    }
