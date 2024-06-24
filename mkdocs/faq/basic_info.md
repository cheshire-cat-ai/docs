# Basic Info

#### Can I insert a long article into the chat?

Please avoid pasting long articles into the chat.  
Use Rabbit Hole to upload long texts instead: just click on the attachment icon in the chat input widget and upload your file.

#### Are the configured LLM APIs used to "instruct" the Cat with the documents I'm going to upload?

That's not exactly how it works: basically when you ask something to the Cat, we pass to the configured LLM a prompt with your actual question + data that can be useful to answer that question. Data can be parts of your documents or chat history.  
Please check our documentation for more details about how the Cat works for you.

#### Can I talk to the Cat in a language different from English?

Of course, you can: just change the prompts in the Plugin folder accordingly, and take care not to mix languages to get best results.

#### How can I know where the Cat gets the answers? I'd like to know if it's using the files I uploaded or if it's querying the configured LLM.

Just open the console in your browser to check the logs there. At some point soon, this information will end up in the user interface, but at the moment is behind the scenes.

#### I sent to the Cat some text and documents I want to get rid of, How can I do?

You can delete the `long_term_memory` folder and restart the Cat!