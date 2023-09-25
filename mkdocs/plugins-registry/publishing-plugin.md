# &#128228; Publishing a Plugin in the Registry

Publishing your plugin and making it available to the whole world is a relatively simple yet crucial step. Take a few minutes to read this section of the guide. Once done, you won't be able to stop!

## &#128095; Start on the Right Foot

A plugin that will be published in our public registry requires some precautions and must have a `plugin.json` file within the root folder with all the fields as complete as possible. This ensures that your plugin is attractive and searchable through the dedicated "Plugins" tab of the Cheshire Cat.

To make it easier for you, we have provided a GitHub repository template so that you only need to clone it and find yourself with a folder ready to develop your first public plugin without worries.

You can find the repository at this address: [https://github.com/cheshire-cat-ai/plugin-template](https://github.com/cheshire-cat-ai/plugin-template)

Click on the colorful "Use this template" button at the top and choose to create a new repository. Once you've chosen the name for your repository and cloned the code to your machine, you can run the setup script to clean up the files and rename everything as needed.

```bash
$ python setup.py
```

To learn more about how to work with the plugin template, read [this dedicated page](plugin-from-template.md).

### &#128230; Release Creation

We recommend using GitHub's release system to effectively manage your plugin releases. Our registry can always download the latest stable release of your plugin tagged on GitHub. You can do this manually or through automation.

A repository created with our template automatically includes the creation of a release on GitHub through a GitHub action. This automation happens whenever the `version` number in the `plugin.json` file changes. The release is automatically tagged with the version number and released in all the formats supported by GitHub.

Here's the documentation related to managing releases on GitHub: [https://docs.github.com/en/repositories/releasing-projects-on-github/managing-releases-in-a-repository](https://docs.github.com/en/repositories/releasing-projects-on-github/managing-releases-in-a-repository)

!!! info
	Remember to change the `version` number in `plugin.json` only when you actually want to create a new version of your plugin. While you're in development, you can either open a develop branch (the automation only runs on the main branch) or continue to push to the main branch without changing the version number.

## &#128220; Take Care of the `plugin.json`

As you may have realized, the `plugin.json` file is what governs all aspects of publishing your plugin and contains the fields that will help your plugin stand out within the registry. Therefore, take care to fill it out as comprehensively as possible and try to complete all the available fields.

In reality, there are only 3 mandatory fields for publishing in the registry: `name`, `author_name` and `version`. However, we strongly recommend adding a couple of `tags` and a `description` as well. It's through these fields that our search system will be able to discover your plugin.

### &#128195; Explanation of the fields

Below is a list of the fields with a brief explanation.

!!! warning
	Fields marked with the asterisk (<span style="color:red">*</span>) are mandatory.

- `name`<span style="color:red">**\***</span>: The name of your plugin.
- `version`<span style="color:red">**\***</span>: The last stable version number.
- `author_name`<span style="color:red">**\***</span>: The author's name or nickname.
- `description`: A brief description of the plugin.
- `author_url`: Link to the author's website.
- `plugin_url`: Link to the plugin's website with the full description/documentation (can be a different link from the GitHub repository).
- `tags`: A comma-separated list of tags (e.g., "multimedia, documents, pdf, csv").
- `thumb`: The direct link to your plugin's logo image. Recommended minimum size is 160x160px. Recommended formats are png or jpg.

## &#128064; Submit Your Plugin for Review

The submission and review process is done through our GitHub repository [awesome-plugins](https://github.com/cheshire-cat-ai/awesome-plugins) and it's quite straightforward. All you need to do is fork the repository and then, after adding your plugin to the JSON file, submit a Pull Request to us.

The fields to add to the new object you'll be adding are as follows:

- `name`: The name of your plugin for identification in the list (for public display, the name contained in your `plugin.json` will be used).
- `url`: The link to your public GitHub repository.

The review process may take a few days, so don't worry if some time passes before you see your plugin approved. This depends on the number of plugins in the queue and the availability of volunteers. We will strive to provide feedback as quickly as possible.

The review is in place to prevent the publication of plugins containing malware, obvious security flaws, or of low quality and relevance. We will be diligent, but we ask for your understanding and request that you always submit tested plugins that do not jeopardize the security of our users.


## &#128276; Stay Updated

The final step is to stay informed about what's happening in the magical world of Cheshire Cat so that you can keep your plugin up to date with the latest developments. To facilitate this, we've created a dedicated channel for plugin developers on our [official Discord server](https://discord.com/invite/bHX5sNFCYU).

We invite you to become a part of our community and let a moderator know that you've submitted a plugin. Once your plugin is approved, we'll be happy to assign you a special role (Plugin Developer) and unlock all the dedicated channels for you.

If you don't use Discord or prefer not to login on our server, we still encourage you to try to keep up with Cheshire Cat AI's updates. We'll conduct periodic review cycles, and if your plugin becomes too outdated or non-functional after some time, we may have to remove it from the registry.

*Looking forward to seeing you among our amazing plugin developers!*