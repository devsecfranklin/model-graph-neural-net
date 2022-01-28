# Manage Storage Key

## Setup


```sh
# doas apk update && doas apk add pass # install pass on alpine
gpg --list-keys # get your public key id
pass init C25565E4701F4ED36A0711AA114F3606EFD923BB # id of your public GPG key
```

## Store credentials in "pass" manager.


```sh
pass insert franklin-storage-key.json
pass ls
pass show franklin-storage-key.json
```
