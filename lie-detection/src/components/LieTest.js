import React, { useState, useEffect } from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import { Navigate } from 'react-router-dom';
import Swal from 'sweetalert2';
import Progress from './Progress.js';
import axios from 'axios';
import Leaderboard from './Leaderboard.js';

import img1 from './images/image1.png';
import img2 from './images/image2.png';
import img3 from './images/image3.png';
import img4 from './images/image4.png';
import img5 from './images/image5.png';
import img6 from './images/image6.png';
import img7 from './images/image7.png';
import img8 from './images/image8.png';
import img9 from './images/image9.png';
import img10 from './images/image10.png';
import img11 from './images/image11.png';
import img12 from './images/image12.png';
import img13 from './images/image13.png';
import img14 from './images/image14.png';
import img15 from './images/image15.png';
import img16 from './images/image16.png';
import img17 from './images/image17.png';

const LieTest = () => {
    const [index, setIndex] = useState(0);
    const [endOfTest, setEndOfTest] = useState(false);
    const [redirectToHome, setRedirectToHome] = useState(false);
    const [imgList] = useState([
        img1, img2, img3, img4, img5, img6,
        img7, img8, img9, img10, img11, img12,
        img13, img14, img15, img16, img17
    ]);
    const [leaderboardWithScores, setLeaderboardWithScores] = useState([]);

    useEffect(() => {
        const fetchDataAndComputeScores = async () => {
            try {
                const response = await axios.get('http://localhost:3001/professors');
                const professorData = response.data;

                const updatedLeaderboard = Leaderboard.map(professor => {
                    const matchingProfessor = professorData.find(p => p.name === professor.name);
                    if (matchingProfessor) {
                        const score = (matchingProfessor.trueResponses / matchingProfessor.totalTests) * 100;
                        return {
                            ...professor,
                            score: score.toFixed(2)
                        };
                    } else {
                        return professor;
                    }
                });

                setLeaderboardWithScores(updatedLeaderboard);
            } catch (error) {
                console.error('Error fetching data:', error);
            }
        };

        fetchDataAndComputeScores();
    }, []);

    const onClickForward = () => {
        const professorIndex = index;
        const hasSeenProfessor = Math.random() < 0.5;

        axios.post('http://localhost:3001/update-professor', { professorIndex, hasSeenProfessor })
            .then(response => {
                console.log('Professor score updated successfully:', response.data, professorIndex, hasSeenProfessor);
            })
            .catch(error => {
                console.error('Error updating professor score:', error);
            });

        if (index + 1 === imgList.length) {
            setEndOfTest(true);
        } else {
            setIndex(index + 1);
        }
    };

    const returnHome = () => {
        Swal.fire({
            title: "Are You Sure?",
            text: "You Won't Be Able to Pick Up Where You Left Off",
            icon: "warning",
            showCancelButton: true,
            confirmButtonColor: "#3085d6",
            cancelButtonColor: "#d33",
            confirmButtonText: "Yes, Restart Test"
        }).then((result) => {
            if (result.isConfirmed) {
                setRedirectToHome(true);
            }
        });
    };

    const handleProgressChange = (value) => {
        setIndex(value - 1);
    };

    return (
        <div className="d-flex justify-content-center align-items-center vh-100">
            <div className="peach-container p-3 rounded text-center">
                <div className="progress-bar-container">
                    <Progress
                        style={{ marginTop: "50px", marginBottom: "50px" }}
                        current={index + 1}
                        onChange={handleProgressChange}
                    />
                </div>
                <div className="white-container p-3 m-2 rounded text-center">
                    <h1 className="lietest">
                        Have you taken a class with this professor?
                    </h1>
                    <div className="image-container my-4">
                        <img src={imgList[index]} alt={`Professor ${index + 1}`} />
                    </div>
                    <div className="button-container d-flex justify-content-between my-3">
                        {endOfTest && <Navigate to="/results" />}
                        <button
                            className="btn btn-primary rounded mx-2"
                            onClick={onClickForward}
                        >
                            Yes
                        </button>

                  <button
                    className="btn btn-primary rounded mx-2"
                    onClick={onClickForward}
                  >
                    No
                  </button>
                </div>
                <button
                  className="btn btn-danger rounded"
                  onClick={returnHome}
                  style={{ marginTop: "30px" }}
                >
                  Restart Test
                </button>
              </div>
            </div>
            <div className="d-flex justify-content-center"></div>
            {redirectToHome && <Navigate to="/home" />}
          </div>
        );
    }

export default LieTest;
