import fitz
import pytesseract
from PIL import Image
from backendservices.upload_service.service import get_file_by_id


def extract_text(report_id: str):
    file_info = get_file_by_id(report_id)

    if not file_info:
        return {"error": f"Report ID '{report_id}' not found!"}

    filepath = file_info["filepath"]
    file_type = file_info["file_type"]
    file_name = file_info["file_name"]

    extracted_text = ""

    try:
        # PDF extraction
        if file_type == "application/pdf":
            pdf_document = fitz.open(filepath)

            for page in pdf_document:
                extracted_text += page.get_text()

            pdf_document.close()

        # Image OCR
        elif file_type in [
            "image/jpeg",
            "image/png",
            "image/jpg"
        ]:
            image = Image.open(filepath)
            extracted_text = pytesseract.image_to_string(image)

        else:
            return {"error": "Unsupported file type!"}

    except Exception as e:
        return {"error": f"Extraction failed: {str(e)}"}

    return {
        "report_id": report_id,
        "file_name": file_name,
        "file_type": file_type,
        "extracted_text": extracted_text.strip()
    }
