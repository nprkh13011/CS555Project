import '../App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import { useNavigate } from 'react-router-dom';
import Logo from '../img/FibFinders_Logo.png';
import React, { useState } from 'react';
import Profiles from './Profiles.js';
import { Leaderboard } from './Leaderboard.js';
import './Rankings.css';

function Rankings() {

  const [period, setPeriod] = useState(0);
  const navigate = useNavigate();
  const handleClick = (e) => {
     
    setPeriod(e.target.dataset.id)
  }

  const shareResults = () => {
    const filteredLeaderboard = between(Leaderboard, period);
    const leaderboardText = filteredLeaderboard.map((item, index) => `${index + 1}. ${item.username}: ${item.score}`).join('\n');
    navigator.clipboard.writeText(leaderboardText)
      .then(() => {
        alert("Leaderboard copied to clipboard!");
      })
      .catch((error) => {
        console.error("Failed to copy leaderboard: ", error);
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
            <Profiles Leaderboard={between(Leaderboard, period)}></Profiles>
        </div>
    </div>
  )
}



function between(data, between){
    const today = new Date();
    const previous = new Date(today);
    previous.setDate(previous.getDate() - (between + 1));

    let filter = data.filter(val => {
        let userDate = new Date(val.dt);
        if (between == 0) return val;
        return previous <= userDate && today >= userDate;
    })

    // sort with asending order
    return filter.sort((a, b) => {
        if ( a.score === b.score){
            return b.score - a.score;
        } else{
            return b.score - a.score;
        }
    })

}

export default Rankings;