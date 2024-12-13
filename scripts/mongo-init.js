// Что-то подобное можно было бы использовать в качестве скрипта
// для инициализации монго, но я в этом пока не разбирался ¯\_(ツ)_/¯
db = connect('mongodb://mongodb:27017');
db = db.getSiblingDB('admin');

db.auth('root', 'root');

db = db.getSiblingDB('forms');

db.createUser({
    'user': 'user',
    'pwd': 'pwd',
    'roles': [{
        'role': 'dbOwner',
        'db': 'forms'
    }]
});

db.createCollection('init');
