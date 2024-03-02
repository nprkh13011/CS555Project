const mongoose = require('mongoose');
const users = require('../models/Users');
const db = require('./db');

const userModel = [
    {
        name: "Test1",
        email: "test1@gmail.com",
        password: "Testing1#"
    },
    {
        name: "Test2",
        email: "test2@gmail.com",
        password: "Testing2**"
    }
];

beforeAll(async () => {
    await db.connect();
});

afterEach(async () => {
    await db.dropCollections();
});

afterAll(async () => {
    await db.closeDatabase();
});

// User Model test - make sure user is created properly
describe('User Model', () => {
    const newUser = new users(userModel);
    for (let i=0; i < userModel.length; i++){
        it('Sign Up User successfully', async () =>{
            // const savedUser = await newUser.save();
            expect(newUser['_id']).toBeDefined();
            expect(newUser['name']).toBe(userModel['name']);
            expect(newUser['email']).toBe(userModel['email']);
            expect(newUser['password']).toBe(userModel['password']);     
        })
    }
})
