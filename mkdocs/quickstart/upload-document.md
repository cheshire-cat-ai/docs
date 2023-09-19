# Upload a Document

Documents can be uploaded via the Admin Portal (and it's also possible through APIs). Uploaded documents will be considered by the Cat to prepare the answer to your question.
These documents are saved in a local database called `declarative memory`.

The Cat's knowledge about socks is quite basic; we will upload more specific knowledge.

Go to the Admin Portal at `localhost:1865/admin` on the `Home` tab, click on `Upload url` and use this url `https://en.wikipedia.org/wiki/N%C3%A5lebinding`:

![Alt text](../assets/img/quickstart/upload-document/upload-url.png)

After you receive notification of the finished read, the Cat can answer with more detailed answers:

![Alt text](../assets/img/quickstart/upload-document/cat-answers.png)

## Next Step
In the next step you will learn how to prepare an empty Plugin