APP_NAME = "inventory-api"
API_VERSION = "v2"

def service_info():
    return {
<<<<<<< HEAD
        "service": APP_NAME,
        "version": API_VERSION
=======
        "name": APP_NAME,
        "version": API_VERSION,
        "health": "ok"
>>>>>>> source/feature/health-check
    }
