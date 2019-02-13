# <h1 align="center"> Kumbh - Bot </h1> <br>
<p align="center">
  <a href="https://github.com/shruti8019/Kumbh-bot">
    <img alt="Check on Zulip Chat" title="Kumbh-Bot" 
  </a>
</p>
<p align="center">
  Bot designed to serve the huge gathering of "THE KUMBH MELA".
</p>



## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Deploy](#deploy)
- [Screenshots](#screenshots)
- [Feedback](#feedback)
- [Contributors](#contributors)
- [Contribute](#contribute)
- [Announcements](#announcements)
- [Acknowledgement](#acknowledgment)

## Introduction

Kumbh-Bot is designed to serve the huge gathering of kumbh mela. Built with Python and ZulipChat-Api, Kumbh-Bot is a feature-rich unofficial ZulipChat Bot that is 100% free.



## Features

Kumbh-Bot holds following features -

* Important dates and events.
* Train enquiry
    -Train between stations
    -Train arriving at stations
    -Train routes
* Play Kumbh-mela Bhajans via links.
* Nearby restuarants and hotels.
* Weather forecasting
* News updates
* Nearby hospitals and police stations.
* Emergency contact
* Lost & Found Services 

 

## Deploy

To deploy Kumbh bot using your local machine as server, follow following steps -

* Firstly create a zulip organisation on which you want to deploy bot. If you already have one then you may skip this step.
* Register a new bot user on the Zulip server's web interface.
	* Log in to the Zulip server.
	* Navigate to Settings -> Your bots -> Add a new bot. Select Generic bot for bot type, set both bot-name and bot username to KumbhBot and click on Create bot.
	* A new bot user should appear in the Active bots panel.
* Download the bot's zuliprc configuration file to your computer.
	* Go to Settings -> Your bots
	* In the Active bots panel, click on the little green download icon to download its configuration file zuliprc (the structure of this file is explained here).

* Install all required python packages, rum command ```pip3 install -r requirements.txt```
* Now we are all set, to run bot enter following command ```zulip-run-bot <absolute path to kumbhBot.py file > --config-file <absolute path to downloaded zuliprc file>```

Example Usage - ```zulip-run-bot ~/Projects/KumbhBot/bot/kumbhBot --config-file ~/Projects/KumbhBot/bot/zuliprc```
* You can now finally use power of KumbhBot in your organisation.

## Screenshots

<strong> Hello user!! :</strong>
<p align="center">
  <img src = "https://github.com/shruti8019/Kumbh-bot/blob/master/KumbhBot/images/Hello.png">
</p>

<strong> News :</strong>
<p align="center">
  <img src = "https://github.com/shruti8019/Kumbh-bot/blob/master/KumbhBot/images/news.png">
</p>

<strong> Weather :</strong>
<p align="center">
  <img src = "https://github.com/shruti8019/Kumbh-bot/blob/master/KumbhBot/images/weather.png">
</p>

<strong> Play Bhajan:</strong>
<p align="center">
  <img src = "https://github.com/shruti8019/Kumbh-bot/blob/master/KumbhBot/images/bhajan.png">
</p>



## Feedback

Feel free to send us feedback on [Email](mailto:support@kumbh-bot.tech) or [file an issue](https://github.com/shruti8019/Kumbh-bot/issues).

## Contributors

<ul>
  <li> <a href="https://github.com/shruti8019">Shruti Jagwani</a></li>
  <li> <a href="https://github.com/ria567">Ria Jain</a></li>
  <li> <a href="https://github.com/imharshita07">Harshita Rastogi</a></li>
  <li> <a href="https://github.com/araishaftab5">Araish Aftab</a></li>
</ul>

## Contribute

<ul>
  <li>Feel free to report issues and bugs.It will be helpful for future launches of application.</li>
  <li>All Suggestions are welcome.</li>
  <li>Fork repository and Contribute.</li>
</ul>

## Acknowledgment

Thanks to [Zulip](https://zulipchat.com/) for providing Zulip Api and Platform.
