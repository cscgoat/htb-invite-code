### HackTheBox invite code solution

HackTheBox invite code solution including a keygen

- invite.py - Useful functions including rot13

- invite-keygen.py - Invite code generator. Spoiler!


##### NOTES:

`makeInviteCode()`

"Va beqre gb trarengr gur vaivgr pbqr, znxr n CBFG erdhrfg gb /ncv/vaivgr/trarengr"


`./invite.py rot13 "Va beqre gb trarengr gur vaivgr pbqr, znxr n CBFG erdhrfg gb /ncv/vaivgr/trarengr"`

In order to generate the invite code, make a POST request to /api/invite/generate

`curl -X POST https://www.hackthebox.eu/api/invite/generate`

{"success":1,"data":{"code":"Q0ZBREctRkhRTUUtWUNWUE4tQ0daUVktRkVWVkU=","format":"encoded"},"0":200}

`./invite.py decode Q0ZBREctRkhRTUUtWUNWUE4tQ0daUVktRkVWVkU=`

CFADG-FHQME-YCVPN-CGZQY-FEVVE