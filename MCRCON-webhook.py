from mcrcon import MCRcon
import time
import requests
import json
import datetime

# define
svr_ip = "localhost"
svr_rcon_port = 25575
svr_rcon_pass = "password"
webhook_url = "https://discord.com/api/webhooks/xxxxxxxx"
before_list_set = set() # 前回値を初期化

def send_webhook(player_name, event_type):
    if not webhook_url:
        print("DISCORD Webhook URLを指定してください")

    if event_type == 'join':
        # 入室時
        title = "プレイヤー参加通知"
        description = "以下のプレイヤーがワールドに参加しました"
        color = 0x00ff00 # RGB 緑色
        
    elif event_type == 'left':
        # 退室時
        title = "プレイヤー退出通知"
        description = "以下のプレイヤーがワールドから退出しました"
        color = 0xff0000 # RGB 赤色
        
    else :
        # その他
        title = "不明なイベント"
        description = "予期せぬプレイヤーイベント"
        color = 0x808080 # RGB 灰色

    # fields
    fields = [{"name": "MCID", "value": mcid, "inline": True} for mcid in player_name]

    # message本体
    message = {
        "embeds": [
            {
                "title": title,
                "description": description,
                "color": color,
                "fields": fields,
                "timestamp": datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9))).isoformat()
            }
        ]
    }

    headers = {
        'Content-Type': 'application/json'
        }

    # webhookを送信
    resp_web = requests.post(webhook_url, data=json.dumps(message), headers=headers)

    # 送信可否の判断
    if resp_web.status_code == 204:
        print("[INFO]Webhookの送信に成功", end='')
    else:
        print("[INFO]Webhookの送信に失敗", end='')

    if event_type == 'join':
        print(f" MCID：{','.join(player_name)}の参加")
    elif event_type == 'left':
        print(f" MCID：{','.join(player_name)}の退室")
    

# MAIN
with MCRcon(svr_ip, svr_rcon_pass, svr_rcon_port) as mcr:
    while True:
        resp = mcr.command("/list")
        # print(resp) 生の返却値

        current_list = resp.split(":")
        if current_list[1].strip(): # 分割した[:]の後の空白を消して文字があるかどうか
            current_list = current_list[1]
            current_list = [p.strip() for p in current_list.split(",")]
        else:
            current_list = []
        
        after_list_set = set(current_list)

        # 前回処理時と比較
        joined_players = after_list_set - before_list_set
        left_players = before_list_set - after_list_set

        # 入退室判定
        if joined_players:
            # 参加処理
            send_webhook(joined_players, "join")
            
        elif left_players:
            # 退室処理
            send_webhook(left_players, "left")

        # 前回値の更新
        before_list_set = after_list_set
        time.sleep(1)
