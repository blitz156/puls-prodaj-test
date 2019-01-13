from fabric.api import local


def restore_backup(path):
    if '.dump' in path:
        binary = 'True'
    elif '.sql' in path:
        binary = 'False'
    elif path == '':
        return

    if binary == 'True':
        cmd = "docker exec -i $(docker ps | grep db_ | awk '{{ print $1 }}') pg_restore --no-acl --no-owner -U postgres -d postgres < {0}".format(path)
    else:
        cmd = "docker exec -i $(docker ps | grep db_ | awk '{{ print $1 }}') psql -U postgres -d postgres < {0}".format(path)

    local(cmd)


def migrate(app=''):
    local("docker exec -i $(docker ps | grep server_ | awk '{{ print $1 }}') python manage.py migrate {}".format(app))


def createsuperuser():
    local("docker exec -it $(docker ps | grep server_ | awk '{{ print $1 }}') python manage.py createsuperuser")


def makemigrations(app=''):
    local("docker exec -i $(docker ps | grep server_ | awk '{{ print $1 }}') python manage.py makemigrations {}".format(app))


def bash():
    local("docker exec -it $(docker ps | grep server_ | awk '{{ print $1 }}') bash")


def shell():
    local("docker exec -it $(docker ps | grep server_ | awk '{{ print $1 }}') python manage.py shell")


def dev():
    local('docker-compose run --rm --service-ports server')


