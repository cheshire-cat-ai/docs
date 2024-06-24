# &#128101; User System

The Cat provides a basic user management system that allows having separated memories for each user.
The user system affects only the [working memory](../../framework/cat-components/memory/working_memory.md) and
the [episodic memory](../../framework/cat-components/memory/long_term_memory.md).
The other memories are shared among users.

More in details, the websocket client indicates the current `user_id` by calling the `ws://localhost:1865/ws/{user_id}` endpoint.
The Cat uses such `user_id` to retrieve the user's working memory and to store the user's conversation (using the `user_id` as a metadatum).

!!! Note
    Please, note that the user management system works only when using a custom client.
    Its usage is not intended from the [admin](../../technical/basics/admin/admin-interface.md) interface,
    which, by default, uses `user_id = "user"`.

## Example

The Cheshire Cat provides two API clients, written in [Python](https://pypi.org/project/cheshire-cat-api/)
and [Typescript](https://www.npmjs.com/package/ccat-api), that allow exploiting the user management system.

!!! example
    **Setting the `user_id` from a custom client:**
    === "Python"
        ```python
        import cheshire_cat_api as ccat

        cat_client = ccat.CatClient()
        
        # Send a message specifying the user_id
        message = "Hello my friend!!"
        cat_client.send(message, user_id="user05")
        ```
    === "Typescript"
        ```typescript
        import { CatClient } from 'ccat-api'

        const cat = new CatClient({
            baseUrl: 'localhost'
        })
        
        cat.send('Hello my friend!!', 'user05');
        ```   

TODO: Add hook example to retrive document only few users.
