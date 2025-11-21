# cribl_cloud_management_sdk_python Examples

This directory contains example scripts that demonstrate how to use the cribl_cloud_management_sdk_python SDK.

## Prerequisites

- Python 3.9 or higher
- pip

## Setup

1. **Set up virtual environment:**
   ```bash
   python3 -m venv examples-env
   source examples-env/bin/activate
   pip install cribl-mgmt-plane
   ```

2. **Configure credentials:**
   ```bash
   CLIENT_ID = "your-client-id"
   CLIENT_SECRET = "your-client-secret"
   ORG_ID = "your-org-id"
   ```

3. **Run an example:**
   ```bash
   python example_cloud_auth.py
   ```
   
## Configuration

Each example can be configured by either:
1. Using a `.env` file
2. Editing the configuration variables directly in the example files

### Environment Variables

- `ORG_ID` - Your Organization ID
- `CLIENT_ID` - Your OAuth2 Client ID
- `CLIENT_SECRET` - Your OAuth2 Client Secret
