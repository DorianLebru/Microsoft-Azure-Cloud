# This function is not intended to be invoked directly. Instead it will be
# triggered by an orchestrator function.
# Before running this sample, please:
# - create a Durable orchestration function
# - create a Durable HTTP starter function
# - add azure-functions-durable to requirements.txt
# - run pip install -r requirements.txt

import logging


def main(mapOutputs):
    results=[]
    list_of_values=[]
    for elem in mapOutputs:
        key = elem[0]
        value = elem[1]
        list_of_values.append(value)
        results.append([key, list_of_values.copy()])
    return results
