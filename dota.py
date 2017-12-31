import discord, urllib.request, json
from discord.ext import commands
from data_dictionary import hero_dic
from data_dictionary import item_dic
from data_dictionary import game_mode_dic

class Dota():
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(pass_context=True)
    async def last(self, ctx):
        userID = ctx.message.author.id
        accID = ''

        """manually add new users here"""
        if userID == '84889907926925312': #zealios/me
            accID = 83738863
        elif userID == '95033934164795392': #arul/snoh
            accID = 113469964
        elif userID == '140259241431662593': #Michael Liang/mallam
            accID = 123743013
        elif userID == '191417957144985600': #Colton Reitz/vaeth
            accID = 63699181
        elif userID == '85112859758977024' or userID == '383053722550534144': #Edward Xia/Napalm Eggrollz
            accID = 82318628
        elif userID == '92360169446473728': #Kenny Kim/Mitochondria
            accID = 237209977
        elif userID == '294982578723880962' or userID == '137399080497184768': #Chase Meadows
            accID = 76378628
        elif userID == '200679705991446529': #Alex Grigorian
            accID = 64010004
        
        with urllib.request.urlopen('https://api.opendota.com/api/players/' + str(accID) + '/recentMatches') as url:
            recentmatches = json.loads(url.read().decode())
            matchID = recentmatches[0]["match_id"]
        
        with urllib.request.urlopen('https://api.opendota.com/api/matches/' + str(matchID)) as url:
            data = json.loads(url.read().decode())
            winner = 'Radiant Victory' if data["radiant_win"] == True else 'Dire Victory'
                
        game_mode = game_mode_dic[data["game_mode"]]

        class Player:
            def __init__(self, username, accountID, hero, items, kda, lhd, team):
                self.username = username
                self.accountID = accountID
                self.hero = hero
                self.team = team
                self.items = items
                self.kda = kda
                self.lhd = lhd

            def setname(self, username):
                self.username = username

            def sethero(self, hero):
                self.hero = hero

            def setitems(self, items):
                self.items = items[:]

            def setkda(self, kda):
                self.kda = kda

            def setlhd(self, lhd):
                self.lhd = lhd

        p1 = Player('', data["players"][0]["account_id"], '', [None, None, None, None, None, None], '', '', 'Radiant' if data["players"][0]["isRadiant"] else 'Dire')
        p2 = Player('', data["players"][1]["account_id"], '', [None, None, None, None, None, None], '', '', 'Radiant' if data["players"][1]["isRadiant"] else 'Dire')
        p3 = Player('', data["players"][2]["account_id"], '', [None, None, None, None, None, None], '', '', 'Radiant' if data["players"][2]["isRadiant"] else 'Dire')
        p4 = Player('', data["players"][3]["account_id"], '', [None, None, None, None, None, None], '', '', 'Radiant' if data["players"][3]["isRadiant"] else 'Dire')
        p5 = Player('', data["players"][4]["account_id"], '', [None, None, None, None, None, None], '', '', 'Radiant' if data["players"][4]["isRadiant"] else 'Dire')
        p6 = Player('', data["players"][5]["account_id"], '', [None, None, None, None, None, None], '', '', 'Radiant' if data["players"][5]["isRadiant"] else 'Dire')
        p7 = Player('', data["players"][6]["account_id"], '', [None, None, None, None, None, None], '', '', 'Radiant' if data["players"][6]["isRadiant"] else 'Dire')
        p8 = Player('', data["players"][7]["account_id"], '', [None, None, None, None, None, None], '', '', 'Radiant' if data["players"][7]["isRadiant"] else 'Dire')
        p9 = Player('', data["players"][8]["account_id"], '', [None, None, None, None, None, None], '', '', 'Radiant' if data["players"][8]["isRadiant"] else 'Dire')
        p10 = Player('', data["players"][9]["account_id"], '', [None, None, None, None, None, None], '', '', 'Radiant' if data["players"][9]["isRadiant"] else 'Dire')

        players = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10]

        """check for null username"""
        for i, x in enumerate(players):
            if data["players"][i]["account_id"] == None:
                x.setname('Unknown')
            else:
                x.setname(data["players"][i]["personaname"])

        """set hero for each player"""
        for i, x in enumerate(players):
            x.sethero(hero_dic[data["players"][i]["hero_id"]])

        """fill items list"""
        for i, x in enumerate(players):
            itemlist = [data["players"][i]["item_0"], data["players"][i]["item_1"],
                        data["players"][i]["item_2"], data["players"][i]["item_3"],
                        data["players"][i]["item_4"], data["players"][i]["item_5"]]
            
            itemnames = [item_dic[itemlist[0]], item_dic[itemlist[1]],
                        item_dic[itemlist[2]], item_dic[itemlist[3]],
                        item_dic[itemlist[4]], item_dic[itemlist[5]]]
            x.setitems(itemnames)

        """set kda"""
        for i, x in enumerate(players):
            x.setkda(str(data["players"][i]["kills"]) + '/' + str(data["players"][i]["deaths"]) + '/' + str(data["players"][i]["assists"]))

        """set last hits/denies"""
        for i, x in enumerate(players):
            x.setlhd(str(data["players"][i]["last_hits"]) + '/' + str(data["players"][i]["denies"]))
                         
        linkstr = 'https://www.dotabuff.com/matches/' + str(data["match_id"])

        """embed object to be sent as a message in discord"""
        emb = (discord.Embed(description='**' + str(winner) + '**\n'
                #'Match ID: ' + str(data["match_id"]) + '\n'
                'Dotabuff: ' + linkstr + '\n'
                'Game mode: ' + str(game_mode) + '\n\n'
                '__**Radiant:**__\n'
                '**' + str(p1.hero) + '\t' + str(p1.username) + '\nKDA: ' + str(p1.kda) + '\t LH/D: ' + str(p1.lhd) + '**\n' + str(p1.items) +'\n\n'
                '**' + str(p2.hero) + '\t' + str(p2.username) + '\nKDA: ' + str(p2.kda) + '\t LH/D: ' + str(p2.lhd) + '**\n' + str(p2.items) +'\n\n'
                '**' + str(p3.hero) + '\t' + str(p3.username) + '\nKDA: ' + str(p3.kda) + '\t LH/D: ' + str(p3.lhd) + '**\n' + str(p3.items) +'\n\n'
                '**' + str(p4.hero) + '\t' + str(p4.username) + '\nKDA: ' + str(p4.kda) + '\t LH/D: ' + str(p4.lhd) + '**\n' + str(p4.items)+'\n\n'
                '**' + str(p5.hero) + '\t' + str(p5.username) + '\nKDA: ' + str(p5.kda) + '\t LH/D: ' + str(p5.lhd) + '**\n' + str(p5.items)+'\n\n'
                '__**Dire:**__\n'
                '**' + str(p6.hero) + '\t' + str(p6.username) + '\nKDA: ' + str(p6.kda) + '\t LH/D: ' + str(p6.lhd) + '**\n' + str(p6.items)+'\n\n'
                '**' + str(p7.hero) + '\t' + str(p7.username) + '\nKDA: ' + str(p7.kda) + '\t LH/D: ' + str(p7.lhd) + '**\n' + str(p7.items)+'\n\n'
                '**' + str(p8.hero) + '\t' + str(p8.username) + '\nKDA: ' + str(p8.kda) + '\t LH/D: ' + str(p8.lhd) + '**\n' + str(p8.items)+'\n\n'
                '**' + str(p9.hero) + '\t' + str(p9.username) + '\nKDA: ' + str(p9.kda) + '\t LH/D: ' + str(p9.lhd) + '**\n' + str(p9.items)+'\n\n'
                '**' + str(p10.hero) + '\t' + str(p10.username) + '\nKDA: ' + str(p10.kda) + '\t LH/D: ' + str(p10.lhd) + '**\n' + str(p10.items) + '\n\n'
                , color=0xFF0000))
        emb.set_author(name='Your most recent DotA match', icon_url='https://res.cloudinary.com/teepublic/image/private/s--Ky-AFUEY--/t_Preview/b_rgb:191919,c_limit,f_jpg,h_630,q_90,w_630/v1475182893/production/designs/706906_1.jpg')
        await self.bot.say(embed=emb)
        

def setup(bot):
    bot.add_cog(Dota(bot))
