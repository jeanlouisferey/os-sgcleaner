# os-sgcleaner
List openstack security groups which aren't used by any servers

# usage:
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
