# Custom Auth Handler

Want to bring in your own authentication system with your own users? The Cat provides a useful API to
customize the default authentication flow and add a custom auth handler which delegates authentication and authorization
to third party systems.

## Preliminary steps

Since the Cat has its own auth handler mechanism, which is always inserted in the auth handler pipe, you need to lock
your instance following the instructions in the [authentication](authentication.md) section.

## Building a Custom AuthHandler

Let's walk through the process of creating a custom `AuthHandler`. While the exact implementation will vary depending on
provider or system you choose to rely on, the overall structure will remain the same.

### Create the Custom Handler 

Start by extending the `BaseAuthHandler` class to define the behaviour for handling
tokens and validating users. Here's an example:

```python
from cat.factory.custom_auth_handler import BaseAuthHandler
from cat.auth.permissions import (
    AuthPermission, AuthResource, AuthUserInfo, get_base_permissions
)
import httpx

class CustomAuthHandler(BaseAuthHandler):
    
    def __init__(self, **config):
        self.server_url = config.get("server_url")

    
    async def authorize_user_from_jwt(self, token: str, auth_resource: str, auth_permission: str):
        jwt_validation_url = f"{self.server_url}/validate-token"
        
        async with httpx.AsyncClient() as client:
            response = await client.get(jwt_validation_url, headers={
                "Authorization": f"Bearer {token}"
            })

        if response.status_code == 200:
            user_data = response.json()

            # Return the user information mapped to AuthUserInfo
            return AuthUserInfo(
                id=user_data.get("username"),
                name=user_data.get("name", ""),
                extra=user_data.get("extra") # Optional data to be passed to the Cat
            )
        else:
            return None  # If the server responds with an error or doesn't respond at all
        
        
    async def authorize_user_from_key(self, protocol: str, user_id: str, api_key: str, auth_resource, auth_permission):
        # Optional: Handle API key authentication, if applicable
        return None

```

### Create the Custom Handler Config 

Create a new `AuthHandlerConfig` class that inherits from `BaseAuthHandlerConfig`.
This will be the configuration class that contains all the necessary settings to initialize your custom handler.

```python
from cat.factory.auth_handler import AuthHandlerConfig
from typing import Type
from pydantic import ConfigDict, Field

class CustomAuthHandlerConfig(AuthHandlerConfig):
    _pyclass: Type = CustomAuthHandler

    server_url: str = Field(..., description="The URL of the identity provider")

    model_config = ConfigDict(
        json_schema_extra={
            "humanReadableName": "Custom Auth Handler",
            "description": "Delegate auth to a custom identity provider."
        }
    )

```

### Register the Custom Handler

Register the new handler with the `factory_auth_handlers` hook.

```python
from cat.mad_hatter.decorators import hook
from typing import List

@hook(priority=0)
def factory_allowed_auth_handlers(allowed: List[AuthHandlerConfig], cat) -> List:
    allowed.append(CustomAuthHandlerConfig)
    return allowed

```

### Activate the Custom Handler

Activate the new handler using the proper endpoint in your Cat installation.

```bash
curl --location --request PUT 'http://{your_cat_instance}/auth_handler/settings/CustomAuthHandlerConfig' \
--header 'Content-Type: application/json' \
--data '{
   "server_url": {your_idp_url},
}'
```

That's it! Now every incoming request will be authenticated using the custom auth handler.

## Key Components and Concepts

### BaseAuthHandler

`BaseAuthHandler` is the class that you will extend to implement your custom auth flow. This is an abstract class that
forces you to implement two basic methods: `authorize_user_from_jwt` and `authorize_user_from_key`. You'll write your
own auth logic in there inserting, for example, credentials validation request to external identity providers.

- `authorize_user_from_jwt`: Validates and processes incoming JWT tokens, extracting user information and 
- mapping it into Cheshire Cat’s `AuthUserInfo` structure. 
- `authorize_user_from_key`: Allows validation of requests based on an API key, usually used for machine to machine communication.

### AuthHandlerConfig

The `AuthHandlerConfig` class provides a base configuration that you can extend to define custom settings for your 
authentication handler. It includes all the necessary settings to initialize your custom handler.
These may include: information about the external identity provider, authentication endpoint, client secrets, etc.

### Allowed Auth Handlers Hook

The `factory_allowed_auth_handlers` hook allows you to add your own auth handlers to the list of allowed auth handlers.

### AuthUserInfo

The `AuthUserInfo` class represents the decoded content of an authentication token. This class is used to standardize the 
output of AuthHandlers, ensuring that token details are consistent across different authentication systems. 
The AuthUserInfo object is crucial for session management within Cat's core, as it either retrieves or creates a user 
session, known as a StrayCat. 