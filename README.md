# Secret santa 🧑‍🎄🎅🎁

Small library to create a secret santa for your friends. It also comes with "exceptions" to customize your attributions.


![maman_noel](https://github.com/elias-ramzi/secret_santa/blob/main/maman_noel.jpg)

## How to use it

Start by cloning the repository:
```
$ git clone https://github.com/elias-ramzi/secret_santa.git
$ cd secret_santa
```

Then to customize your repo for your secret santa 🧑‍🎄:

- Enter your email login in `email_login.json` file.
- Add all the participants to the `participants.json` file.
- (Optional) You can customize the email template using the `message.html` file (you will access to the two variables `giver` and `receiver`).
- (Optional) You can customize the `from`, `subject` and `attachement` (a photo) of the emails using the `meta_data.json` file.
- (Optional) Add exceptions to the `exceptions.json` file.
- Use the the script: `$ bash secret_santa.sh`.
