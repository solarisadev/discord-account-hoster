# Discord Token Monitor

This tool is designed to monitor the status of Discord tokens by checking their validity against Discord's API. It is intended for **security research purposes only** and must be used in compliance with Discord's [Terms of Service](https://discord.com/terms) and [Developer Terms of Service](https://discord.com/developers/docs/legal).

**Disclaimer**: This tool is provided for educational and research purposes only. Misuse of Discord tokens is strictly prohibited and can result in account bans or legal action. Ensure you have explicit permission from Discord before using this tool.

---

## Features
- Reads tokens from a `tokens.txt` file.
- Checks the validity of each token using Discord's API.
- Logs token statuses to a file (`token_status.log`).
- Configurable check interval via `config.json`.

---

## Prerequisites
- Python 3.8 or higher.
- `requests` library (install via `pip install requests`).

---

## Setup

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/discord-token-monitor.git
   cd discord-token-monitor
   ```

2. **Install Dependencies**:
   ```bash
   pip install requests
   ```

3. **Configure the Tool**:
   - Add your tokens to `tokens.txt`, one per line:
     ```
     USER_TOKEN_1
     USER_TOKEN_2
     USER_TOKEN_3
     ```
   - Modify `config.json` to set your preferences:
     ```json
     {
         "log_file": "token_status.log",
         "check_interval": 60
     }
     ```

4. **Run the Tool**:
   ```bash
   python token_monitor.py
   ```

---

## Usage

- The tool will check the status of each token at the specified interval (in seconds) and log the results to `token_status.log`.
- Example log output:
  ```
  2023-10-10 12:00:00 - Token: USER_TOKEN... - Status: Valid
  2023-10-10 12:00:00 - Token: USER_TOKEN... - Status: Invalid
  2023-10-10 12:00:00 - Token: USER_TOKEN... - Status: Error: 429
  ```

---

## Configuration

### `config.json`
- **`log_file`**: The file where token statuses will be logged.
- **`check_interval`**: The interval (in seconds) at which tokens are checked.

### `tokens.txt`
- Add one token per line. Do not include any additional characters or whitespace.

---

## Important Notes
1. **Permission**: Ensure you have explicit written permission from Discord to use this tool. Unauthorized use of Discord tokens is a violation of their Terms of Service.
2. **Security**: Handle tokens with extreme care. Do not share them publicly or store them in insecure locations.
3. **Compliance**: This tool is for monitoring and research purposes only. Do not use it to perform actions on behalf of users.
4. **Rate Limits**: Be mindful of Discord's rate limits. Excessive API requests may result in temporary bans.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Contributing

If you have suggestions or improvements, feel free to open an issue or submit a pull request. Please ensure your contributions align with the project's goals and comply with Discord's policies.

---

## Support

For questions or issues, please open an issue on the [GitHub repository](https://github.com/your-username/discord-token-monitor/issues).

---

**Disclaimer**: This tool is not affiliated with or endorsed by Discord Inc. Use it at your own risk and ensure compliance with all applicable laws and policies.
