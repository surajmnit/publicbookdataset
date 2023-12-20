# Azure Function for Retrieving and Processing Book Data

## Overview

This repository contains an Azure Function that fetches book data from a CSV file stored in Azure Blob Storage, processes it, and returns it in a paginated JSON format. It's designed to be accessed via an HTTP trigger.

**Key Features:**

- Retrieves data securely from Blob Storage using Azure Key Vault for secret management
- Handles pagination to efficiently retrieve and return large datasets
- Logs events for monitoring and troubleshooting

## Prerequisites

- An Azure subscription with the following resources:
    - Azure Function App
    - Azure Key Vault
    - Azure Blob Storage
- Python 3.6 or higher
- Required Python libraries (listed in `requirements.txt`)

## Deployment

1. Create the required Azure resources.
2. Install the required Python libraries: `pip install -r requirements.txt`
3. Set the following environment variables in your Azure Function App:
    - `KEYVAULT_URL`: The URL of your Azure Key Vault
    - `SECRET_NAME`: The name of the secret in Key Vault containing your Blob Storage account key
4. Deploy the code to your Azure Function App.

## Usage

1. Send an HTTP GET request to the function's endpoint (e.g., `https://your-function-app.azurewebsites.net/api/getbooks`).
2. Optionally, include query parameters to control pagination:
    - `page`: The page number to retrieve (default: 1)
    - `pagesize`: The number of records per page (default: 100)

## Example Response

```json
[
  {"bookID": "1", "title": "Author 1", ...},
  {"bookID": "2", "title": "Author 2", ...},
  ...
]
```

## Additional Information

- **Logging:** The function logs events to the Azure Functions console for monitoring and troubleshooting.
- **Error Handling:** The function includes basic error handling and returns informative error messages in case of issues.

## Contributing

Feel free to contribute to this project by submitting issues or pull requests!