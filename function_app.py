import azure.functions as func
import logging
import json

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)


@app.route(route="hello")
def hello_function(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Python HTTP trigger function processed a request.")

    name = req.params.get("name")
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get("name")

    if name:
        response_data = {
            "message": f"Hello, {name}! Welcome to Azure Functions.",
            "status": "success",
        }
        return func.HttpResponse(
            json.dumps(response_data), mimetype="application/json", status_code=200
        )
    else:
        response_data = {
            "message": "Please pass a name in the query string or request body",
            "status": "error",
        }
        return func.HttpResponse(
            json.dumps(response_data), mimetype="application/json", status_code=400
        )
