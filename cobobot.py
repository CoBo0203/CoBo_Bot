import asyncio
import discord
client=discord.Client()
async def my_background_task():
    await client.wait_until_ready()
    while not client.is_closed():
        game = discord.Game('코보야 도움을 해보세요!')
        await client.change_presence(status=discord.Status.online, activity=game)
        await asyncio.sleep(3)
        game = discord.Game(f'{len(client.users)}명의 유저와 함께하고 있어요!')
        await client.change_presence(status=discord.Status.online, activity=game)
        await asyncio.sleep(3)
        game = discord.Game('이 메세지는 3초 마다 랜덤으로 바뀌어요!')
        await client.change_presence(status=discord.Status.online, activity=game)
        await asyncio.sleep(3)
        game = discord.Game(f'{len(client.guilds)}개의 서버가 사용하고 있어요!')
        await client.change_presence(status=discord.Status.online, activity=game)
        await asyncio.sleep(3)
        game = discord.Game('제작자를 부를때는 멘션해주세요')
        await client.change_presence(status=discord.Status.online, activity=game)
        await asyncio.sleep(3)
client.loop.create_task(my_background_task())
token="Njc0MDc1NDEzNjc2NTU2Mjk4.Xjjcpw.AEtLKqSfhIBvYcqwCbQ2GS9YnmI"
@client.event
async def on_ready():
    print('CoBo Bot on')
@client.event
async def on_message(message):
    if message.author.bot:
        return None
    async def makeembed(title, description):

        embed=discord.Embed(
            title=title,
            description=description,
            colour=discord.Colour.blue()
        )
        await message.channel.send(embed=embed)
        
    if message.content=='코보야':
        await message.channel.send(f'<@{message.author.id}> **왜요?**(제작자를 부를때는 멘션이나 코보 라고 해주세요)')
    if message.content.startswith('안녕하세요'):
        await message.channel.send('**안녕하세요!(꾸벅)**')
    if message.content=='코보야 뭐해?':
        await message.channel.send( f'<@{message.author.id}>님이랑 대화하고 있었죠:laughing:')
    if message.content=='코보야 ㅎㅇ':
        await message.channel.send(f'<@{message.author.id}> ㅎㅇㅎㅇ')
    if message.content=='코보야 도움':
        await makeembed('**코보 도움말**', '`코보야 ㅎㅇ`\n**사용시:**코보도 같이 인사합니다.\n`코보야 초대`\n**사용시**:코보가 초대링크를 줍니다.\n`코보야 ㅂㅇ또는 ㅃㅇ`\n**사용시**:코보도 잘가라고 인사 해줍니다.\n`코보야 잘가`\n**사용시**:코보가 잘가라고 인사해줍니다.\n`코보야 ㅂㅂ` \n**사용시**:코보도 같이 잘가라고 인사해줍니다.\n`코보야 자기소개`\n**사용시**:코보가 자기소개를 합니다.')
        await makeembed(' ','`코보야 찬양해`\n**사용시**:사용한 사람을 찬양합니다.\n`코보야 좋은 아침 또는 굿모닝`\n**사용시**:아침인사를 해줘요!\n\n**도움말에 없는 명령어도 있어연**\n**알아서 잘 찾아보세요**\n\n**추후 추가 예정**')
    if message.content=='코보야 ...':
        await message.channel.send('....?')
    if message.content.startswith('ㅋㅋ'):
        await message.channel.send('ㅋㅋㅋ')
    if message.content=='ㅋ':
        await message.channel.send('ㅋㅋㅋ')
    if message.content=='코보야 초대':
        await message.channel.send('https://discordapp.com/api/oauth2/authorize?client_id=674075413676556298&permissions=0&scope=bot\n 이 링크로 초대 하실수 있어요!')
    if message.content=='코보야 배고파':
        await message.channel.send('저는 맛없어요!')
    if message.content=='코보야 ㅃㅇ':
        await message.channel.send('ㅂㅇㅂㅇ')
    if message.content=='코보야 잘가':
        await message.channel.send('내일 또 만나요~~')
    if message.content=='코보야 돈줘':
        await message.channel.send('저도 돈이 없는 걸요?')
    if message.content=='코보야 돈내놔':
        await message.channel.send('그러지 마세요')
    if message.content=='코보야 ㅂㅇ':
        await message.channel.send('ㅂㅇㅂㅇ')
    if message.content=='코보야 ㅂㅂ':
        await message.channel.send('ㅂㅂ 다음에 만나요~~')
    if message.content=='코보야 자기소개':
        await makeembed('CoBo Bot','제작자:CoBo\n\n언어:python\n\n종류:대화봇')
    if message.content=='코보야 심심해':
        await message.channel.send('저도요')
    if message.content=='코보야 놀자':
        await message.channel.send('싫어요')
    if message.content=='코보야 코로나':
        await message.channel.send('후덜덜 무서워요:cold_sweat:')
    if message.content=='코보야 찬양해':
        await makeembed('찬양하라',f'**{message.author.name}**을(를)찬양해! ')
    if message.content=='룰루랄라':
        await message.channel.send('히힛♪♪')
    if message.content=='코보봇 바보':
        await makeembed('내가 모를 줄 알았냐?',f'<@!{message.author.id}> 조용이해 나쁜넘아')
    if message.content=='코보야 죽어':
        await message.channel.send(':rage: 뒤지실?')
    if message.content=='코보야 저리가':
        await message.channel.send('너가 가면 되잖아')
    if message.content=='코보야 이리와':
        await message.channel.send('니가 오면 되잖아')
    if message.content=='코보야 사랑해':
        await message.channel.send(':two_hearts: 저도요!')
    if message.content=='안녕':
        await message.channel.send('**안녕!**')
    if message.content=='코보야 안녕':
        await message.channel.send(f'<@{message.author.id}> ㅎㅇ')
    if message.content=='코보야 음악':
        await makeembed('만들줄 모름',f'**{message.author.name}**님 음악 기능 만드는 법 좀 알려주세요 ㅠㅠ')
    if message.content=='코보야 도움말':
        await makeembed('안내 메세지','`코보야 도움`을 입력해 주세요')
    if message.content.startswith('ㅠ'):
        await message.channel.send(f'{message.author.name}님 슬퍼 하지 말아여(토닥)')
    if message.content.startswith('ㅜ'):
        await message.channel.send(f'{message.author.name}님 슬퍼 하지 말아여(토닥)')
    if message.content=='코보야 좋은 아침':
        await message.channel.send('좋은 아침!')        
    if message.content=='코보야 굿모닝':
        await message.channel.send('굿모닝!')
    if message.content=='코보야 응답해':
        await makeembed('무전기 넘어로 들리는 소리','지지지직 코보 여기 있어요')
    if message.content=='코보야 꺼져':
        await message.channel.send('너부터....꺼져 :middle_finger:')
    if message.content=='코보야 뒈져':
        await message.channel(' :middle_finger: ')
    if message.content=='코보야 뒤져':
        await message.channel(' :middle_finger: ')
    if message.content==':rage:':
        await message.channel('화내지 마세요오')
client.run(token)