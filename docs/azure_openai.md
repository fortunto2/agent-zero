# Azure OpenAI Configuration

Agent Zero supports Azure-hosted OpenAI models. You can configure your credentials through environment variables in the `.env` file. The loader accepts either `OPENAI_AZURE_*` or `AZURE_OPENAI_*` naming schemes.

```
# Either style works
API_KEY_OPENAI_AZURE=your-key
OPENAI_AZURE_ENDPOINT=https://example-resource.openai.azure.com
OPENAI_API_VERSION=2024-12-01-preview

# Alternative naming
AZURE_OPENAI_API_KEY=your-key
AZURE_OPENAI_ENDPOINT=https://example-resource.openai.azure.com
AZURE_OPENAI_API_VERSION=2024-12-01-preview
```

If both variants are present, the `AZURE_OPENAI_*` values take precedence. Specify the API version when required by Azure.
