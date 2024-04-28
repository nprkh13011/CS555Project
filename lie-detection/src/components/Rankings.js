import '../App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import { useNavigate } from 'react-router-dom';
import Logo from '../img/FibFinders_Logo.png';
import React, { useState } from 'react';
import Profiles from './Profiles.js';
import LeaderboardData from './Leaderboard.js'; // Import the Leaderboard data directly
import './Rankings.css';
import axios from 'axios';
import html2canvas from 'html2canvas';

function Rankings() {
  const [period, setPeriod] = useState(0);

  const navigate = useNavigate();
  const handleClick = (e) => {
    setPeriod(e.target.dataset.id)
  };

  const shareResults = () => {
    const leaderboardElement = document.querySelector('.profs');
  
    html2canvas(leaderboardElement)
      .then(canvas => {
        const image = canvas.toDataURL(); // Convert canvas to image data URL
        const link = document.createElement('a');
        link.href = image;
        link.download = 'leaderboard.png'; // Set the filename for the downloaded image
        
        // Prompt the user before downloading
        const confirmed = window.confirm('Do you want to download your leaderboard to share?');
        if (confirmed) {
          link.click(); // Trigger the download
        }
      })
      .catch(error => {
        console.error('Error while capturing screenshot:', error);
      });
  };
  

  return (
    <div className="board">
      <h1 className='leaderboard'>Leaderboard</h1>

      <div className="duration">
        <button onClick={() => navigate('/home')}>Home</button>
        <button onClick={() => navigate('/instructions')}>Start Test</button>
        <button onClick={shareResults}>Share Results</button>
        <button onClick={() => navigate('/logout')}>Logout</button>
      </div>

      <div className="profs">
        <Profiles Leaderboard={LeaderboardData} period={period} /> {/* Pass LeaderboardData as prop */}
      </div>
    </div>
  );
}

async function between(data, between) {
    console.log('Data:', data)
    const today = new Date();
    const previous = new Date(today);
    previous.setDate(previous.getDate() - (between + 1));

    try {
        const response = await axios.get('http://localhost:3001/professors');
        const professorData = response.data;

        const updatedScores = data.map((value, index) => {
            const matchingProfessor = professorData.find(p => p.index === index);
            if (matchingProfessor) {
                const score = (matchingProfessor.trueResponses / matchingProfessor.totalTests) * 100;
                return score.toFixed(2);
            } else {
                return value.score;
            }
        });

        return updatedScores.sort((a, b) => a - b);
    } catch (error) {
        console.error('Error fetching data:', error);
        return data.map(() => 0); // Return zero scores if there's an error
    }
}


export default Rankings;