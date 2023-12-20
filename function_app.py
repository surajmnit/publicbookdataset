from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient
import azure.functions as func
import logging
from azure.storage.blob import BlobServiceClient
import pandas as pd
import os

# Set up logging
logging.basicConfig(level=logging.INFO)

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

def get_secret_from_keyvault(secret_name):
    keyvault_url = os.environ.get("KEYVAULT_URL")
    credential = DefaultAzureCredential()
    client = SecretClient(vault_url=keyvault_url, credential=credential)

    try:
        secret = client.get_secret(secret_name)
        return secret.value
    except Exception as e:
        logging.error(f"Error retrieving secret '{secret_name}' from Key Vault: {str(e)}")
        raise

@app.route(route="getbooks")
def http_trigger(req: func.HttpRequest) -> func.HttpResponse:
    try:
        page = int(req.params.get('page', 1))  # Default to page 1 if not specified
        pagesize = int(req.params.get('pagesize', 100))  # Adjust the page size as needed

        filename = req.params.get('name')
        storageaccounturl = 'https://bookdataset.blob.core.windows.net'
        secret_name = os.environ.get("SECRET_NAME")
        storageaccountkey = get_secret_from_keyvault(secret_name)
        localfilename = '/tmp/' + str(filename)
        container_name = "books"
        filename = 'books.csv'
        blobname = str(filename)
        blob_service_client_instance = BlobServiceClient(account_url=storageaccounturl, credential=storageaccountkey)
        blob_client_instance = blob_service_client_instance.get_blob_client(container_name, blobname, snapshot=None)

        with open(localfilename, "wb") as my_blob:
            blob_data = blob_client_instance.download_blob()
            blob_data.readinto(my_blob)

        df = pd.read_csv(localfilename, on_bad_lines='skip')

        # Paginate the data
        start_index = (page - 1) * pagesize
        end_index = start_index + pagesize
        paginated_data = df.iloc[start_index:end_index]

        # Convert DataFrame to JSON
        json_data = paginated_data.to_json(orient='records')

        logging.info(f"Successfully retrieved and processed data for page {page} with {pagesize} records.")

        return func.HttpResponse(json_data, mimetype="application/json")

    except Exception as e:
        logging.error(f"Error processing request: {str(e)}")
        return func.HttpResponse(f"Error: {str(e)}", status_code=500)