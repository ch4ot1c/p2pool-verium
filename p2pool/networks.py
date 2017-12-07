from p2pool.bitcoin import networks
from p2pool.util import math

# CHAIN_LENGTH = number of shares back client keeps
# REAL_CHAIN_LENGTH = maximum number of shares back client uses to compute payout
# REAL_CHAIN_LENGTH must always be <= CHAIN_LENGTH
# REAL_CHAIN_LENGTH must be changed in sync with all other clients
# changes can be done by changing one, then the other

nets = dict(
    verium=math.Object(
        PARENT=networks.nets['verium'],
        SHARE_PERIOD=15, # seconds
        CHAIN_LENGTH=12*60*60//15, # shares
        REAL_CHAIN_LENGTH=12*60*60//15, # shares
        TARGET_LOOKBEHIND=20, # shares
        SPREAD=10, # blocks
        IDENTIFIER='e037d5b8c6923610'.decode('hex'),
        PREFIX='7208c1a53ef659b0'.decode('hex'),
        P2P_PORT=8777,
        MIN_TARGET=0,
        MAX_TARGET=2**256//2**20 - 1,
        PERSIST=True,
        WORKER_PORT=8336,
        BOOTSTRAP_ADDRS='198.52.200.75'.split(' '),
        ANNOUNCE_CHANNEL='#p2pool-alt',
        VERSION_CHECK=lambda v: v >= 60011,
    ),
    verium_testnet=math.Object(
        PARENT=networks.nets['verium_testnet'],
        SHARE_PERIOD=15, # seconds
        CHAIN_LENGTH=12*60*60//15, # shares
        REAL_CHAIN_LENGTH=12*60*60//15, # shares
        TARGET_LOOKBEHIND=20, # shares
        SPREAD=10, # blocks
        IDENTIFIER='e037d5b8c7923110'.decode('hex'),
        PREFIX='7208c1a54ef619b0'.decode('hex'),
        P2P_PORT=18777,
        MIN_TARGET=0,
        MAX_TARGET=2**256//2**20 - 1,
        PERSIST=False,
        WORKER_PORT=18336,
        BOOTSTRAP_ADDRS='198.52.200.75'.split(' '),
        ANNOUNCE_CHANNEL='#p2pool-alt',
        VERSION_CHECK=lambda v: v >= 60011,
    ),
)
for net_name, net in nets.iteritems():
    net.NAME = net_name
