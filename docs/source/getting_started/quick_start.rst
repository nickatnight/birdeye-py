Quick Start
===========

Get the price of a token on the Solana blockchain

.. code-block:: python

    from birdeyepy import BirdEye

    client = BirdEye(api_key="your-api-key") # 'x-chain' header defaults to solana

    # DEFI

    # https://docs.birdeye.so/reference/get_defi-price
    client.defi.price()  # defaults to So11111111111111111111111111111111111111112

    client.defi.price(
        address="Gr11mosZNZjwpqnemXNnWs9E2Bnv7R6vzaKwJTdjo8zQ",
        include_liquidity=True,  # can also use strings 'true' or 'false'
    )

    # https://docs.birdeye.so/reference/get_defi-history-price
    client.defi.history(time_from=1732398942, time_to=1732398961)  # defaults to So11111111111111111111111111111111111111112

    client.defi.history(
        time_from=1732398942,
        time_to=1732398961,
        address="Gr11mosZNZjwpqnemXNnWs9E2Bnv7R6vzaKwJTdjo8zQ",
        address_type="token",  # or 'pair'...defaults to 'token'
        type_in_time="15m"  # default
    )

    # TOKEN

    # https://docs.birdeye.so/reference/get_defi-tokenlist
    client.token.list_all()

    # https://docs.birdeye.so/reference/get_defi-token-security
    client.token.security(address="Gr11mosZNZjwpqnemXNnWs9E2Bnv7R6vzaKwJTdjo8zQ")

    # https://docs.birdeye.so/reference/get_defi-token-overview
    client.token.overview(address="Gr11mosZNZjwpqnemXNnWs9E2Bnv7R6vzaKwJTdjo8zQ")

    # https://docs.birdeye.so/reference/get_defi-token-creation-info
    client.token.creation_info(address="Gr11mosZNZjwpqnemXNnWs9E2Bnv7R6vzaKwJTdjo8zQ")

    # https://docs.birdeye.so/reference/get_defi-token-trending
    client.token.trending()

    # https://docs.birdeye.so/reference/post_defi-v2-tokens-all
    client.token.list_all_v2()

    # https://docs.birdeye.so/reference/get_defi-v2-tokens-new-listing
    client.token.new_listing(
        time_to=1732398961,
        meme_platform_enabled=True,  # can also use strings 'true' or 'false'
    )

    # https://docs.birdeye.so/reference/get_defi-v2-tokens-top-traders
    client.token.top_traders(address="Gr11mosZNZjwpqnemXNnWs9E2Bnv7R6vzaKwJTdjo8zQ")

    # https://docs.birdeye.so/reference/get_defi-v2-markets
    client.token.all_markets(address="Gr11mosZNZjwpqnemXNnWs9E2Bnv7R6vzaKwJTdjo8zQ")

    # https://docs.birdeye.so/reference/get_defi-v3-token-meta-data-single
    client.token.market_metadata_single(address="Gr11mosZNZjwpqnemXNnWs9E2Bnv7R6vzaKwJTdjo8zQ")

    # https://docs.birdeye.so/reference/get_defi-v3-token-meta-data-multiple
    client.token.market_metadata_multiple(
        addresses=["Gr11mosZNZjwpqnemXNnWs9E2Bnv7R6vzaKwJTdjo8zQ", "AGQZRtz7hZtz3VJ1CoXRMNMyh2ZMZ1g6pv4aGMUSpump"],
    )  # can also use comma separated strings 'Gr11mosZNZjwpqnemXNnWs9E2Bnv7R6vzaKwJTdjo8zQ,AGQZRtz7hZtz3VJ1CoXRMNMyh2ZMZ1g6pv4aGMUSpump'

    # https://docs.birdeye.so/reference/get_defi-v3-token-market-data
    client.token.market_data(address="Gr11mosZNZjwpqnemXNnWs9E2Bnv7R6vzaKwJTdjo8zQ")

    # https://docs.birdeye.so/reference/get_defi-v3-token-trade-data-single
    client.token.trade_data_single(address="Gr11mosZNZjwpqnemXNnWs9E2Bnv7R6vzaKwJTdjo8zQ")

    # https://docs.birdeye.so/reference/get_defi-v3-token-trade-data-multiple
    client.token.trade_data_multiple(
        addresses=["Gr11mosZNZjwpqnemXNnWs9E2Bnv7R6vzaKwJTdjo8zQ", "AGQZRtz7hZtz3VJ1CoXRMNMyh2ZMZ1g6pv4aGMUSpump"],
    )  # can also use comma separated strings 'Gr11mosZNZjwpqnemXNnWs9E2Bnv7R6vzaKwJTdjo8zQ,AGQZRtz7hZtz3VJ1CoXRMNMyh2ZMZ1g6pv4aGMUSpump'

    # https://docs.birdeye.so/reference/get_defi-v3-token-holder
    client.token.holder(address="Gr11mosZNZjwpqnemXNnWs9E2Bnv7R6vzaKwJTdjo8zQ")

Get the price of a token on the Ethereum blockchain

.. code-block:: python

    from birdeyepy import BirdEye

    client = BirdEye(api_key="your-api-key", chain="ethereum")

    client.defi.price(address="0x514910771af9ca656af840dff83e8264ecf986ca")
