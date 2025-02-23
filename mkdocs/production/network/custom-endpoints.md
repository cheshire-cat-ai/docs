# Custom Endpoints

The Cheshire Cat is entirely based on FastAPI and leverages FastAPI routers to instantiate its base endpoints.
Need additional endpoints to cover your specific use case? The Cat provides a specific decorator for that.

## How to Create a Custom Endpoint

Inside your plugin script you can use the `@endpoint` decorator to wrap any sync or async function
that will be used as a FastAPI path operation. Here's simple example:

```python
from cat.mad_hatter.decorators import endpoint

@endpoint.get(path="/hello")
def hello_world():
    return {"Hello":"world"}
```

The default prefix of all custom endpoints is `/custom` so you have to consume it like this:

```curl
curl http://localhost:1865/custom/hello
```

!!! note FastAPI under the hood
    Since there's FastAPI under the hood, you can use every FastAPI operation parameters like `path`, `tags`, `response_model`, etc.

Here's a more complex example:

```python

from cat.mad_hatter.decorators import endpoint
from pydantic import BaseModel
from typing import List, Optional

class CustomDocument(BaseModel):
    document_id: str
    title: str
    content: str
    tags: Optional[List[str]] = []
    created_by: Optional[str] = None

@endpoint.post(path="/ingest", prefix="/custom-ingestion", tags=["Custom Ingestion"], response_model=CustomDocument)
def custom_ingestion(document: CustomDocument, stray=Depends(HTTPAuth(AuthResource.MEMORY, AuthPermission.WRITE))):
    
    # some custom ingestion pipeline
    
    return document

```

Once you activate your plugin the Cheshire Cat will add the custom endpoints to the FastAPI routes and will clear the
`/docs` cache to reflect the new endpoints and their OpenAPI documentation.

## Available Decorators

You have three different decorators available to declare custom endpoints:

 - `@endpoint.get`: To declare a GET operation;
 - `@endpoint.post`: To declare a POST operation;
 - `@endpoint.endpoint`: To declare any other HTTP verb operation;

If you use `@endpoint.endpoint` you need to specify the allowed methods like this:

```python
from cat.mad_hatter.decorators import endpoint

@endpoint.endpoint(path="/delete", methods=["DELETE"], tags=["Delete Custom"])
def custom_delete():
    return {"result":"custom delete endpoint"}
```