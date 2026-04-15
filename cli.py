import argparse
import logging

from bot.client import BinanceClient
from bot.orders import place_order
from bot.validators import validate_input
from bot.logging_config import setup_logger


def main():
    setup_logger()

    parser = argparse.ArgumentParser(description="Binance Futures Trading Bot")

    parser.add_argument("--symbol", required=True, help="e.g. BTCUSDT")
    parser.add_argument("--side", required=True, help="BUY or SELL")
    parser.add_argument("--type", required=True, help="MARKET or LIMIT")
    parser.add_argument("--quantity", type=float, required=True)
    parser.add_argument("--price", type=float)

    args = parser.parse_args()

    try:
        # ✅ Validate input
        validate_input(args.symbol, args.side, args.type, args.quantity, args.price)

        # ✅ Initialize client
        client = BinanceClient().get_client()

        print("\n📤 Order Request Summary")
        print("----------------------------")
        print(f"Symbol   : {args.symbol}")
        print(f"Side     : {args.side}")
        print(f"Type     : {args.type}")
        print(f"Quantity : {args.quantity}")
        print(f"Price    : {args.price}")
        print("----------------------------")

        # ✅ Place order
        order = place_order(
            client,
            args.symbol,
            args.side,
            args.type,
            args.quantity,
            args.price
        )

        print("\n✅ Order Placed Successfully!")
        print("----------------------------")
        print(f"Order ID      : {order.get('orderId')}")
        print(f"Status        : {order.get('status')}")
        print(f"Executed Qty  : {order.get('executedQty')}")
        print(f"Avg Price     : {order.get('avgPrice')}")
        print("----------------------------")

    except Exception as e:
        print("\n❌ Error:", str(e))
        logging.error(str(e))


if __name__ == "__main__":
    main()