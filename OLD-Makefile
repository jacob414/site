SSH_ALIAS=jacob@cirrus:src/mine/site/

.PHONY: download
download:
	rsync -ar $(SSH_ALIAS) ./

.PHONY: live
live:
	rsync -ar ./ $(SSH_ALIAS)

