const mongoose = require('mongoose');

const professorSchema = new mongoose.Schema({
    index: { // index of professor dependent on their order in Leaderboard.js in the front-end
        type: Number,
        required: true
    },
    totalTests: {
        type: Number,
        default: 0
    },
    trueResponses: {
        type: Number,
        default: 0
    }
});

module.exports = mongoose.model('Professor', professorSchema);