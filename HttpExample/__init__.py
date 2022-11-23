import logging

import azure.functions as func

def integration(a, b, N):
    dx = (b-a)/N
    x=a
    sum_left = 0
    sum_right = 0
    for i in range(N):
        sum_left += abs(math.sin(x))*dx
        x+=dx
        sum_right += abs(math.sin(x))*dx
    return sum_left, sum_right

def integration_without_N(a, b):
    T=[]
    for N in ([10, 100, 100, 1000, 10000, 100000, 1000000]):
        T+=[(integration(float(a), float(b), N))]
    return '$T'

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    lower = req.params.get('lower')
    upper = req.params.get('upper')
    if not lower:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            lower = req_body.get('lower')

    if not upper:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            upper = req_body.get('upper')

    if upper and lower:
        return func.HttpResponse(f"Results : {integration_without_N(lower, upper)}.")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )

        
