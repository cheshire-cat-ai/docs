# User Management


We divide users in 3 categories:

| User type    | Use case             | Where are they stored  | Authentication method     |
|--------------|----------------------|------------------------|---------------------------|
| **Public**   | Website support chat | Nowhere                | API keys (`CCAT_API_KEY`, `CCAT_API_KEY_WS`) and `user_id` |
| **Internal** | Company assistant    | Cat core               | JSON Web Token (JWT)      |
| **Custom**   | Your imagination     | Your identity provider | Your custom `AuthHandler` |

If you are developing an application that supports multiple users, it's crucial to ensure that each user's session and memories are isolated, with granular access.

Each user interacts with the Cat via a dedicated [`StrayCat`](../../framework/cat-components/cheshire_cat/stray_cat.md) instance, which in turn you will be able to use in your plugins as `cat`.

Let's now see the 3 types of users in detail.

## Public Users

Users are public when they are not stored in core or in an external identity provider (like [KeyCloak](https://github.com/lucagobbi/catcloak)), but they are still allowed to use endpoints. A typical use case is a customer support AI on a public website, where you don't want to register and store users.

Public users will be created, kept during the conversation, then permanently deleted.  
To allow them access to the Cat you need to provide in each request a `user_id` and a credential (if required).

### ID

By default, the Cat requires a unique user identifier to associate sessions and memory data with individual users. 
Generate this temporary identifier as you see fit and pass it as `user_id` to HTTP endpoints or to the WebSocket messaging interface.

You can pass a user ID to WebSocket endpoint by changing the address:  
`ws://localhost:1865/ws/caterpillar_123456`

For HTTP endpoints, just include a `user_id` header in the request:  
`user_id`: `caterpillar_123456`

!!! note 
    If no user id is provided, the Cat will assume `user_id = "user"`.

### Credentials

If you set up `CCAT_API_KEY` and `CCAT_API_KEY_WS`, public users still need to provide those credentials, respectively via [http](./authentication.md#http-key) and [websocket](./authentication.md#websocket-key).

If you did not set them, at your own peril all endpoints are wide open and you just need to specify the `user_id`.  

Most people building public chatbots leave websocket open and lock down all http endpoints.  
In any case it is recommended that you do this kind of requests server side, from a smartphone app, or between containers in a private docker network.  
Avoid using your keys in a browser or any other transparent client.



## Internal Users

In use cases in which a specific and restricted set of users will use your Cat, you want dedicated credentials, detailed management and permanent storage.

### Management

The Cat framework includes a simple, internal user management system for creating, retrieving, updating, and deleting users. Endpoints for user management can be found on your installation under `/docs`.

If you're looking for a straightforward way to manage users, you can use the Admin panel. Simply click on the `Settings` tab and you'll see a `User Management` section.

### Credentials

Once registered into the Cat with username and password, a user can be assigned granular permissions and can access endpoints with a JWT (JSON Web Token).

Detailed instructions on how to obtain and use the JWT are [here](./authentication.md#obtaining-a-jwt).  
Remember to customize your JWT secret via the [`CCAT_JWT_SECRET`](./authentication.md#2-securing-jwt) environment variable.

!!! note 
    When authenticating requests with a JWT token, you do not need to pass the `user_id`; The Cat will automatically extract it from the token.


## Custom Users

If you already have a user management system or identity provider, you can easily integrate it with the Cat by implementing a custom `AuthHandler`.

This allows you to use your own authentication logic and pass the necessary `AuthUserInfo` to the Cat. For more details, refer to the [custom auth guide](./custom-auth.md).

### Credentials

While you can customize the `AuthHandler` to assign identity and permissions via any identity provider, we enforce a standard on how credentials must be sent to the Cat:

 - for http, via `Authentication: Bearer <credential>` header
 - for websocket, via `?token=<credential>` query parameter 
 - the two above are valid for both api keys and JWT

This allows for auth and user management customization without breaking the many [client libraries and tools](../network/clients.md) the community is building.


## Examples

### Access current user from a plugin

In hooks, tools, forms and custom endpoints you can easily obtain user information from the `cat` variable, instance of [`StrayCat`](../../framework/cat-components/cheshire_cat/stray_cat.md).

```python
from cat.mad_hatter.decorators import tool

@tool(return_direct=True)
def who_am_i(arg, cat):
    """Use to retrieve info about the current user."""
    return f"Hello {cat.user_id}, here is some info about you: {cat.user_data.model_dump_json()}"
```

### Users and memories

In the Cat, users and memories are closely related. Without user-specific memory isolation, The Cat cannot maintain context across conversations.
By default, the user system affects only the [working memory](../../framework/cat-components/memory/working_memory.md) and
the [episodic memory](../../framework/cat-components/memory/long_term_memory.md). The other memories are shared among users, but you could easily think about a custom plugin to store and restrict access to data in [Long Term Memory](../../framework/cat-components/memory/long_term_memory.md) based on `user_id`.

Here's an example of how the `user_id` could be used to filter declarative memories both on the uploading and retrieval side:

```python

from cat.mad_hatter.decorators import hook

@hook
def before_rabbithole_insert_memory(doc, cat):
    # insert the user id metadata
    doc.metadata["author"] = cat.user_id
    return doc

@hook
def before_cat_recalls_declarative_memories(declarative_recall_config, cat):
    # filter memories using the user_id as metadata. 
    declarative_recall_config["metadata"] = {"author": cat.user_id}
    return declarative_recall_config

```


