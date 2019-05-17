import discord, urllib.request, json, copy
from discord.ext import commands
from city_dictionary import city_dic

class Weather():
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def weather(self, ctx, *args):
        api_key = API_KEY
        cityID = ''

        """Retrieve city ID from dictionary"""
        if len(args) == 0:
            await self.bot.say('Not enough arguments. Usage: \'$weather city_name\'')
        elif len(args) == 1:
            if args[0].lower() == 'athens':
                cityID = 4180386
            else:
                cityID = city_dic[args[0].title()]
        elif len(args) == 2:
            cityID = city_dic[args[0].title() + ' ' + args[1].title()]
        elif len(args) == 3:
            cityID = city_dic[args[0].title() + ' ' + args[1].title() + ' ' + args[2].title()]
        else:
            await self.bot.say('Too many arguments. Usage: \'$weather city_name\'')

        api_url = 'http://api.openweathermap.org/data/2.5/weather?id=' + str(cityID) + '&appid=' + api_key
        api_url_3 = 'http://api.openweathermap.org/data/2.5/forecast?id=' + str(cityID) +'&appid=' + api_key

        #current forecast
        with urllib.request.urlopen(api_url) as url:
            wdata = json.loads(url.read().decode())
        #five day forecast (used as 3)
        with urllib.request.urlopen(api_url_3) as url:
            wdata3 = json.loads(url.read().decode())
        
        weather_icon_url = ''
        hex_color = 0x000000

        #set icon/embed color based on weather
        if 'clear' in wdata["weather"][0]["main"].lower():
            weather_icon_url = 'https://upload.wikimedia.org/wikipedia/commons/thumb/e/e7/Gnome-weather-clear.svg/2000px-Gnome-weather-clear.svg.png'
            hex_color = 0x42c2f4
        elif 'clouds' in wdata["weather"][0]["main"].lower():
            weather_icon_url = 'http://res.freestockphotos.biz/pictures/15/15146-illustration-of-a-stormy-cloud-pv.png'
            hex_color = 0x808384
        elif 'snow' in wdata["weather"][0]["main"].lower():
            weather_icon_url = 'https://cdn4.iconfinder.com/data/icons/weather-29/256/snowflake-512.png'
            hex_color = 0xffffff
        elif 'rain' in wdata["weather"][0]["main"].lower():
            weather_icon_url = 'http://www.cavagnac.com/templates/cavagnac/inc_files/weather/rain.png'
            hex_color = 0x3b83cc
        elif 'mist' in wdata["weather"][0]["main"].lower():
            weather_icon_url = 'http://cdn.onlinewebfonts.com/svg/img_541488.png'
            hex_color = 0xdae1e8

        temp_k = wdata["main"]["temp"]
        temp_c = temp_k - 273.15
        temp_f = (temp_c * 1.8) + 32

        wdata3temps = [(wdata3["list"][7]["main"]["temp_max"]), (wdata3["list"][15]["main"]["temp_max"]),
                       (wdata3["list"][23]["main"]["temp_max"])]
        
        wdata3_c = copy.deepcopy(wdata3temps)
        wdata3_c[:] = [x - 273.15 for x in wdata3_c]

        wdata3_f = copy.deepcopy(wdata3_c)
        wdata3_f[:] = [(x * 1.8) + 32 for x in wdata3_f]

        emb = (discord.Embed(description='__**' + wdata["name"].title() + '**__\n'
                            '' + wdata["weather"][0]["description"].title() + '\n'
                            '' + "{:.2f}".format(temp_c) + '°C/' + "{:.2f}".format(temp_f) + '°F\n\n'
                            '**Three Day Forecast**\n'
                            '\t' + wdata3["list"][7]["weather"][0]["main"] + '  |  '
                            '' + wdata3["list"][15]["weather"][0]["main"] + '  |  '
                            '' + wdata3["list"][23]["weather"][0]["main"] + '  |  \n'
                            'C: ' + '{:.2f}'.format(wdata3_c[0]) + '  |  '
                            '{:.2f}'.format(wdata3_c[1]) + '  |  '
                            '{:.2f}'.format(wdata3_c[2]) + '  |  \n'
                            'F:  ' + '{:.2f}'.format(wdata3_f[0]) + '  |  '
                            ' {:.2f}'.format(wdata3_f[1]) + '  |  '
                            ' {:.2f}'.format(wdata3_f[2]) + '  |  '
                            , color=hex_color))
        emb.set_author(name='Weather Forecast', icon_url=weather_icon_url)
        await self.bot.say(embed=emb)
        
def setup(bot):
    bot.add_cog(Weather(bot))
