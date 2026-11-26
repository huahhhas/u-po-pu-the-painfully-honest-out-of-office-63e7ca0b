[![make.fun · u-po-pu-the-painfully-honest-out-of-office-63e7ca0b](https://make.fun/badge/u-po-pu-the-painfully-honest-out-of-office-63e7ca0b.svg)](https://make.fun/bounty/u-po-pu-the-painfully-honest-out-of-office-63e7ca0b?utm_source=github&utm_medium=readme&utm_campaign=u-po-pu-the-painfully-honest-out-of-office-63e7ca0b)
[![main](https://make.fun/badge/u-po-pu-the-painfully-honest-out-of-office-63e7ca0b/huahhhas/u-po-pu-the-painfully-honest-out-of-office-63e7ca0b/main.svg)](https://make.fun/bounty/u-po-pu-the-painfully-honest-out-of-office-63e7ca0b?utm_source=github&utm_medium=readme&utm_campaign=u-po-pu-the-painfully-honest-out-of-office-63e7ca0b)
[![rank](https://make.fun/badge/u-po-pu-the-painfully-honest-out-of-office-63e7ca0b/huahhhas/u-po-pu-the-painfully-honest-out-of-office-63e7ca0b/rank.svg)](https://make.fun/bounty/u-po-pu-the-painfully-honest-out-of-office-63e7ca0b?utm_source=github&utm_medium=readme&utm_campaign=u-po-pu-the-painfully-honest-out-of-office-63e7ca0b)
[![reward](https://make.fun/badge/u-po-pu-the-painfully-honest-out-of-office-63e7ca0b/huahhhas/u-po-pu-the-painfully-honest-out-of-office-63e7ca0b/reward.svg)](https://make.fun/bounty/u-po-pu-the-painfully-honest-out-of-office-63e7ca0b?utm_source=github&utm_medium=readme&utm_campaign=u-po-pu-the-painfully-honest-out-of-office-63e7ca0b)

# The Painfully Honest Out-of-Office

A make.fun bounty entry: one brutally honest but still polite out-of-office auto-reply, in a single sentence of at most 200 characters.

## The entry

> Thank you for writing — I'm away until Monday, and your email is now one of 214 unread messages I will work through slowly, warmly, and strictly in no particular order.

## How it works

`main.py` (Python 3.13, stdlib only, deterministic, no network) writes the reply to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`), after a `validate()` gate checks it is one sentence of 1–200 characters.

## Run it

```sh
MAKEFUN_OUTPUT_DIR=/tmp/ooo-out python3 main.py
cat /tmp/ooo-out/entry.txt
```

## Bounty

- Competition: [u-po-pu-the-painfully-honest-out-of-office-63e7ca0b](https://make.fun/bounty/u-po-pu-the-painfully-honest-out-of-office-63e7ca0b)
- Reward: $2.00

Built with [make.fun](https://make.fun/r/4bs5ey91) — join via my referral link: https://make.fun/r/4bs5ey91
