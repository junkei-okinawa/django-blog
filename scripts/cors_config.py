import os
from pathlib import Path

from google.cloud import storage
from google.oauth2 import service_account

from dotenv import load_dotenv

# load .env file
BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(verbose=True)
dotenv_path = BASE_DIR / ".env"
load_dotenv(dotenv_path)

# load credentials
gs_secret_file_path = os.environ.get("GS_SECRET_KEY_PATH")
if not gs_secret_file_path:
    raise ValueError("GS_SECRET_KEY_PATH is not set.")
GS_CREDENTIALS = service_account.Credentials.from_service_account_file(
    os.path.join(BASE_DIR, gs_secret_file_path)
)

# get origin urls
CLOUDRUN_SERVICE_URL = os.environ.get("CLOUDRUN_SERVICE_URL")
LOCAL_DOMAIN = os.environ.get("LOCAL_DOMAIN")


def cors_configuration(bucket_name):
    """Set a bucket's CORS policies configuration."""

    # set origin urls
    origin_list = []
    if CLOUDRUN_SERVICE_URL:
        origin_list.append(CLOUDRUN_SERVICE_URL)
    if LOCAL_DOMAIN:
        origin_list.append(LOCAL_DOMAIN)

    storage_client = storage.Client(credentials=GS_CREDENTIALS)
    bucket = storage_client.get_bucket(bucket_name)
    bucket.cors = [
        {
            "origin": origin_list,
            "responseHeader": ["Content-Type", "x-goog-resumable"],
            "method": ["GET", "PUT", "POST"],
            "maxAgeSeconds": 3600,
        }
    ]
    bucket.patch()

    print(f"Set CORS policies for bucket {bucket.name} is {bucket.cors}")
    return bucket


def bucket_metadata(bucket_name):
    """Prints out a bucket's metadata."""
    # bucket_name = 'your-bucket-name'

    storage_client = storage.Client(credentials=GS_CREDENTIALS)
    bucket = storage_client.get_bucket(bucket_name)

    print(f"ID: {bucket.id}")
    print(f"Name: {bucket.name}")
    print(f"Storage Class: {bucket.storage_class}")
    print(f"Location: {bucket.location}")
    print(f"Location Type: {bucket.location_type}")
    print(f"Cors: {bucket.cors}")
    print(f"Default Event Based Hold: {bucket.default_event_based_hold}")
    print(f"Default KMS Key Name: {bucket.default_kms_key_name}")
    print(f"Metageneration: {bucket.metageneration}")
    print(
        f"Public Access Prevention: {bucket.iam_configuration.public_access_prevention}"
    )
    print(f"Retention Effective Time: {bucket.retention_policy_effective_time}")
    print(f"Retention Period: {bucket.retention_period}")
    print(f"Retention Policy Locked: {bucket.retention_policy_locked}")
    print(f"Object Retention Mode: {bucket.object_retention_mode}")
    print(f"Requester Pays: {bucket.requester_pays}")
    print(f"Self Link: {bucket.self_link}")
    print(f"Time Created: {bucket.time_created}")
    print(f"Versioning Enabled: {bucket.versioning_enabled}")
    print(f"Labels: {bucket.labels}")


if __name__ == "__main__":
    bucket_name = os.environ.get("GS_BUCKET_NAME")
    # bucket_metadata(bucket_name)
    cors_configuration(bucket_name)
