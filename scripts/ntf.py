import firebase_admin
from firebase_admin import messaging, credentials

# FCM API 設定
cred = credentials.Certificate(
    "pushnotificationtestandr-efa03-firebase-adminsdk-qsalv-b941f1a9bb.json")
firebase_admin.initialize_app(cred)

# 送信先デバイスのトークン
device_token = 'eyO-RefMRDugBwhmSFC_Gj:APA91bEe5x6OOvvgUGk-9KYw9GBa5_nozhlOX7XQrIoqRHS17qfCXZKAo0jtm2pathjDqXX0Y7k7ND-n08w7o2mWSq3ckyLHsE5AiRgjlkMOK_8TXxMV6dwAkem6b7Pb5NgmgsiO2vzL'

# 通知のタイトルと本文
message = messaging.Message(
    # data={
    #     'title': 'Test',
    #     'body': 'テスト',
    #     'sound': 'default',
    #     'tag': 'default',
    #     'collapse_key': 'collapse_key'
    # },
    android=messaging.AndroidConfig(
        collapse_key='collapse_key',
        notification=messaging.AndroidNotification(
          title="Test",
          body="オーバーライド",
          sound="default",
          tag="override",
        )
    ),
    token=device_token,
)

print(message)
messaging.send(message)
