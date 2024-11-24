BirdEye Client
==============

.. toctree::
    :maxdepth: 1
    :caption: Resources

    resources/defi
    resources/token
    resources/trader


.. note::

    The BirdEye api requires an ``x-chain`` or ``x-chains`` header to be set in each request. The client will initialize with ``solana`` by default. See :class:`birdeyepy.utils.BirdEyeChainEnum`:


.. autoclass:: birdeyepy.birdeye.BirdEye
    :members:

APIs
----

.. code-block:: python

    from birdeyepy import BirdEye

    client = BirdEye(api_key="your-api-key")

    # DEFI

    # https://public-api.birdeye.so/defi/price
    client.defi.price()  # defaults to So11111111111111111111111111111111111111112

    client.defi.price(
        address="Gr11mosZNZjwpqnemXNnWs9E2Bnv7R6vzaKwJTdjo8zQ",
        include_liquidity=True,  # can also use strings 'true' or 'false'
    )

    # https://public-api.birdeye.so/defi/history_price
    client.defi.history(time_from=1732398942, time_to=1732398961)  # defaults to So11111111111111111111111111111111111111112

    client.defi.history(
        time_from=1732398942,
        time_to=1732398961,
        address="Gr11mosZNZjwpqnemXNnWs9E2Bnv7R6vzaKwJTdjo8zQ",
        address_type="token",  # or 'pair'...defaults to 'token'
        type_in_time="15m"  # default
    )

    # TOKEN

    # https://public-api.birdeye.so/defi/tokenlist
    client.token.list_all()

    # TRADER

    # https://docs.birdeye.so/reference/get_trader-gainers-losers
    client.trader.gainers_losers()

    # https://public-api.birdeye.so/trader/txs/seek_by_time
    client.trader.seek_by_time(address="Gr11mosZNZjwpqnemXNnWs9E2Bnv7R6vzaKwJTdjo8zQ")
