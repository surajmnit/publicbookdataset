# Azure Function with Blob Storage and Key Vault Integration

This project demonstrates the integration of Azure Functions with Azure Blob Storage and Azure Key Vault. The Azure Function exposes an HTTP-triggered endpoint (`getbooks`) to retrieve paginated data from a CSV file stored in Azure Blob Storage. The storage account key is securely stored in Azure Key Vault.

## Table of Contents

- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)

## Features

- HTTP-triggered Azure Function for retrieving paginated data.
- Securely retrieves storage account key from Azure Key Vault using Azure Managed Identity.
- Integration with Azure Blob Storage to download a CSV file.

## Getting Started

### Prerequisites

Before running the Azure Function, make sure you have the following:

- Azure subscription
- Azure Storage Account with a container named "books" and a CSV file named "books.csv"
- Azure Key Vault with a secret named "StorageAccountKey" containing the storage account key
- Azure Function App with an assigned managed identity

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/surajmnit/publicbookdataset.git
   cd publicbookdataset

2. Install dependencies:

   ```bash
   pip install -r requirements.txt

### Usage

Deploy the Azure Function to your Azure Function App.
Trigger the function by accessing the endpoint:

   ```bash
    Copy code
    curl https://yourfunctionapp.azurewebsites.net/api/getbooks?page=1&pagesize=10&name=books.csv
    Adjust the parameters as needed.
    Configuration

Ensure that the following environment variables or configuration settings are set:

AZURE_CLIENT_ID
AZURE_CLIENT_SECRET
AZURE_TENANT_ID
AZURE_STORAGE_ACCOUNT_URL
KEY_VAULT_URL


### Contributing

We welcome contributions! If you find a bug or have an enhancement request, please follow the Contributing Guidelines.

Fork the repository.
Create a new branch: git checkout -b feature/new-feature.
Make your changes and commit: git commit -m 'Add new feature'.
Push to the branch: git push origin feature/new-feature.
Submit a pull request.
