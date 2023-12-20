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

## Getting data and using rest api endpoint

    ```bash
    import requests
    import pandas as pd
    
    def fetch_data_from_azure_function(page, pagesize):
        # Replace with your Azure Function endpoint URL
        function_url = "https://publicbookdataset.azurewebsites.net/api/getbooks"
        
        # Set the parameters
        params = {
            'page': page,
            'pagesize': pagesize
        }
        
        # Make the HTTP request to the Azure Function endpoint
        response = requests.get(function_url, params=params)
        
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON response
            return response.json()
        else:
            # Print an error message if the request was not successful
            print(f"Error: {response.status_code}")
            return None
    
    def main():
        # Assign initial page and pagesize parameters
        page = 1
        pagesize = 100
        
        # Initialize an empty list to store JSON data
        json_data = []
        
        while True:
            # Fetch data from Azure Function endpoint
            data = fetch_data_from_azure_function(page, pagesize)
            
            # Break the loop if no more data is returned
            if not data:
                break
            
            # Append the data to the list
            json_data.extend(data)
            
            # Increment the page for the next iteration
            page += 1
        
        # Convert the list of JSON data to a Pandas DataFrame
        df = pd.DataFrame(json_data)
        
        # Display the resulting DataFrame
        print("Data Frame:")
        print(df.head())
    
    if __name__ == "__main__":
        main()

    ```

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