import requests
from decouple import config
import logging

logger = logging.getLogger(__name__)
# Rancher-specific settings
RANCHER_METADATA_URL = config("RANCHER_METADATA_URL", "http://rancher-metadata")


def get_rancher_service_info():
    """Helper to get service info from Rancher metadata"""
    try:
        response = requests.get(f"{RANCHER_METADATA_URL}/2015-12-19/self/service")
        return response.json()
    except Exception as e:
        logger.exception(e)
        return {}
