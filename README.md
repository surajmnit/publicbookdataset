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
