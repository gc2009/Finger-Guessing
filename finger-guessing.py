"""
@author: GaoChang
"""
from rich.console import Console
from random import choice
CONTENT = {1: "石头", 2: "剪刀", 3: "布"}
QUESTION_STYLE = 'cyan bold'
OUTPUT_RESULT_STYLE = 'italic green'
PUNCH_OUT_STYLE = 'magenta'
npcWin = playerWin = allPlay = 0

# 1:石头, 2:剪刀, 3:布
def judge(content: dict) -> str or None:
    """
    通过提供的字典, 来判断谁输。
    1:石头, 2:剪刀, 3:布
    返回输家, None为平局
    """
    players = list(content.keys())
    values = list(content.values())
    player1_result = values[0]
    player2_result = values[1]

    if player1_result == player2_result:
        return None
    elif player1_result == 1 and player2_result == 3:
        return players[0]
    elif player1_result == 3 and player2_result == 1:
        return players[1]
    elif player1_result < player2_result:
        return players[1]
    else: return players[0]


console = Console()
console.rule('[bold cyan]剪刀石头布')
console.print("[green]您好, 我是NPC。接下来, 您的游戏将与我进行!", justify='center')
console.print("[magenta bold]在游戏开始之前, 我们需要进行初始化")

console.print("您希望NPC叫什么名字?\n[NPC] ",style=QUESTION_STYLE,end='')
npcName = input()
if npcName.replace(' ', '') == '':
    npcName = "NPC"
console.print(f'NPC的名字已设置为: {npcName}',style=OUTPUT_RESULT_STYLE)

console.print("您希望您叫什么名字?\n[Player] ",style=QUESTION_STYLE,end='')
playerName = input()
if playerName.replace(' ', '') == '':
    playerName = "Player"
console.print(f'您的名字已设置为: {npcName}',style=OUTPUT_RESULT_STYLE)
console.rule("[green]初始化完毕 以下为游戏说明")
console.print("[red bold]1. <Enter> = 出拳\n2. 输入'quit' = 退出", justify='center')
console.rule('[green]游戏说明')
print()

def punchOut() -> int:
    return choice([1, 2, 3])
while True:
    npcResult = punchOut()
    console.print(f"{npcName}已出拳, 结果: {CONTENT[npcResult]}", style=PUNCH_OUT_STYLE)
    get = console.input("[cyan]> ")
    if get == 'quit':
        console.rule('[cyan]游戏总结')
        console.print(f'[magenta]你们总共玩了{allPlay}局, 其中:',justify='center')
        console.print(f'[magenta]你赢了{playerWin}局\n{npcName}赢了{npcWin}局\n有{allPlay - (playerWin+npcWin)}局是平局', justify='center')
        if npcWin > playerWin:
            console.print(f'[red]看来, 你还是打不过{npcName}啊!',justify='center')
        elif npcWin < playerWin:
            console.print(f'[green]看来, 你还是有点实力!',justify='center')
        else:
            console.print(f'[cyan]你这把和{npcName}打成平手, 还得练!',justify='center')
        console.rule('[yellow bold]算了, 老子不陪你玩了, 走了!')
        break
    else:
        playerResult = punchOut()
        console.print(f"{playerName}已出拳, 结果: {CONTENT[playerResult]}", style=PUNCH_OUT_STYLE)
        loser = judge({npcName: npcResult, playerName: playerResult})
        if (loser != None):
            if (loser == npcName):
                console.print(f'[green]{npcName}输了, 你逃过一劫!')
                playerWin += 1
            else:
                console.print(f'[red]你输了!!!')
                npcWin += 1
        else: console.print('[cyan]是平局!')
        allPlay += 1
        print()