# This function is not intended to be invoked directly. Instead it will be
# triggered by an orchestrator function.
# Before running this sample, please:
# - create a Durable orchestration function
# - create a Durable HTTP starter function
# - add azure-functions-durable to requirements.txt
# - run pip install -r requirements.txt

import logging
from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient


def main(fileName):
    account_url = "https://lab2ex5.blob.core.windows.net"
    default_credential = DefaultAzureCredential()

    # Create the BlobServiceClient object
    blob_service_client = BlobServiceClient.from_connection_string("DefaultEndpointsProtocol=https;AccountName=lab2ex5;AccountKey=DefaultEndpointsProtocol=https;AccountName=lab2ex5;AccountKey=o8e1gD+kMe1lagvSogM++KhFmHTTn+8ofKaUWVBXmrFNDdsga/qaBuYExLN+JBlK/zoti2p+Iupf+AStxDUNzA==;EndpointSuffix=core.windows.net")

    container_client = blob_service_client.get_container_client(container='documents')
    blob_list = container_client.list_blobs()

    results=[]
    for blob in blob_list:
        temp_results=[]
        text = container_client.download_blob(blob.name).readall()
        lines=text.splitlines()

        temp_results=[]
        for i in range(len(lines)):
            temp_results.append((i+1,str(lines[i].strip())))
        results.extend(temp_results)
    return results
