// @ts-check
import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';
import mermaid from 'astro-mermaid';

export default defineConfig({
  site: 'https://cheshire-cat-ai.github.io',
  base: '/docs/',
  integrations: [
    // astro-mermaid must come before Starlight so its markdown plugins run.
    mermaid({ theme: 'default', autoTheme: true }),
    starlight({
      title: 'Cheshire Cat AI docs',
      logo: {
        src: './src/assets/cheshire-cat-logo.svg',
        alt: 'Cheshire Cat AI',
      },
      favicon: '/favicon.ico',
      customCss: ['./src/styles/custom.css'],
      components: {
        // Inject the version switcher above the default sidebar.
        Sidebar: './src/components/Sidebar.astro',
      },
      social: [
        { icon: 'github', label: 'GitHub', href: 'https://github.com/cheshire-cat-ai/core' },
        { icon: 'discord', label: 'Discord', href: 'https://discord.gg/bHX5sNFCYU' },
      ],
      editLink: {
        baseUrl: 'https://github.com/cheshire-cat-ai/docs/edit/main/',
      },
      sidebar: [
        {
          label: 'Quickstart',
          items: [
            { label: 'Install', slug: 'quickstart/installation-configuration' },
            { label: 'Message the Cat', slug: 'quickstart/message' },
            { label: 'Create a Plugin', slug: 'quickstart/prepare-plugin' },
            { label: 'Write the first Tool', slug: 'quickstart/writing-tool' },
            { label: 'Write the first Hook', slug: 'quickstart/writing-hook' },
            { label: 'Conclusion', slug: 'quickstart/conclusion' },
          ],
        },
        {
          label: 'Plugins',
          items: [
            { label: 'Install a Plugin', slug: 'quickstart/installing-plugin' },
            { label: 'How to Write a Plugin', slug: 'plugins/plugins' },
            { label: 'Write an Agent', slug: 'plugins/agents' },
            { label: 'Tools', slug: 'plugins/tools' },
            { label: 'Hooks', slug: 'plugins/hooks' },
            { label: 'Custom Endpoints', slug: 'plugins/endpoints' },
            { label: 'Logging', slug: 'plugins/logging' },
            { label: 'Settings', slug: 'plugins/settings' },
            { label: 'Dependencies', slug: 'plugins/dependencies' },
            { label: 'Examples', slug: 'plugins/examples' },
            {
              label: 'Hooks API Reference',
              items: [
                {
                  label: 'Flow',
                  items: [
                    { slug: 'plugins/hooks-reference/flow/before_cat_reads_message' },
                    { slug: 'plugins/hooks-reference/flow/cat_recall_query' },
                    { slug: 'plugins/hooks-reference/flow/before_cat_recalls_memories' },
                    { slug: 'plugins/hooks-reference/flow/before_cat_recalls_episodic_memories' },
                    { slug: 'plugins/hooks-reference/flow/before_cat_recalls_declarative_memories' },
                    { slug: 'plugins/hooks-reference/flow/before_cat_recalls_procedural_memories' },
                    { slug: 'plugins/hooks-reference/flow/after_cat_recalls_memories' },
                    { slug: 'plugins/hooks-reference/flow/before_cat_stores_episodic_memory' },
                    { slug: 'plugins/hooks-reference/flow/before_cat_sends_message' },
                  ],
                },
                {
                  label: 'Agent',
                  items: [
                    { slug: 'plugins/hooks-reference/agent/before_agent_starts' },
                    { slug: 'plugins/hooks-reference/agent/agent_fast_reply' },
                    { slug: 'plugins/hooks-reference/agent/agent_allowed_tools' },
                    { slug: 'plugins/hooks-reference/agent/agent_prompt_prefix' },
                    { slug: 'plugins/hooks-reference/agent/agent_prompt_suffix' },
                  ],
                },
                {
                  label: 'Rabbit Hole',
                  items: [
                    { slug: 'plugins/hooks-reference/rabbit-hole/rabbithole_instantiates_parsers' },
                    { slug: 'plugins/hooks-reference/rabbit-hole/rabbithole_instantiates_splitter' },
                    { slug: 'plugins/hooks-reference/rabbit-hole/before_rabbithole_insert_memory' },
                    { slug: 'plugins/hooks-reference/rabbit-hole/before_rabbithole_splits_text' },
                    { slug: 'plugins/hooks-reference/rabbit-hole/after_rabbithole_splitted_text' },
                    { slug: 'plugins/hooks-reference/rabbit-hole/before_rabbithole_stores_documents' },
                    { slug: 'plugins/hooks-reference/rabbit-hole/after_rabbithole_stored_documents' },
                  ],
                },
                {
                  label: 'Factory',
                  items: [
                    { slug: 'plugins/hooks-reference/factory/factory_allowed_llms' },
                    { slug: 'plugins/hooks-reference/factory/factory_allowed_embedders' },
                    { slug: 'plugins/hooks-reference/factory/factory_allowed_auth_handlers' },
                  ],
                },
                {
                  label: 'Lifecycle',
                  items: [
                    { slug: 'plugins/hooks-reference/lifecycle/before_cat_bootstrap' },
                    { slug: 'plugins/hooks-reference/lifecycle/after_cat_bootstrap' },
                  ],
                },
              ],
            },
            {
              label: 'Registry',
              items: [
                { label: 'Using the Plugin Template', slug: 'plugins/plugins-registry/plugin-from-template' },
                { label: 'Publishing a Plugin', slug: 'plugins/plugins-registry/publishing-plugin' },
              ],
            },
          ],
        },
        {
          label: 'Deploy',
          items: [
            { label: 'Make the Cat Private', slug: 'production/administrators/make_the_cat_private' },
            { label: 'Environment Variables', slug: 'production/administrators/env-variables' },
            { label: 'Automatic Tests', slug: 'production/administrators/tests' },
            { label: 'Backups and Updates', slug: 'production/administrators/backups-updates' },
            {
              label: 'Network',
              items: [
                { label: 'HTTP Endpoints', slug: 'production/network/http-endpoints' },
              ],
            },
            {
              label: 'Auth',
              items: [
                { label: 'Authentication', slug: 'production/auth/authentication' },
                { label: 'Authorization', slug: 'production/auth/authorization' },
                { label: 'User Management', slug: 'production/auth/user-management' },
                { label: 'Custom Auth', slug: 'production/auth/custom-auth' },
              ],
            },
          ],
        },
        {
          label: 'FAQ',
          items: [
            { label: 'General', slug: 'faq/general' },
            { label: 'Basic Info', slug: 'faq/basic_info' },
            { label: 'Errors', slug: 'faq/errors' },
            { label: 'Customization', slug: 'faq/customization' },
            { label: 'Security & Spending', slug: 'faq/security_and_spending' },
            {
              label: 'Concepts',
              items: [
                { label: 'Language Models', slug: 'faq/llm-concepts/llm' },
                { label: 'Retrieval Augmented Generation', slug: 'faq/llm-concepts/rag' },
                { label: 'Prompt', slug: 'faq/llm-concepts/prompt' },
                { label: 'Encoder', slug: 'faq/llm-concepts/embedder' },
                { label: 'Vector Memory', slug: 'faq/llm-concepts/vector-memory' },
              ],
            },
          ],
        },
      ],
    }),
  ],
});
