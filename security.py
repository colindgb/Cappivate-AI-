import hashlib

def hash_license_key(license_key):
    return hashlib.sha256(license_key.encode()).hexdigest()

def validate_license(license_key, stored_hash):
    return hash_license_key(license_key) == stored_hash
