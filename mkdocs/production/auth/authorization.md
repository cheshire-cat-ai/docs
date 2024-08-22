# Authorization

The Cat comes with its own roles and permissions to authorize requests and resource access. Each resource comes with granular roles for writing, editing, listing, reading and deleting (e.g. `CONVERSATION_WRITE`). 
You can view the available permissions at `/auth/available-permissions`.

If you have [secured your HTTP/WS Cat endpoints](./authentication.md), every incoming request using JWT authorization header will check for proper permissions for that user, otherwise, if you are using api keys you'll get full permission and will access every available resource.

If you want to manage users permissions you easily do that via restful APIs or via Admin panel, head over to [user-management](./user-management.md) for more info.