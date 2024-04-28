import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './Rankings.css';

export default function Profiles({ Leaderboard }) {
    return (
        <div id="profile">
            {Item(Leaderboard)}
        </div>
    )
}

function Item(data) {
    const [computedScores, setComputedScores] = useState([]);

    useEffect(() => {
        const fetchComputedScores = async () => {
            try {
                const response = await axios.get('http://localhost:3001/professors');
                const professorData = response.data;

                console.log('Professor Data:', professorData); // Log the fetched professor data

                const updatedScores = data.map((value, index) => {
                const matchingProfessor = professorData.find(p => p.index === index);
                console.log('Matching Professor:', matchingProfessor); // Log the matching professor
                if (matchingProfessor) {
                    const score =
                      (matchingProfessor.trueResponses /
                        matchingProfessor.totalTests) *
                      100;
                    console.log(`Calculated Score for ${value.name}: ${score}`); // Log the calculated score
                    return score.toFixed(2);
                } else {
                    return value.score;
                }
            });

                console.log('Updated Scores:', updatedScores); // Log the updated scores array

                // Log individual scores before setting the state
                updatedScores.forEach((score, index) => {
                    console.log(`Score for ${data[index].name}: ${score}%`);
                });

                setComputedScores(updatedScores);
            } catch (error) {
                console.error('Error fetching data:', error);
            }
        };
        
        fetchComputedScores(); // Call the fetchComputedScores function

    }, []); // Add a comma here

    return (
        <>
            {
                data.map((value, index) => (
                    <div className="flex" key={index}>
                        <div className="item">
                            <img src={value.img} alt="" />

                            <div className="info">
                                <h3 className='name text-dark'>{value.name}</h3>
                                <span>{value.location}</span>
                            </div>
                        </div>
                        <div className="item">
                            <span>{computedScores[index]}%</span>
                        </div>
                    </div>
                ))
            }
        </>
    )
}