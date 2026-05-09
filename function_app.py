import azure.functions as func
import logging

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

@app.route(route="hello", methods=["GET", "POST"])
def hello_world(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("HelloWorld function processed a request.")

    name = req.params.get("name")
    if not name:
        try:
            body = req.get_json()
        except ValueError:
            body = None
        if body:
            name = body.get("name")

    greeting = (
        f"Hello, {name}! Greetings from Sanjay's Python Azure Function — deployed via GitHub CD!"
        if name
        else "Hello from Sanjay's Python Azure Function — deployed via GitHub CD! Pass ?name=YourName to personalize."
    )

    return func.HttpResponse(greeting, status_code=200, mimetype="text/plain")