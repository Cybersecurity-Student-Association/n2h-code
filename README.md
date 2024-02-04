# Getting Started
### 1. Create your Discord Developer Application
1. Navigate to the [Discord Developer Portal](https://discord.com/developers/).
2. Create a new application. Name it whatever you like!
3. Go to the Bot section of your application and reset the Token. **SAVE THIS AS IT CANNOT BE RETRIEVED LATER**. Turn on the "Message Content" Intent. This will allow us to read message content.
4. Generate your invitation URL using the OAuth2 -> URL Generator. Be sure to check the `bot` and `application.commands` scopes. Add permissions as wanted. If you are unsure, use the following permissions integer: `824633723968`.
5. Paste this URL in your browser to add to servers.

### 2. Write your Bot's code
1. Install the discord library in your folder using the commands [here](https://discordpy.readthedocs.io/en/stable/intro.html).
2. Create a `.env` file in your directory. Add the following, replacing [token] with the token you saved: `TOKEN=[token]`.
3. Write your bot code in a .py file in the directory.