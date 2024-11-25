Quick Start
===========

Get the price of a token on the Solana blockchain

.. code-block:: python

    from birdeyepy import BirdEye

    client = BirdEye(api_key="your-api-key")  # 'x-chain' header defaults to solana

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

Get the price of a token on the Ethereum blockchain

.. code-block:: python

    from birdeyepy import BirdEye

    client = BirdEye(api_key="your-api-key", chain="ethereum")

    client.defi.price(address="0x514910771af9ca656af840dff83e8264ecf986ca")
