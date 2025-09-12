# -*- coding: utf-8 -*-
"""
API Handler Module - Handles communication with external APIs
"""

import requests
from config import FDA_API_URL


def get_drug_info_from_api(drug_name: str):
    """
    Fetch drug information from the openFDA API.

    Args:
        drug_name (str): The generic name of the drug to search.

    Returns:
        dict | None: Dictionary containing drug details if found, otherwise None.
    """
    try:
        # Build the API request URL
        url = f"{FDA_API_URL}?search=generic_name:{drug_name}&limit=1"
        response = requests.get(url, timeout=10)
        data = response.json()

        # Check if results exist
        if "results" in data:
            drug_info = data["results"][0]
            return {
                "brand_name": drug_info.get("openfda", {}).get("brand_name", ["Not Available"])[0],
                "generic_name": drug_info.get("openfda", {}).get("generic_name", ["Not Available"])[0],
                "manufacturer": drug_info.get("openfda", {}).get("manufacturer_name", ["Not Available"])[0],
                "purpose": drug_info.get("purpose", ["Not Available"])[0],
                "warnings": drug_info.get("warnings", ["Not Available"])[0],
                "dosage": drug_info.get("dosage_and_administration", ["Not Available"])[0],
            }

    except Exception as e:
        print(f"Error fetching drug info: {e}")

    return None
