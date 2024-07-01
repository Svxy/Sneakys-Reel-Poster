<h1 align=center>Sneaky's Reel Poster</h2>

<h4 align=center>
A locally ran Docker Desktop based automation script allowing users to upload a video to Instagram Reels every day at a specific time.

<br><sup>could have come up with a better name...</sup><br>

This makes it a lot easier for accounts that post daily memes or quotes, more specifically the "Day __ of posting ______" style of meme which has recently become somewhat popular on Reels.
</h4>

<br><hr><br>

- [Getting Started]()
    - [Installing](#installing)
    - [Setup](#setup)
    - [Building & Running](#building-and-running)
- [Contributing](#contributing)
- [Copyright](#copyright)

<br><hr><br>

### Installing

<br>

> Click <a href='https://github.com/Svxy/Sneakys-Reel-Poster/archive/refs/heads/main.zip'>here</a> or use the command below.

<br>

- Open PowerShell in the desired directory
- Paste and run the following command:
```shell
git clone https://github.com/Svxy/Sneakys-Reel-Poster.git
```
- If you dont plan on contributing, only keep whats in the <b><a href='app'>/app</a></b> folder.

<br><hr><br>

### Setup

<br>

- To start you're going to want to move your Reel video into the <b><a href='app'>/app</a></b> folder, and then define it in line <b><a href='https://github.com/Svxy/Sneakys-Reel-Poster/blob/6d3adb878d071b767490434907c521be8579e4e6/app/post_reel.py#L33'>33</a></b> of <a href='app/post_reel.py'>post_reel.py</a>:<br>
```python
    video_path = 'PATH/TO/YOUR/VIDEO.mp4'
```
<sup><b>And dont forget to add your desired caption, tags, and posting interval, lines <b><a href='https://github.com/Svxy/Sneakys-Reel-Poster/blob/6d3adb878d071b767490434907c521be8579e4e6/app/post_reel.py#L36'>36</a></b> & <b><a href='https://github.com/Svxy/Sneakys-Reel-Poster/blob/6d3adb878d071b767490434907c521be8579e4e6/app/post_reel.py#L48'>48</a></b>.</b></sup>

<br>

- Next, because the script uses environment variables to define the Username and Password, you'll need to go into the <b><a href='app/run.cmd'>run.cmd</a></b> file and replace the USERNAME and PASSWORD variables to your own login on line <b><a href='https://github.com/Svxy/Sneakys-Reel-Poster/blob/6d3adb878d071b767490434907c521be8579e4e6/app/run.cmd#L8'>8</a></b>.
```shell
docker run -d --name reel-poster -v "%DAY_COUNT_PATH%:/app/day_count.txt" -e USERNAME=IG_USERNAME -e PASSWORD=IG_PASSWORD reel-poster
```

<br><hr><br>

### Building and Running

<br>
<b><sup>Make sure to have Docker Desktop running!</sup></b>
<br>

- After properly setting everything up, you should be able to press and run the <b><a href='app/build.cmd'>build.cmd</a></b> file which will build a new docker container for you to run.
- Next, press and run the <b><a href='app/build.cmd'>run.cmd</a></b> file to start up the container and begin posting your memes every day consistently!

<br>

<b>NOTE:</b> To see the log file open Docker Desktop, and navigate to your container's <b>Files</b> tab, within the file explorer select <b>"app/reel_poster.log"</b> and press the <b>"Open file editor"</b> button.

<br><hr><br>

## Contributing

<br>

I more than welcome any contributions to enhance DupliSweep and make it even better. To contribute, please just be sure to follow these guidelines:

1. Fork the repository on GitHub.
2. Create a new branch from the `main` branch for your feature or bug fix.
3. Commit your changes and push the branch to your forked repository.
4. Submit a pull request with a detailed description of your changes.

<br><hr><br>

## Copyright

Copyright © 2024-2025 TnyavnTo/Svxy/Sneaky<br>[GNU General Public License](LICENSE).

<br>
