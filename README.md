# DigitalOceanBot
DigitalOcean droplets status bot
Helps in retrieving the status of all the droplets available on DigitalOcean.

### Environment Variables
1. FLASK_APP - Entry point for the flask app. In this case, dostatbot.py
2. APP_ENV - Development/Testing/Debugging/Production
3. SLACK_CHANNEL - Name of the channel where the bot should post its replies
4. DIGITAL_OCEAN_TOKEN - Token generated from DigitalOcean to access their API
5. SLACK_BOT_TOKEN - Bot token generated from Slack API
6. SECRET - Slack secret which shall be passed along with token to access slack api
7. OAuth - OAuth token generated on slack 

### Usage
1. /dostat help - Displays all possible commands
2. /dostat droplets - Provides a list of all the available droplets with their IPs and status on digitalocean
3. /dostat status [droplet_name] - Provides the status of any individual droplet with its IP address
4. /dostat reboot [droplet_name] - Reboots mentioned droplet on digitalocean

### Development progress
- [x] Initial development
- [x] Heroku deployable code and dependencies
- [x] Individual droplet status functionality
- [x] Reboot droplet command
- [x] Add request cache to reduce overhead on the server, works in the case of status command
- [ ] Add more commands to interact with droplets
- [ ] Add ssh connection functionality
