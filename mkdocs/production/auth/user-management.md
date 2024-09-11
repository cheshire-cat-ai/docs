# User Management

If you are developing an application that supports multiple users, it's crucial to ensure that each user's session and memories are isolated. By separating user sessions, you can prevent the mixing of user data, which is particularly important for maintaining data privacy and providing a personalized experience for each user.
[Why is this important?](#why-is-this-important)

## Shadow Users

By default, the Cat requires a unique user identifier to associate sessions and memory data with individual users. 
The easiest way to provide this identifier is passing the `user_id` to HTTP endpoints or to the WebSocket messaging interface.

You can pass the user ID in the WebSocket endpoint like this:
`ws://localhost:1865/ws/{user_id}`

For HTTP endpoints, just include the `user_id` in the request header.

!!! note 
    If no user id is provided, the Cat will assume `user_id = "user"`.

## Internal Users

The Cat framework includes a simple, internal user management system for creating, retrieving, updating, and deleting users. This system provides a convenient, built-in way to manage JWT authentication. By default, authentication is disabled in The Cat. [Need help enabling it?](./authentication.md).

!!! note 
    When authenticating requests with a JWT token, you do not need to pass the `user_id`; The Cat will automatically extract it from the token.

### Managing Internal Users

#### Admin Panel

If you're looking for a straightforward way to manage users, you can use the Admin panel. Simply click on the `Settings` tab and you'll see a `User Management` section.

#### Restful API

The internal user management system is also accessible via a comprehensive RESTful API. There are endpoints for creation, retrieval, updating, and deletion of users. For more information, check the [endpoints](../../production/endpoints.md) page.

## Want to bring in your own users?

If you already have a user management system or identity provider, you can easily integrate it with the Cat by implementing a custom `AuthHandler`.

This allows you to use your own authentication logic and pass the necessary `AuthUserInfo` to the Cat. For more details, refer to the [custom auth guide](./custom-auth.md).

## Why is this important?

As stated above, when working with multiple users, it’s important to separate their sessions and memories. Without that, you'll face WebSocket connection issues and poor user experience can arise. The Cat internally use the provided `user_id` to build a WebSocket connection and tie it to a [StrayCat](../../framework/cat-components/cheshire_cat/stray_cat.md) instance which will handle the user session and memory retrieval.

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

### Users and conversations

The WebSocket client and the HTTP message endpoint identifies the current `user_id` using respectively the `ws://localhost:1865/ws/{user_id}` path variable or the `user_id` in the request header.
The Cat uses this `user_id` to access the user's working memory and store conversations, using the `user_id` as metadata for retrieval. 

This ensures that conversations remain isolated, preventing any mix-up between different users and providing a seamless, personalized experience.

