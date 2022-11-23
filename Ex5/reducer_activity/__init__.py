# This function is not intended to be invoked directly. Instead it will be
# triggered by an orchestrator function.
# Before running this sample, please:
# - create a Durable orchestration function
# - create a Durable HTTP starter function
# - add azure-functions-durable to requirements.txt
# - run pip install -r requirements.txt

import logging


def main(pair):
    key=pair[0]
    value=pair[1]

    count = 0
    for k in value:
        count+=k
    return [key, count]
