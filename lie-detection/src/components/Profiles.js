import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './Rankings.css';

export default function Profiles({ Leaderboard }) {
    const [computedScores, setComputedScores] = useState([]);

    useEffect(() => {
        const fetchComputedScores = async () => {
            try {
                const response = await axios.get('http://localhost:3001/professors');
                const professorData = response.data;

                const updatedScores = Leaderboard.map((value, index) => {
                    const matchingProfessor = professorData.find(p => p.index === index);
                    if (matchingProfessor) {
                        const score = (matchingProfessor.trueResponses / matchingProfessor.totalTests) * 100;
                        console.log(`Calculated Score for ${value.name}: ${score}`);
                        return score.toFixed(2);
                    } else {
                        return value.score;
                    }
                });

                setComputedScores(updatedScores);
            } catch (error) {
                console.error('Error fetching data:', error);
            }
        };
        
        fetchComputedScores();
    }, [Leaderboard]);

    const computedScoresMap = {};
    computedScores.forEach((score, index) => {
        const professor = Leaderboard[index];
        computedScoresMap[professor.name] = score;
    });

    const sortedProfiles = Leaderboard.slice().sort((a, b) => {
        const scoreA = computedScoresMap[a.name];
        const scoreB = computedScoresMap[b.name];
        return scoreB - scoreA; // Sort in descending order
    });




    return (
        <div id="profile">
            {sortedProfiles.map((profile, index) => {
                const profileIndex = Leaderboard.findIndex(item => item.name === profile.name);
                const computedScore = computedScores[profileIndex];
                
                return (
                    <div className="flex" key={index}>
                        <div className="item">
                            <img src={profile.img} alt="" />
                            <div className="info">
                                <h3 className='name text-dark'>{profile.name}</h3>
                                <span>{profile.location}</span>
                            </div>
                        </div>
                        <div className="item">
                            <span>{computedScore}%</span>
                        </div>
                    </div>
                );
            })}
        </div>
    );
}
