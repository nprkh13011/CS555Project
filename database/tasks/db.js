
const mongoose = require('mongoose');
const {MongoMemoryServer} = require('mongodb-memory-server');
let mongod = undefined;

//connect to the db
module.exports.connect = async() => {
    mongod = await MongoMemoryServer.create();
    const uri = mongod.getUri();
    await mongoose.connect(uri, {
        useNewUrlParser: true
    });
}

//close the connection and drop DB entirely
module.exports.closeDatabase = async() => {
    if (mongod){
        await mongoose.connection.dropDatabase();
        await mongoose.connection.close();
        await mongod.stop();
    }
    
}

//clear the DB and delete the collections from db
module.exports.dropCollections = async() => {
    if (mongod) {
    const collections = mongoose.connection.collections;
    for (const key in collections) {
        const collection = collections[key];
        await collection.deleteMany();
    }
}
}