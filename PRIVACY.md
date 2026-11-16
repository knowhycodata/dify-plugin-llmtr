# Privacy Policy

This plugin does not collect, store, or log any user data itself.

When you use an LLMTR model in Dify, the plugin sends your prompt messages, model parameters, and the API key you configured to the LLMTR API at `https://llmtr.com/v1` to generate a response. It does not contact any other endpoint. Your API key is stored by your Dify instance as an encrypted credential, not by this plugin.

On the LLMTR side, prompt and response bodies are not written to the usage and billing database; usage records hold the model, token counts, and cost. Turkey-hosted models (`llmtr/...`) run on LLMTR infrastructure in Turkey; other models are processed under the rules of the selected upstream provider. See https://llmtr.com for LLMTR's own terms and privacy policy.
