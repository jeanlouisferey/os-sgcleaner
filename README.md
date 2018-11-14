# os-sgcleaner
List openstack security groups which aren't used by any servers and delete its if you want.

## usage:
CloudName is the name of your openstack tenant defined in clouds.yml
or in openstack rc file

```shell
python os-sgcleaner.py CloudName
```
to list all sg unused

```shell
python os-sgcleaner.py CloudName --deletesg
```
to delete all sg unused

## Disclaimer
I could not be held responsible for the possible disappearance of your security groups. Please check what you want to do before using --deletesg switch.
