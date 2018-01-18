# easy_bot

This discord bot began as a joke, but eventually snowballed into the larger project that it is now.
It does basic things like sending emojis, reacting with emojis, and supports role-dependent commands, and also has more advanced
functionalities, such as displaying information about a user's most recent DotA 2 match and giving a brief weather forecast of 
a given city.

The .awk script was used to parse the massive city JSON database to retrieve a python dictionary of each city name and its
corresponding ID.

## How to Use

Visit this [link](https://discordapp.com/api/oauth2/authorize?client_id=392141837051101186&permissions=0&scope=bot) to add this bot to any server you own.
Enter `$info` into a text channel for detailed instructions.

## Built With
* [OpenDota API](https://docs.opendota.com/)

* [OpenWeatherMap API](https://openweathermap.org/api)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
