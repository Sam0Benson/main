from yoomoney import Authorize

Authorize(
    client_id="323D1C0F4822B05DF8172AFE181E193E746F71311FA6BDE6F84C0AF6D0A3F45F",
    redirect_uri="https://t.me/weatheryadenbot",
    scope=["account-info",
           "operation-history",
           "operation-details",
           "incoming-transfers",
           "payment-p2p",
           "payment-shop",
           ]
)