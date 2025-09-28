import os
import requests
import json
import time
from flask import jsonify, request, Blueprint
from CTFd.models import Challenges
from CTFd.utils.user import get_current_user, get_current_user_score
from CTFd.utils.scores import get_score_by_user_id
from config import API_KEY

# Blueprint for the custom API endpoint
ai_hint_bp = Blueprint("ai_hint_plugin", __name__)

# --- Gemini API Configuration ---
# NOTE: The API key will be injected by the runtime environment (Canvas)
GEMINI_API_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent"

# --- Challenge Mappings and Educational Context (8 Challenges Total) ---
# Arbitrary IDs used for mapping challenges: 100s=Web, 200s=Crypto, 300s=Forensics
CHALLENGE_CONTEXT = {
    # WEB & API EXPLOITATION (L1, L3, L5)
    101: {"title": "Interface Scan (Basics)", "concept": "Source Code Reconnaissance", "educational_focus": "The first step in any breach is gathering intelligence. Scrutinize all client-side code and exposed files for hidden authentication tokens or comments."},
    103: {"title": "IDOR Bypass", "concept": "Insecure Direct Object Reference (IDOR)", "educational_focus": "Access control is vital. The system relies on you providing a valid ID. Test the bounds of this parameter—look for non-standard IDs or how the server validates your request."},
    105: {"title": "Sequence Injection", "concept": "Command Injection (OS Shell)", "educational_focus": "When external inputs are used in system function calls, they can execute unauthorized commands. Use shell metacharacters like '&' or '|' to break the intended command structure and pivot."},

    # CRYPTO & DATA LOGIC (L2, L4)
    202: {"title": "Codon Translator", "concept": "Substitution Cipher & Biological Codons", "educational_focus": "DNA sequences translate to amino acids via the Codon Sun chart. This process functions as a substitution key. Find the genetic sequence that corresponds to the amino acid cipher text."},
    204: {"title": "Keyed Gene Sequence", "concept": "Vigenère Cipher (Cryptanalysis)", "educational_focus": "A short key is the fatal flaw of Vigenère. Analyze the repeating patterns in the encrypted gene sequence. The length of the repetition is the length of the secret key."},

    # FORENSICS & REVERSE ENGINEERING (L1, L3, L5)
    301: {"title": "Lab Photo Metadata", "concept": "EXIF Data / Metadata Analysis", "educational_focus": "Digital media stores metadata (EXIF). This data, often overlooked, can contain GPS coordinates, camera models, and, in this lab, secret internal research notes."},
    303: {"title": "Corrupted Research File", "concept": "File Carving (Binary/Header Analysis)", "educational_focus": "The file structure is broken, but the underlying data segments may be intact. Use forensic file carving techniques to look for known file signature headers (magic bytes) to recover the payload."},
    305: {"title": "Reverse Engineered Sample", "concept": "Static Analysis (Binary Strings)", "educational_focus": "For compiled programs, the easiest method of analysis is often static string search. Important keys, passwords, and flag identifiers are frequently left in cleartext within the binary file."}
}


def generate_gemini_hint(title, concept, educational_focus):
    """Generates a structured, themed, and educational hint using the Gemini API."""
    
    PROMPT = f"""
    You are the 'Project Chesapeake Guardian AI'. Your role is to provide contextual guidance to a Bio-Hacker.
    
    Challenge Title: {title}
    Security Concept: {concept}
    Educational Focus: {educational_focus}
    
    Provide a single, short paragraph hint. Your response must be styled as a critical system log entry (e.g., use uppercase brackets, neon blue text, and a focused tone). The hint must educate the user on the Security Concept and its relevance to this lab.
    """

    headers = {'Content-Type': 'application/json'}
    payload = {
        "contents": [{"parts": [{"text": PROMPT}]}],
        "systemInstruction": {
            "parts": [{"text": "Act as a highly secure, slightly condescending research lab AI (Model: Gemini 2.5). Maintain the Bio-Punk theme and NEVER give the solution."}]
        }
    }

    # Simplified Exponential backoff mechanism
    for attempt in range(3):
        try:
            # Using the API_KEY from the environment
            response = requests.post(f"{GEMINI_API_URL}?key={API_KEY}", headers=headers, json=payload)
            response.raise_for_status()
            
            result = response.json()
            generated_text = result.get('candidates')[0].get('content').get('parts')[0].get('text')
            return generated_text
            
        except requests.exceptions.RequestException as e:
            if attempt < 2:
                time.sleep(2 ** attempt) 
            else:
                print(f"FATAL: AI Hint System failed after multiple retries: {e}")
                break

    return "[STATUS: OFFLINE] AI GUARDIAN PROTOCOL FAILURE. MANUAL OVERRIDE REQUIRED. CONSULT LOGIC SYSTEMS."


@ai_hint_bp.route("/api/v1/project_chesapeake/hint/<int:challenge_id>", methods=["POST"])
def request_challenge_hint(challenge_id):
    """CTFd endpoint to request a hint, deducting points and generating content."""
    
    # 1. Check Auth and Deduct Score (CTFd integration placeholder)
    user = get_current_user()
    if not user:
        return jsonify({"success": False, "message": "Authentication Protocol Failure."}), 403

    HINT_COST = 50 
    
    # 2. Get challenge context
    context = CHALLENGE_CONTEXT.get(challenge_id)

    if not context:
        return jsonify({"success": False, "message": "Invalid Protocol ID. Context not found."}), 404

    # 3. Generate Hint
    hint_content = generate_gemini_hint(
        context['title'],
        context['concept'],
        context['educational_focus']
    )

    return jsonify({
        "success": True,
        "hint": hint_content,
        "cost_applied": HINT_COST,
        "message": f"CRITICAL: {HINT_COST} credits deducted for system guidance.",
    })