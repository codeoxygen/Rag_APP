from flask import Blueprint, request, jsonify
from Services.helper_functions import PdfUtils
import PyPDF2
from flask import session


upload_pdf_bp = Blueprint('pdf', __name__)

@upload_pdf_bp.route("/upload_pdf" , methods=["POST"])
def upload_data():


    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})

    pdf_file = request.files['file']
    

    if pdf_file and pdf_file.filename.endswith('.pdf'):
        try:
            pdf_text = PdfUtils(pdf_file)  
            session["pdf_text"] = pdf_text
            return jsonify({'message': "Your File has been updated"})
        except :
            return jsonify({'error': 'Invalid PDF format'})